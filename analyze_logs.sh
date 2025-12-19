#!/bin/bash

exec > report.txt  #Сохранение stdout в файл

echo -e "Отчет о логе веб-сервера\n========================"

# Подсчет общего количества запросов
count=0
while read -r line; do
  count=$((count + 1))
done < access.log
echo "Общее количество запросов: $count"

# Подсчёт уникальных IP
awk '{i+=!a[$1]++}
     END {print "Количество уникальных IP-адресов:", i}' access.log

# Подсчёт методов
echo -e "\nКоличество запросов по методам:"
awk '
{
  if (match($0, /"[A-Z]+ /)) {
    m = substr($0, RSTART + 1, RLENGTH - 2)
    count[m]++
  }
}
END {
  for (m in count)
    printf "%5d %s\n", count[m], m
}
' access.log | sort -nr

# Самый популярный URL
echo
awk '
{
  if (match($0, /\/[a-z]+\.[a-z]+/)) {
    u = substr($0, RSTART, RLENGTH)
    count[u]++
  }
}
END {
  max = 0
  for (u in count)
    if (count[u] > max) {
      max = count[u]
      key = u
    }
  printf "Самый популярный URL: %d %s\n", max, key
}
' access.log

echo "Отчет сохранен в файл report.txt" >&2   #Выведет после исполнения в консоль
