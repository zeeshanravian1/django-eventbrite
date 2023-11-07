# django-eventbrite

## Name

Eventbrite Events Manager

## Description

This project is build in [Django](https://www.djangoproject.com/) using [Python](https://www.python.org/) 3.11.6 with [Pyenv](https://realpython.com/intro-to-pyenv/) and [Poetry](https://python-poetry.org/) for dependency management. This project uses [SQLite](https://www.sqlite.org/index.html) database for storing data.

## Installing Dependencies

### [Pyenv](https://realpython.com/intro-to-pyenv/)

- This project uses Pyenv for python version management. You can follow this [tutorial](https://realpython.com/intro-to-pyenv/) to configure pyenv. Or you can follow below steps to configure pyenv.z

- Install pyenv build dependencies:

```bash
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl
```

- Using pyenv-installer:

```bash
curl https://pyenv.run | bash
```

- Load pyenv automatically by adding
the following to ~/.bashrc:

```bash
echo -e '\n\nexport PYENV_ROOT="$HOME/.pyenv"\ncommand -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"\neval "$(pyenv init -)"' >> ~/.bashrc
```

- Restart your shell so the path changes take effect:

```bash
exec "$SHELL" # Or just restart your terminal
```

- Verify that pyenv is installed properly by using this command:

```bash
pyenv --version
```

### [Python](https://www.python.org/)

To run project, you must have python 3.11.6 installed on your system.
If python 3.11.6 is not installed on your system, you can follow this [tutorial](https://realpython.com/intro-to-pyenv/) to install it on your system. Or you can follow below steps to install python 3.11.6 on your system.

- List all available python versions:

```bash
pyenv install --list
```

- List specific python versions:

```bash
pyenv install --list | grep " 3\.11"
```

- Install specific python version:

```bash
pyenv install -v 3.11.6
```

- List all installed python versions:

```bash
pyenv versions
```

- List specific installed python versions:

```bash
pyenv versions | grep " 3\.11"
```

- Change Global Python Version **(Optional)**:

```bash
pyenv global 3.11.6
```

- Change Local Python Version **(Optional)**:

```bash
pyenv local 3.11.6
```

- Verify that python is installed properly by using this command:

```bash
python --version
```

### [Poetry](https://python-poetry.org/)

- This project uses Poetry for dependency management. You can follow this [tutorial](https://python-poetry.org/docs/#installation) to install Poetry on your system. Or you can follow below steps to install Poetry on your system.

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Add poetry to path:

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
```

- Enable tab completion:

```bash
poetry completions bash >> ~/.bash_completion
```

- Restart your shell so the path changes take effect:

```bash
source ~/.bashrc
```

- Verify that poetry is installed properly by using this command:

```bash
poetry --version
```

- Update poetry version **(Optional)**:

```bash
poetry self update
```

- Create Virtual Environment:
Go to project directory and type following command in terminal.

```bash
poetry init
```

> **_NOTE:_** This command will ask you some questions, you can skip them by pressing enter key.

- Activate Virtual Environment:
To activate virtual environment type following command in terminal.

```bash
poetry shell
```

- Install Dependencies:
To install dependencies type following command in terminal.

```bash
poetry install
```

- Install Specific Dependency:
To install specific dependency type following command in terminal.

```bash
poetry add <dependency_name>
```

> **_NOTE:_** Replace **< dependency_name >** with your dependency name.

- Verify your environment dependencies by running:

```bash
poetry show
```

- Remove Dependency:
To remove dependency type following command in terminal.

```bash
poetry remove <dependency_name>
```

- Listing the environments associated with the project:
To show all virtual environments type following command in terminal.

```bash
poetry env list
```

- Remove Virtual Environment:
To remove virtual environment type following command in terminal.

```bash
poetry env remove <virtual_environment_name>
```

> **_NOTE:_** Replace **< virtual_environment_name >** with your virtual environment name.

- Update Dependencies:
To update dependencies type following command in terminal.

```bash
poetry update
```

- Deactivate Virtual Environment:
To deactivate virtual environment type following command in terminal.

```bash
exit
```

### Geospatial Libraries

On Debian/Ubuntu, you are advised to install the following packages which will install, directly or by dependency, the required geospatial libraries:

```bash
sudo apt-get install binutils libproj-dev gdal-bin
```

## Usage

- Activate Virtual Environment:
To activate virtual environment type following command in terminal.

```bash
poetry shell
```

- Run Django Server:
To run the Django server run this command

```bash
python manage.py runserver
```
