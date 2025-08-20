# pydig/cli.py

from pydig import (
    __version__,
    __app_name__,
    SetupError,
    data,
    forms,
    pydig,
    qualities,
    config
)
from typing import Optional
import typer
from pathlib import Path
import re
from datetime import date
from configparser import ConfigParser

app = typer.Typer(help="pydig CLI media downloader")
config_parser = ConfigParser()
config = config.Config()



def _version_fun(respond : bool) -> None :
    if respond :
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

# setup
@app.command(help="initializing pydig CLI app")
def setup() -> None:
    _data_error = data._create_app_output_location(otdata=data.DEFAULT_OUTPUT_LOCATION)
    if _data_error :
        typer.secho(
            f":) well done!",
            fg = typer.colors.GREEN
        )
        raise typer.Exit()
    raise SetupError(":( application setup failed!")

# download
# @app.command(help="download data from youtube platform")
# def youtube(
#     # youtube video url
#     url : str,
#     # form mp3 | mp4
#     form : forms.YoutubeForms = typer.Option(
#         forms.YoutubeForms.MP4,
#         "--form",
#         "-f",
#         help="available forms (MP3 | MP4)"
#     ),
#     # video quality [144, 240, 360, 480, 720, 1080]
#     quality : qualities.YoutubeQuality = typer.Option(
#         qualities.YoutubeQuality.Q3.value,
#         "--quality",
#         "-q",
#         help="available qualities"
#     )
# ) -> None :
#     # check if the user is connected
#     is_connected = data.NetworkConnection().is_connected()
#     if not is_connected:
#         typer.secho(
#             f":( {ERRORS[is_connected]}",
#             fg = typer.colors.RED
#         )
#         raise typer.Exit(1)

#     # downloading data
#     youtube = pydig.YoutubeController(url=url, form=form, quality=quality)
#     if youtube.is_valid() != SUCCESS:
#         typer.secho(
#             f":( {ERRORS[youtube.is_valid()]}",
#             fg = typer.colors.RED
#         )
#         raise typer.Exit(1)
#     download  = youtube.download()
#     if download != SUCCESS :
#         typer.secho(
#             f":( {ERRORS[download]}, {youtube.quality}",
#             fg = typer.colors.RED
#         )
#         raise typer.Exit(1)
#     config_parser.read([config.DEFAULT_CONFIG_FILE_PATH])
#     typer.secho(
#         f":) data downloaded success [{config_parser['General']['output']}]"
#     )



@app.callback()
def main(
    version : Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        callback=_version_fun,
        is_eager=True
    )
) -> None : return