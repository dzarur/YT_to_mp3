import os
import yt_dlp

def download(link: str):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3'}],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
    except Exception as e:
        print("{e}")

download("https://www.youtube.com/watch?v=qIXyu-BexSk")