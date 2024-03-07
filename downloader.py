import os
from pytube import YouTube

class Downloader(object):

    def download_mp3(self , folder ,urls):
        for url in urls:
            try:
                yt = YouTube(url)
            
            except Exception as e:
                print(e)
                print("Error downloading a song.Continuing..")
                continue
            else:
                print(f"Downloading {yt.title} ...")
                song = yt.streams.filter(only_audio = True ).first()
                out_file = song.download(folder)
                file_name = out_file.rsplit("." , 1)[0] # get the name without the extension(remove .mp4 extension)
                os.rename(out_file , file_name + ".mp3") # add .mp3 extension 

    
    def __str__(self):
        # returns a help menu
        st = ""
        st += "-" * 17 + " MP3 - DOWNLOADER " + "-" * 17 + "\n"
        st += "run: python3 main.py <folder-to_download_in> <url(s)>\n"
        st += "-" * 53 + "\n"
        return st
    

    
