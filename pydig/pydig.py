# pydig/pydig.py

from pydig import config, exceptions
from pytubefix import YouTube
from configparser import ConfigParser
import ffmpeg
from pathlib import Path


config_parser = ConfigParser()
config = config.Config()


class YouTubeContoller :
    def __init__(self, url : str, resolution : bool) -> None :
        self.url = url
        self.resolution = 0 if not resolution else resolution

    # download data as form of mp3 (audio)
    def audio(self) -> None :
        """:( something wrong with this PATH it can't read ```config.ini``` correctly"""
        PATH = config_parser["General"]["output"].join("/youtube/mp3")
        try :
            yt = YouTube(self.url)
            yt.streams.filter(only_audio=True).first().download(output_path=PATH)
        except exceptions.YouTubeError :
            raise exceptions.YouTubeError(f":( couldn't download audio from \"{self.url}\"!")
        return [yt.title, PATH]

    # downloading data as form mp4 (video)
    def video(self) -> None : ...


# dealing with instagram actions
class InstagramController : ...

# dealing with tiktok actions
class TiktokController : ...

# dealing with facebook actions
class FacebookController : ...

# dealing with pinterset actions
class PinterestController : ...



