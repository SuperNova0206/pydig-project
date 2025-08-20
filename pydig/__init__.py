# pydig/__init__.py

__version__ = "0.1.0"
__app_name__ = "pydig"


class AppErrors(Exception) :
    def __init__(self, message : str) -> None :
        self.message = message
        super().__init__(self.message)

class ConfigureError(AppErrors) : pass
class ConfigurationFileError(AppErrors) : pass
class AppDataError(AppErrors) : pass
class InternetConnectionError(AppErrors) : pass
class SetupError(AppErrors) : pass