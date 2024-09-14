Задание 1

```
cat /etc/protocols | sort -k 2,2nr | head -n 5 | awk '{print $2, $1}'
```
****![image](https://github.com/user-attachments/assets/7314ed58-c8fc-410e-8730-365a1f1a8405)

Задание 2

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
****(![image](https://github.com/user-attachments/assets/fab90c9c-3dfa-45f3-9664-f18dd9798501)

Задание 3

```
#!/bin/bash

text=$*
length=${#text}

# Формирование символов рамки от 1 до длины слова + 2 пробела
for _ in $(seq 1 $((length + 2))); do
    line+="-"
done

echo "+${line}+"
echo "| ${text} |"
echo "+${line}+"
```

Задание 4

```
#!/bin/bash

file="$1"

identifiers=$(grep -o -E '\b[a-zA-Z]*\b' "$file" | sort -u)

echo "Идентификаторы:"
echo "$identifiers"
```

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