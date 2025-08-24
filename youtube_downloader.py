import os
import yt_dlp


def download_video(url):
    desktop_path = os.path.expanduser("~/Desktop")
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(desktop_path, '%(title)s.%(ext)s'),
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        print(f"Title: {info['title']}")
        print("Download finished successfully.")


if __name__ == "__main__":
    url = input("Enter YouTube URL: ")
    if url.strip():
        download_video(url)
    else:
        print("Invalid URL.")
