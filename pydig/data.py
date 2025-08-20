# pydig/data.py

from configparser import ConfigParser
from pathlib import Path
from pydig import (
    __app_name__,
    AppDataError,
    InternetConnectionError
)
from pydig.config import Config
import requests as req

DEFAULT_OUTPUT_LOCATION = Path.home().joinpath(f"{__app_name__}_output")

def _create_app_output_location(otdata : Path) -> int :
    config_file = Config(otdata=otdata)
    config_file.write()
    try :
        otdata.mkdir(exist_ok=True)
    except AppDataError:
        raise AppDataError(":( failed to make output app folder!")
    return True

# checking if user is connected
class NetworkConnection :
    def __init__(self, url = "https://clients3.google.com/generate_204", timeout = 5) :
        self.__url = url
        self.__timeout = timeout
    @property
    def url(self) -> str : return self.__url
    @property
    def timeout(self) -> int : return self.__timeout

    @url.setter
    def url(self, url : str) -> None : self.__url = url
    @timeout.setter
    def timeout(self, timeout : int) -> None : self.__timeout = timeout

    def is_connected(self) -> bool :
        try :
            req.get(url=self.__url, timeout=self.__timeout)
        except  InternetConnectionError:
            raise InternetConnectionError(":( you're not connect to the internet!")
        return True

# handling youtube downloads
class YoutubeModel : ...

# handling instagram downloads
class InstagramModel : ...

# handling tiktok downloads
class TiktokModel : ...

# handling facebook downloads
class FacebookModel : ...

# handling pinterest downloads
class PinterestModel : ...
