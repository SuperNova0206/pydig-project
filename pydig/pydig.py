# pydig/pydig.py

from pydig import (
    config
)
from pytubefix import YouTube
import re
from configparser import ConfigParser
import ffmpeg
from pathlib import Path


config_parser = ConfigParser()
config = config.Config()


# dealing with youtube actions
# class YoutubeController :
#     def __init__(self, url : str, form : str, quality : int) -> None :
#         self.__url = url
#         self.__form = form
#         self.__quality = quality

#     @property
#     def url(self) -> str : return self.__url
#     @url.setter
#     def url(self, url : str) -> None : self.__url = url

#     @property
#     def form(self) -> int : return self.__form
#     @form.setter
#     def form(self, form : int) -> None : self.__form = form


#     @property
#     def quality(self) -> str : return self.__quality
#     @quality.setter
#     def quality(self, quality : str) -> None : self.__quality = quality

#     def download(self) -> int :
#         yt = YouTube(url=self.__url)
#         config_parser.read(config.DEFAULT_CONFIG_FILE_PATH)
#         if self.__form == "mp3" :
#             try :
#                 PATH = config_parser["General"]["output"] + "/youtube/mp3"
#                 stream = yt.streams.filter(only_audio=True).first()
#                 stream.download(output_path=PATH)
#                 return SUCCESS
#             except :
#                 return DOWNLOAD_DATA_ERROR
#         else :
#             try :
#                 # TODO : making the app able to download data from youtube with user choosed resolution
#                 PATH = config_parser["General"]["output"] + "/youtube/mp4"
#                 return SUCCESS
#             except :
#                 return DOWNLOAD_DATA_ERROR

#     def is_valid(self) -> int :
#         return SUCCESS if re.search(r'^(?:https?://)?(?:www\.)?youtube\.com/watch\?v=([A-Za-z0-9_-]{11})', self.__url) else DATA_ERROR
#     def audio(self) -> int : ...



# dealing with instagram actions
class InstagramController : ...

# dealing with tiktok actions
class TiktokController : ...

# dealing with facebook actions
class FacebookController : ...

# dealing with pinterset actions
class PinterestController : ...



