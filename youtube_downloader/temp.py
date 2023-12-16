import pytube
from tkinter import filedialog
import tkinter

def youtube_downloader(url, save_path):
    video = pytube.YouTube(url).streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()
    print("Video downloading...")
    video.download(output_path= save_path)
    print("Video downloaded")

if __name__ == "__main__":
    tkinter.Tk().withdraw()
    url = input("Enter a youtube video url : ")
    save_dir = filedialog.askdirectory()
    youtube_downloader(url, save_dir)