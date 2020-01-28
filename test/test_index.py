from gitsemver.index import semver
from test.fixture import semver_config, git_logs


def test_semver(git_logs, semver_config):
    assert semver(git_logs, semver_config) == '0.19.0-feat-pypi-upload.5'
