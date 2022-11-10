# Озвучка текста

Пользователь предоставляет текст, а программа конвертирует его в аудио, сохраняет и озвучивает.

## Установка

Для работы программы понадобится `Python 3`. Если у вас он не установлен, воспользуйтесь [статьей по его установке]("https://docs.microsoft.com/ru-ru/windows/python/beginners#install-python").
Скачайте форк репозитория себе на компьютер. Установите зависимости командой в папке проекта:
```sh
pip install -r requirements.txt
```
Создайте папку, в которой будут храниться файлы, используемые в процессе выполнения работы программы (файл с текстом, готовое аудио). В этой папке создайте файл с расширением `.txt`, затем поместите в него свой текст.

## Настройка файла .env

Создайте файл `.env`. Поместите в переменную `TEXTFILE_NAME` название текстового файла и в переменную `AUDIOFILE_NAME` желаемое название файла с аудио на выходе. Также создайте переменную `OBJ_FOLDER_NAME` с названием папки. Важно указывать расширения файлов `.txt` и `.mp3`.
```
TEXTFILE_NAME="text.txt"
AUDIOFILE_NAME="audio.mp3"
OBJ_FOLDER_NAME="folder"
```

## Запуск

Перейдите в командную строку. Вам поможет пункт `Запуск командной строки в Проводнике` [статьи по командной строке]("https://wp-seven.ru/instruktsii/tips/windows-10-tips/komandnaya-stroka-v-windows-10.html#:~:text=В%20Windows%2010%201607%20Anniversary,затем%20на%20Открыть%20командную%20строку").
Для запуска используюте команду в папке проекта:
```sh
python main.py
```

## Автор

George Salt: [Вконтакте]("https://vk.com/george_salt"), [YouTube]("https://www.youtube.com/@george20097").