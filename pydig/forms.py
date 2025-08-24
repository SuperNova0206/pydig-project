# pydig/forms.py

from enum import Enum

# youtube data forms
class YoutubeForms(str, Enum):
    MP3 = "mp3",
    MP4 = "mp4"

# instagram data forms
class InstagramForms(str, Enum) :
    VIDEO = "mp4"
    PIC = "png"

# tiktok data forms
class TiktokFormats(str, Enum) : ...

# facebook data forms
class FacebookFormats(str, Enum) : ...

# pinterst data forms
class PinterestFormats(str, Enum) : ...