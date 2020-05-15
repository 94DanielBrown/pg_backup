import pytest
import subprocess

from pgbackup import pgdump

url = "postgres://postgres:docker@localhost:5432/movies"


def test_dump_calls_pg_dump(mocker):
    """
    Utilize pg_dump with database URL
    """
    mocker.patch('subprocess.Popen')
    assert pgdump.dump(url)
    subprocess.Popen.assert_called_with(['pg_dump', url], stdout=subprocess.PIPE)


def test_dump_handles_oserror(mocker):
    """
    pgdump.dump returns reponse if pg_dump isn't installed
    """
    mocker.patch('subprocess.Popen', side_effect=OSError('No such file'))
    with pytest.raises(SystemExit):
        assert pgdump.dump(url)
        subprocess.Popen.assert_called_with(['pg_dump', url], stdout=subprocess.PIPE)




