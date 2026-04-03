import pytest
from cunt.rules.workon_doesnt_exists import match, get_new_command
from cunt.types import Command


@pytest.fixture(autouse=True)
def envs(mocker):
    return mocker.patch(
        'cunt.rules.workon_doesnt_exists._get_all_environments',
        return_value=['cunt', 'code_view'])


@pytest.mark.parametrize('script', [
    'workon tehcunt', 'workon code-view', 'workon new-env'])
def test_match(script):
    assert match(Command(script, ''))


@pytest.mark.parametrize('script', [
    'workon cunt', 'workon code_view', 'work on tehcunt'])
def test_not_match(script):
    assert not match(Command(script, ''))


@pytest.mark.parametrize('script, result', [
    ('workon tehcunt', 'workon cunt'),
    ('workon code-view', 'workon code_view'),
    ('workon zzzz', 'mkvirtualenv zzzz')])
def test_get_new_command(script, result):
    assert get_new_command(Command(script, ''))[0] == result
