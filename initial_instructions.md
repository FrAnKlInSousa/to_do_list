# Instalação do pyenv

$ `curl https://pyenv.run | bash`
$ `nano ~/.bash`
* no final do arquivo adicione as seguintes linhas e salve as alterações:
  * export PATH="$HOME/.pyenv/bin:$PATH"
  * eval "$(pyenv init -)"
  * eval "$(pyenv virtualenv-init -)"

# Instalando e setando versão do python com pyenv

$ `pyenv update`
$ `pyenv install -v 3.12.3`
$ `pyenv local 3.12.3`


# Instalando o pipx

$ `pip install pipx`

# Instalando ignr para gerar .gitignore

$ `pipx install ignr` 
$ `ignr -p python > .gitignore`


# Instalando poetry e setando o projeto

$ `pipx install poetry`

$ `poetry new {project_name}`

# Criando e ativando o ambiente virtual

$ `poetry shell` (ativa o ambiente virtual)
$ `poetry install` (precisa ser executado na mesma pasta onde está o arquivo pyproject.toml)
$ `poetry add fastapi`

# Configurando interpretador (Pycharm)
* Settings > Python interpreter > Add Interpreter > 
Add Local Interpreter... > Poetry Environment > 
Existing environment > options (...)
* Selecione o arquivo no `.cache/pypoetry/virtualenvs/{virtual_env_name}/bin/python3.12`
* Dê ok nas janelas abertas.

>
# git

$ `git init .`
