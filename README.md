# Python4Nastja

## Environment setup

Before starting to work with Python configure your environment. Go to https://github.com/pyenv/pyenv/tree/v2.3.6 and follow the steps from https://github.com/pyenv/pyenv/tree/v2.3.6#basic-github-checkout or try their new https://github.com/pyenv/pyenv-installer . I helps to avoid bullshit version conflicts between different python versions in your machine.

After that, `pyenv install 3.11.0`, we can work with the latest python version. Select it globally `pyenv global 3.11.0` and check if it works. Then install the requirements

```
pip install -r requirements.txt
```

## Tests execution

Take a look inside `example_module` directory. It's my old example code for CERN robotics group, but it is fresh enough. Execute `pytest` from the project root or from example directory, Pytest will automatically detect test sources and execute them.
