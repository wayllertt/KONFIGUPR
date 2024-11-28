import os
import tarfile
import json
import tkinter as tk
from tkinter import messagebox
import xml.etree.ElementTree as ET

class ShellEmulator:
    def __init__(self, config_file):
        self.load_config(config_file)
        self.current_dir = '/'
        self.file_system = None
        self.load_vfs()

    def load_config(self, config_file):
        tree = ET.parse(config_file)
        root = tree.getroot()
        self.hostname = root.find('hostname').text
        self.vfs_image = root.find('vfs_image').text
        self.log_file = root.find('log_file').text

    def load_vfs(self):
        with tarfile.open(self.vfs_image, 'r') as tar:
            self.file_system = tar
            self.file_system.extractall(path='/tmp/vfs')

    def execute_command(self, command):
        command_parts = command.split()
        cmd = command_parts[0]

        if cmd == 'ls':
            return self.ls()
        elif cmd == 'cd':
            if len(command_parts) < 2:
                return "Error: cd requires a directory path"
            return self.cd(command_parts[1])
        elif cmd == 'exit':
            self.exit_shell()
        elif cmd == 'cp':
            if len(command_parts) < 3:
                return "Error: cp requires two arguments"
            return self.cp(command_parts[1], command_parts[2])
        elif cmd == 'echo':
            return self.echo(" ".join(command_parts[1:]))
        elif cmd == 'pwd':
            return self.pwd()
        else:
            return f"Unknown command: {cmd}"

    def ls(self):
        try:
            files = os.listdir(self.current_dir)
            return "\n".join(files)
        except FileNotFoundError:
            return f"Directory {self.current_dir} not found."

    def cd(self, directory):
        new_dir = os.path.join(self.current_dir, directory)
        if os.path.isdir(new_dir):
            self.current_dir = new_dir
            return f"Changed directory to {self.current_dir}"
        else:
            return f"Directory {directory} not found."

    def exit_shell(self):
        self.save_log()
        exit()

    def cp(self, src, dest):
        try:
            if not os.path.exists(src):
                return f"File {src} not found."
            with open(src, 'rb') as fsrc:
                data = fsrc.read()
            with open(dest, 'wb') as fdest:
                fdest.write(data)
            return f"Copied {src} to {dest}"
        except Exception as e:
            return f"Error copying file: {str(e)}"

    def echo(self, text):
        return text

    def pwd(self):
        return self.current_dir

    def save_log(self):
        log_data = {"hostname": self.hostname, "last_session": []}
        with open(self.log_file, 'w') as log_file:
            json.dump(log_data, log_file, indent=4)

    def run(self):
        root = tk.Tk()
        root.title(f"{self.hostname} Shell Emulator")
        self.text_box = tk.Text(root, height=20, width=80)
        self.text_box.pack()
        self.entry = tk.Entry(root, width=80)
        self.entry.pack()
        self.entry.bind("<Return>", self.on_enter)
        root.mainloop()

    def on_enter(self, event):
        command = self.entry.get()
        self.entry.delete(0, tk.END)
        output = self.execute_command(command)
        self.text_box.insert(tk.END, f"{self.hostname}: {self.current_dir}$ {command}\n{output}\n")
        self.text_box.yview(tk.END)

if __name__ == "__main__":
    config_file = 'config.xml'
    emulator = ShellEmulator(config_file)
    emulator.run()

