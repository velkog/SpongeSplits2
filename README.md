<h1> <img src="res/SpongeSplits.png" alt="LiveSplit" height="45" width="45" align="top"/> SpongeSplits</h1>

[![GitHub](https://img.shields.io/github/license/velkog/SpongeSplits?color=brightgreen&label=License&logo=github&logoColor=white)](https://raw.githubusercontent.com/velkog/SpongeSplits2/master/LICENSE)
[![Linter](https://github.com/velkog/SpongeSplits2/workflows/Lint/badge.svg?color=brightgreen&label=License&logo=github&logoColor=white)](https://github.com/velkog/SpongeSplits2/actions)
[![Unit Tests](https://github.com/velkog/SpongeSplits2/workflows/Unit%20Tests/badge.svg?color=brightgreen&label=License&logo=github&logoColor=white)](https://github.com/velkog/SpongeSplits2/actions)

SpongeSplits is a video autosplitting tool for SpongeBob Squarepants: Battle for Bikini Bottom.

## Development Checklist:
- [ ] Add roadmap and features here
- [ ] Add unit/intergration tests
- [ ] Startup Flags (abseil)
- [ ] Fix codebase to pass super-linter
- [ ] Get codebase typed, and checks integrated with Github Actions
- [ ] Migrate configuration files to TOML (from YAML)

# Installation
* For production installs, use: `pip install .`
* For development also run, use: `pip install -e ".[dev]"`

# Development
* [Keras currently supports up to Python 3.6](https://github.com/keras-team/keras/issues/11690). Due to this limitation, this project is officially built and run on Windows Python 3.6.8. 
* Download Python 3.6.8 here: https://www.python.org/downloads/release/python-368/
* Unfortunately this project is intended for being run on Windows. If you're running into issues, you may find luck installing the [Unofficial Windows Binaries for Python](https://www.lfd.uci.edu/~gohlke/pythonlibs/).