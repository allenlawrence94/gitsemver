import pytest
from semver.version import Versioner


@pytest.fixture(scope='function')
def versioner():
    return Versioner()


def test_bump(versioner):
    versioner.bump(0)
    assert versioner.version[0] == 1
    versioner.bump(1)
    versioner.bump(1)
    versioner.bump(2)
    assert versioner.version[1] == 2
    assert versioner.version[2] == 1
    versioner.bump(0)
    assert versioner.version[0] == 2
    assert versioner.version[1] == 0
    assert versioner.version[2] == 0
