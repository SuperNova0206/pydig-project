# pydig/pydig.py

from pydig import config, exceptions
from pytubefix import YouTube
from configparser import ConfigParser
import subprocess
import os


config_parser = ConfigParser()
config_parser.read(config.Config.DEFAULT_CONFIG_FILE_PATH)
PATH : str = config_parser["General"]["output"]

class YouTubeContoller :
    def __init__(self, url : str, resolution : bool) -> None :
        self.url = url
        self.resolution = 0 if not resolution else resolution

    # download data as form of mp3 (audio)
    def audio(self) -> None :
        global PATH
        PATH += "/youtube/audios"
        try :
            yt = YouTube(self.url)
            yt.streams.filter(only_audio=True).first().download(output_path=PATH)
        except exceptions.YouTubeError :
            raise exceptions.YouTubeError(f":( couldn't download audio from \"{self.url}\"!")
        return [yt.title, PATH]

    # downloading data as form mp4 (video)
    def video(self) -> None :
        global PATH
        PATH += "/youtube/videos"
        try :
            yt = YouTube(self.url)
            yt.streams.filter(res=self.resolution, adaptive=True, file_extension="mp4").first().download(output_path=PATH, filename="video.mp4")
            yt.streams.filter(only_audio=True).first().download(output_path=PATH, filename="audio.mp3")
            subprocess.run(
                [
                "ffmpeg",
                "-i", PATH + "/video.mp4",
                "-i", PATH + "/audio.mp3",
                "-c:v", "copy",
                "-map", "0:v:0",
                "-map", "1:a:0",
                "-c:a", "copy",
                PATH + f"/{yt.title}.mp4"
                ],
                check=True
            )
            os.remove(PATH + f"/video.mp4")
            os.remove(PATH + f"/audio.mp3")
        except exceptions.YouTubeError :
            raise exceptions.YouTubeError(f":( we coudn't download video form \"{self.url}\"")
        return [yt.title, PATH]


# dealing with instagram actions
class InstagramController : ...

# dealing with tiktok actions
class TiktokController : ...

# dealing with facebook actions
class FacebookController : ...

# dealing with pinterset actions
class PinterestController : ...



