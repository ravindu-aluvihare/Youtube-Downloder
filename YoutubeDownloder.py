import yt_dlp

link = input("Enter Youtube video link: ")
ydl_opts = {}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])

print("Downloaded successfully")
