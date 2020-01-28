# gitsemver

Super simple command line tool for generating a semantic version from git logs.

I made this because GitVersion has annoying environment requirements, and semantic-release does too much. Lmk if you
know of better alternatives.

## Usage
Add a `gitsemver.yml` file to your project directory, here's an example:
```yaml
major: 'api\('
minor: 'feat\('
patch: '(fix|chore|docs|style|refactor|test|ci|build|perf)\('
```
It maps major, minor, and patch version increments to git commits via the corresponding regex, just like GitVersion.

And then run `gitsemver` from within you project directory.

I use it with poetry like so: `poetry version $(gitsemver)`
