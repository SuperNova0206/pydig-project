# pydig/config.py

from pathlib import Path
from configparser import ConfigParser
import typer
from  pydig import (
    __app_name__,
    ConfigureError,
    ConfigurationFileError
)

config_parser = ConfigParser()

class Config :
    DEFAULT_CONFIG_DIR_PATH = Path(typer.get_app_dir(__app_name__))
    DEFAULT_CONFIG_FILE_PATH = DEFAULT_CONFIG_DIR_PATH / "config.ini"
    def __init__(self, otdata = "") -> None :
        self.__otdata = otdata

    @property
    def  otdata(self) -> Path : return self.__otdata

    @otdata.setter
    def otdata(self, otdata : Path) -> None : self.otdata = otdata

    def write(self) -> bool:
        try :
            Config.DEFAULT_CONFIG_DIR_PATH.mkdir(exist_ok=True)
        except ConfigureError:
            raise ConfigureError(":( configuration file folder failed to create!")

        try :
            Config.DEFAULT_CONFIG_FILE_PATH.touch(exist_ok=True)
        except ConfigureError :
            raise ConfigureError(":( configuration file failed to create!")

        config_parser.read(Config.DEFAULT_CONFIG_FILE_PATH)
        config_parser["General"] = {"OUTPUT" : str(self.otdata)}

        try :
            with Config.DEFAULT_CONFIG_FILE_PATH.open("w") as f :
                config_parser.write(f)
        except ConfigurationFileError :
            raise ConfigurationFileError(":( writing data to configuration file failed!")
        return True
