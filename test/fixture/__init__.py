import pytest
from pathlib import Path
from semver.config import Config


FIXTURE = Path(__file__).parent


@pytest.fixture(scope='session')
def git_logs():
    with open(FIXTURE/'log', 'r') as f:
        return f.read()


@pytest.fixture(scope='session')
def semver_config():
    return Config.from_yaml(FIXTURE/'semver.yml')

