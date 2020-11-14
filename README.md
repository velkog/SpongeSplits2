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

## Things To Note:

Unfortunately for me, I needed to get this working for Windows which ended up being harder than one might've thought. To get all the different dependencies to work harmoniously, people recommeneded installing the [Unofficial Windows Binaries for Python](https://www.lfd.uci.edu/~gohlke/pythonlibs/)

In the end, I was able to get all Pip-installed packages to work for the project using Python 3.6.8. My recomendation would be to use 3.6, however 3.7 **might work.** If you end up running into a DLL runtime error (on Windows), then I'd suggest to try installing these binaries. I'm keeping some of these binaries here for potential future use, but you'll likely want to download them and install for yourself from the [source](https://www.lfd.uci.edu/~gohlke/pythonlibs/).


# Installation
* For production installs, use: `pip install .`
* For development also run, use: `pip install -e ".[dev]"`


[![Actions Status](https://github.com/{owner}/{repo}/workflows/{workflow_name}/badge.svg)](https://github.com/{owner}/{repo}/actions)
