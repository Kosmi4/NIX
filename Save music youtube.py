from pytube import YouTube

# URL
url = input("Insert URL YouTube: ")
yt = YouTube(url)

# Itags in video
print("Itag's:")
for stream in yt.streams.filter(only_audio=True, mime_type="audio/webm"):
    print(stream.abr + " (" + "itag=" + str(stream.itag) + ")")
    

# pick video 
itag = input("pick ITAG: ")
stream = yt.streams.get_by_itag(itag)
print("Downloading file...")
stream.download(output_path="Download", filename_prefix="audio_")
print("Downloading finished")
