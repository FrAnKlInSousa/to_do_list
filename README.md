# Instalações globais

## Curl

```commandline
sudo snap install curl
```

## Pyenv
* Pré-requisito: Curl instalado


$ `https://pyenv.run | bash`

```commandline
nano .bashrc
```

* Cole a seguintes linhas no arquivo e salve:

```
# Load pyenv automatically by appending
# the following to 
# ~/.bash_profile if it exists, otherwise ~/.profile (for login shells)
# and ~/.bashrc (for interactive shells) :

export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init - bash)"
eval "$(pyenv virtualenv-init -)"
```
* Feche e abre o terminal novamente ou use o comando:
```commandline
source ~/.bashrc
```
# Instalando e setando versão do python com pyenv

$ `pyenv update`
$ `pyenv install -v 3.12.3`
$ `pyenv local 3.12.3`


## Observação

* Caso dê erro na instalação do python, instale as seguintes libs:

```commandline
sudo apt update
sudo apt install build-essential curl libbz2-dev libffi-dev liblzma-dev libncursesw5-dev libreadline-dev libsqlite3-dev libssl-dev libxml2-dev libxmlsec1-dev llvm make tk-dev wget xz-utils zlib1g-dev
```
# Pipx

```commandline
pip install pipx
pipx ensurepath
```

# Poetry

* Após rodar o seguinte comando, reabra o terminal.
```commandline
pipx install poetry
```
$ `poetry new {project_name}`


## Gerenciando múltiplas versões do python com pyenv

* Pré-requisito: Pyenv instalado.
* Instalando uma versão específica do python
```commandline
pyenv update
pyenv install 3.12:latest
```

## Criando o ambiente virtual

$ `poetry shell` (ativa o ambiente virtual)

Se o camando acima não der certo, use o passo a passo abaixo:

Exibe o comando para ativar o ambiente virtual
```commandline
poetry env activate
```
Para ativar, você pode digitar o comando printado pelo comando logo acima ou então pode usar em conjunto com o comando eval para já ativá-lo:

$ `eval $(poetry env activate)`

* O comando a seguir precisa ser executado na pasta onde contém o arquivo pyproject.toml

```commandline
poetry install
```

## Configurando o pycharm

# Configurando interpretador (Pycharm)
* Settings > Python interpreter > Add Interpreter > 
Add Local Interpreter... > Poetry Environment > 
Existing environment > options (...)
* Selecione o arquivo no `.cache/pypoetry/virtualenvs/{virtual_env_name}/bin/python3.12`
* Dê ok nas janelas abertas.

```
Add new interpreter... > Add local interpreter
Type: Poetry
Base python: ~/.pyenv/versions/3.12.9/bin/python
Path to poetry: {YOUR_HOME}/.local/bin/poetry
```

## Instalando ruff, taskipy, pytest, factory-boy
```commandline
poetry add --group dev ruff
```
```commandline
poetry add --group dev pytest pytest-cov factory-boy freezegun
```
```commandline
poetry add --group dev taskipy
```

# SQLAlchemy

```commandline
poetry add sqlalchemy
```
# Extensão do pydantic

```commandline
poetry add pydantic-settings
```

# Alembic

```commandline
poetry add alembic
```
Criando a tabela users

$ `alembic revision --autogenerate -m "{message}"`

Aplicando a migração no banco:
$ `alembic upgrade head`
### Fonte

# PWD

```commandline
poetry add pwdlib[argon2]
```

```commandline
poetry add python-multipart
```

```commandline
poetry add pyjwt
```


* [Managing Multiple Python Versions With pyenv](https://realpython.com/intro-to-pyenv/)
