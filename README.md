# Python4Nastja

## Environment setup

Before starting to work with Python configure your environment. Go to https://github.com/pyenv/pyenv/tree/v2.3.6 and follow the steps from https://github.com/pyenv/pyenv/tree/v2.3.6#basic-github-checkout or try their new https://github.com/pyenv/pyenv-installer . I helps to avoid version conflicts between different python versions in your machine.

After that, `pyenv install 3.11.0`, we can work with the latest python version. Select it globally `pyenv global 3.11.0` and check if it works. Then install the requirements

```
pip install -r requirements.txt
```

## Python package structure

In the internet there are countless tutorials on how to create and deploy your python package, so let's not repeat it here. The way I organized the code in this repo is just one of many possibilities, but let us start somewhere.

- ROOT
  - module1 (or like in recent python docs "subpackage")
    - source1.py (or like in recent python docs "module1.py")
    - source2.py
    - sourceN.py
  - module2
  - moduleN
  - documentation
  - tests (for the purpose of this presentation I decided to use flat test structure, but nothing prevents you from putting the test sources in the additional directories)

## Short sample main.py

Small `main.py` example is included in the package to show that we can easily import our components and use them in the production.

## Tests execution

Take a look inside `example_module` directory. It's my old example code for CERN robotics group, but it is fresh enough. Execute `pytest` from the project root or from example directory, Pytest will automatically detect test sources and execute them.

This will include all print outputs:
```
pytest -s
```

This will execute tests only from the selected subpackage and generate the coverage report for them
```
pytest --cov=robotic_arm_module --cov-report html tests/
```

## Run linter

Static code analysis tool `pylint` can be executed per file

```
pylint main.py
```

Or per module/subpackage

```
pylint example_module
```
