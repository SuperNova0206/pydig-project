# pydig/cli.py

from pydig import (
    __version__,
    __app_name__,
    SUCCESS,
    ERRORS,
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
    if _data_error != SUCCESS :
        typer.secho(
            f":( Oops something wrong: {ERRORS[_data_error]}",
            fg = typer.colors.RED
        )
        raise typer.Exit(1)

    typer.secho(
        f":) well done!",
        fg = typer.colors.GREEN
    )

# download
#! not yet still have a problem while downloading video
@app.command(help="download data from youtube platform")
def youtube(

    url : str,

    form : forms.YoutubeForms = typer.Option(
        forms.YoutubeForms.MP4,
        "--form",
        "-f",
        help="available forms (MP3 | MP4)"
    ),

    quality : qualities.YoutubeQuality = typer.Option(
        qualities.YoutubeQuality.Q3,
        "--quality",
        "-q",
        help="available qualities"
    )
) -> None :
    # check if the user is connected
    is_connected = data.NetworkConnection().is_connected()
    if is_connected != SUCCESS :
        typer.secho(
            f":( {ERRORS[is_connected]}",
            fg = typer.colors.RED
        )
        raise typer.Exit(1)

    # downloading data
    youtube = pydig.YoutubeController(url=url, form=form, quality=quality)
    if youtube.is_valid() != SUCCESS:
        typer.secho(
            f":( {ERRORS[youtube.is_valid()]}",
            fg = typer.colors.RED
        )
        raise typer.Exit(1)
    download  = youtube.download()
    if download != SUCCESS :
        typer.secho(
            f":( {ERRORS[download]}",
            fg = typer.colors.RED
        )
        raise typer.Exit(1)
    config_parser.read([config.DEFAULT_CONFIG_FILE_PATH])
    typer.secho(
        f":) data downloaded success [{config_parser['General']['output']}]"
    )



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