from .index import semver
from .config import Config
from subprocess import run
from pathlib import Path


if __name__ == '__main__':
    logs = run(['git', 'log'], capture_output=True).stdout.decode()
    config = Config.from_yaml(Path.cwd()/'semver.yml')
    print(semver(logs, config))
