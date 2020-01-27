from .index import semver
from subprocess import Popen


if __name__ == '__main__':
    Popen(['git', 'log'])