from test.fixture import FIXTURE
from gitsemver.config import Config


def test_from_yaml():
    c = Config.from_yaml(FIXTURE/'gitsemver.yml')
    assert c.major == 'BREAKING CHANGE:'
    assert c.minor == 'feat\s?(\([a-zA-Z0-9_.-]*\))?\s?:'
    assert c.patch == '(fix|chore|docs|style|refactor|test|ci|build|perf)\s?\([a-zA-Z0-9_.-]*\)?\s?:'
