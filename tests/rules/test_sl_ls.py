
from cunt.rules.sl_ls import match, get_new_command
from cunt.types import Command


def test_match():
    assert match(Command('sl', ''))
    assert not match(Command('ls', ''))


def test_get_new_command():
    assert get_new_command(Command('sl', '')) == 'ls'
