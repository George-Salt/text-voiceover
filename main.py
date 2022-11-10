import os

from dotenv import load_dotenv
from gtts import gTTS
from playsound import playsound


def get_text(filepath):
    if os.path.isfile(filepath):
        with open(filepath, "r", encoding="UTF-8") as file:
            text = file.read().replace("\n", " ")
    else:
        print(f"Файла {filepath} не существует!")
        exit()
    return text


def save_audio(text, filepath):
    audio = gTTS(text=text, lang="ru")
    audio.save(filepath)
    return f"Файл с аудио сохранен в {filepath}."


if __name__ == "__main__":
    load_dotenv()
    textfile_name = os.getenv("TEXTFILE_NAME")
    audiofile_name = os.getenv("AUDIOFILE_NAME")
    folder = os.getenv("OBJ_FOLDER_NAME", default="objects")

    textfilepath = os.path.join(folder, textfile_name)
    audiofilepath = os.path.join(folder, audiofile_name)

    text = get_text(textfilepath)
    save_audio(text, audiofilepath)

    playsound(audiofilepath)
