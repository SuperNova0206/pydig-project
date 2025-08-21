# pydig/cli.py

from pydig import (
    __version__,
    __app_name__,
    data,
    forms,
    pydig,
    qualities,
    config
)
from pydig import exceptions
from typing import Optional
import typer
from pathlib import Path

app = typer.Typer(help="pydig CLI media downloader")

def _version_fun(respond : bool) -> None :
    if respond :
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

# setup
@app.command(help="initializing pydig CLI app")
def setup(
    output : Path = typer.Option(
        data.DEFAULT_OUTPUT_LOCATION,
        "--output",
        "-o",
        help="specify downloading folder"
    )
) -> None:
    _data_error = data._create_app_output_location(otdata=output)
    if _data_error :
        typer.secho(
            f":) well done!",
            fg = typer.colors.GREEN
        )
        raise typer.Exit()
    raise exceptions.SetupError(":( application setup failed!")

# download
@app.command(help="download data from youtube platform")
def youtube(

    # youtube video url
    url : str,

    # form mp3 | mp4
    mimetype : forms.YoutubeForms = typer.Option(
        forms.YoutubeForms.MP4,
        "--form",
        "-f",
        help="available forms (MP3 | MP4)"
    ),

    # video quality [144, 240, 360, 480, 720, 1080]
    resolution : Optional[qualities.YoutubeQuality] = typer.Option(
        None,
        "--quality",
        "-q",
        help="available qualities"
    )
) -> None :
    connection = data.NetworkConnection()
    connection.is_connected()
    youtubeProcess = pydig.YouTubeContoller(url=url, resolution=360 if resolution == None else resolution)
    if mimetype == "mp3" :
        msg : list = youtubeProcess.audio()
        typer.secho(
            f":) {msg[0]} downloaded successfully\n>>> \"{msg[1]}\"",
            fg = typer.colors.GREEN
        )
        raise typer.Exit()
    msg : list = youtubeProcess.video()
    typer.secho(
        f":) \"{msg[0]}.mp4\" downloaded successfully\n>>> \"{msg[1]}\"",
        fg = typer.colors.GREEN
    )
    raise typer.Exit()


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