Задание 1


****<img width="722" alt="Снимок экрана 2024-09-21 в 4 55 29 PM" src="https://github.com/user-attachments/assets/81de3178-db57-4c8e-9994-4ae47c78abf2">


Задание 2

```
cat /etc/protocols | sort -k 2,2nr | head -n 5 | awk '{print $2, $1}'
```
****<img width="788" alt="Снимок экрана 2024-09-30 в 6 08 44 PM">


Задание 3

```
x=input()
print ('+', end ="")
y=[print ('-', end='') for i in range(len(x)+2)]
print ('+')
print (f"|{x}|")
print ('+', end ="")
y=[print ('-', end='') for i in range(len(x)+2)]
print ("+")
```

****![image](https://github.com/user-attachments/assets/29f50776-43cc-4aa2-83b7-e97a45c8a0b0)


Задание 4

```
#!/bin/bash

file="$1"

identifiers=$(grep -o -E '\b[a-zA-Z]*\b' "$file" | sort -u)

echo "Идентификаторы:"
echo "$identifiers"
```

****<img width="346" alt="Снимок экрана 2024-09-29 в 5 26 43 PM" src="https://github.com/user-attachments/assets/66373aec-d9f5-44d0-9c13-e79668baed61">



Задание 5

```
#!/bin/bash

file=$1

# 755 - Чтение, запись, исполнение - Владалец | Чтение, исполнение - Другие пользователи
chmod 755 "./$file"

# Копируем команду в /usr/local/bin
sudo cp "$file" /usr/local/bin/

echo "Файл '$file' скопирован в usr/local/bin/, права были выданы"
```

Задание 6

```
#!/bin/bash

for file in *.c *.js *.py; do
    # Чтение первой строки с начала
    line=$(head -n 1 "$file")
    if [[ $line == "#"* || $line == "//"* || $line == "/*"* ]]; then
        echo "Файл $file начинается с комментария"
    else
        echo "Файл $file не начинается с комментария"
    fi
done
```

Задание 7

```
#!/bin/bash

# Хеш-таблица
declare -A duplicats

# Рекурсивная функция для поиска и вывода дубликатов
findDuplicates() 
{
    local dir="$1"
    
    # Перебираем все файлы и подкаталоги в данном каталоге
    for file in "$dir"/*; do
        # Если файл
        if [[ -f "$file" ]]; then
            # оставляем только имя файла
            file=$(basename "$file")
            if [ duplicats["$file"] ]; then
                # Добавляем +1
                duplicats["$file"]=$((duplicats["$file"] + 1))
            else
                duplicats["$file"]=1
            fi

            if [ "${duplicats["$file"]}" -eq 2 ]; then
                echo "Файл-дубликат - '$file'"
            fi
        # Если подкаталог
        elif [[ -d "$file" ]]; then
            # Рекурсивно вызываем данную функцию
            findDuplicates "$file"
        fi
    done
}

findDuplicates "."
```

Задание 8

```
#!/bin/bash

# Ищем все файлы с заданным расширением в текущем каталоге и сохраняем их в массиве
files=( $(find . -type f -name "*.$1") )

# Создаем архив файлов без повторений
tar -cvf "archive.tar" "${files[@]}"

echo "Архив создан"
```

Задание 9

```
#!/bin/bash

# sed s/что_заменять/на_что_заменять/опции
# g - Замените все вхождения строки в файле
# > - передача вывода второму аргументу
sed 's/    /\t/g' "$1" > "$2"

# Выводим сообщение об успешном завершении скрипта
echo "Файл исправлен"
```

Задание 10

```
#!/bin/bash

# sed s/что_заменять/на_что_заменять/опции
# g - Замените все вхождения строки в файле
# > - передача вывода второму аргументу
sed 's/    /\t/g' "$1" > "$2"

# Выводим сообщение об успешном завершении скрипта
echo "Файл исправлен"
```
