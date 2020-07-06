import json
import selenium.webdriver
import pytest
import os

@pytest.fixture(scope = 'session')
def config():
    cwd=os.getcwd()
    files = os.listdir(cwd)
    print("Files in %r: %s" % (cwd, files))
    with open('config.json') as config_file:
        config = json.load(config_file)

    assert config['browser'] in ['Firefox', 'Chrome']

    return config

@pytest.fixture()
def browser(config):
    if config['browser']=='Firefox':
        brows = selenium.webdriver.Firefox()
    elif config['browser']=='Chrome':
        brows = selenium.webdriver.Chrome()
    else:
        raise Exception(f'Browser "{config["browser"]}" is not supported')

    brows.get(config["baseurl"])
    brows.maximize_window()

    yield brows
    brows.quit()