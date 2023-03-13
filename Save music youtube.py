from pytube import YouTube

# Запрос URL видео и разбивка его на части
url = input("Введите URL видео на YouTube: ")
yt = YouTube(url)

# Печать доступных потоков
print("Доступные потоки для загрузки:")
for stream in yt.streams.filter(only_audio=True, mime_type="audio/webm"):
    print(stream.abr + " (" + "itag=" + str(stream.itag) + ")")
    

# Выбор потока и скачивание аудиофайла
itag = input("Выберите ITAG для потока, который нужно загрузить: ")
stream = yt.streams.get_by_itag(itag)
print("Скачивание аудиофайла...")
stream.download(output_path="Download", filename_prefix="audio_")
print("Аудиофайл успешно загружен!")