# tests/test_pydig.py

from pydig import __version__, __app_name__, cli
from typer.testing import CliRunner
from pydig import data, pydig

run = CliRunner()
connect = data.NetworkConnection()

class TestCommands :
    @staticmethod
    def test_version() -> None :
        results = run.invoke(cli.app, ["--version"])
        assert results.exit_code == 0
        assert results.stdout.strip() == f"{__app_name__} v{__version__}"

class TestNetworkConnection :
    @staticmethod
    def test_is_connect() -> None :
        assert connect.is_connected() == 0

class TestYoutube : ...



