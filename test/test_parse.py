from test.fixture import git_logs, semver_config
from semver.parse import LogParser
from semver.config import Config
import pytest


@pytest.fixture(scope='module')
def parser() -> LogParser:
    return LogParser(Config('jazz', 'feat', 'fix'))


def test_commit_match(parser: LogParser):
    assert parser.commit_match.match('\n\n    jazz-eater\n\n')
    assert not parser.commit_match.match('\n    feat(): I win\n\n')
    assert parser.commit_match.match('\n\n    fix(): yalalala\n\n')


def test_parse_commits(parser: LogParser, git_logs):
    commits = parser.parse_commits(git_logs)
    assert commits
    for c in commits:
        assert c in {2, 1}

