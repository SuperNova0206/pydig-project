"""Handling pydig app Errors"""

# pydig/exceptions.py

class AppErrors(Exception) :
    def __init__(self, message : str) -> None :
        self.message = message
        super().__init__(self.message)

class SetupError(AppErrors) : pass
class YouTubeError(AppErrors) : pass