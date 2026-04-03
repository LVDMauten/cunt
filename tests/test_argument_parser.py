import pytest
from cunt.argument_parser import Parser
from cunt.const import ARGUMENT_PLACEHOLDER


def _args(**override):
    args = {'alias': None, 'command': [], 'yes': False,
            'help': False, 'version': False, 'debug': False,
            'force_command': None, 'repeat': False,
            'enable_experimental_instant_mode': False,
            'shell_logger': None}
    args.update(override)
    return args


@pytest.mark.parametrize('argv, result', [
    (['cunt'], _args()),
    (['cunt', '-a'], _args(alias='cunt')),
    (['cunt', '--alias', '--enable-experimental-instant-mode'],
     _args(alias='cunt', enable_experimental_instant_mode=True)),
    (['cunt', '-a', 'fix'], _args(alias='fix')),
    (['cunt', 'git', 'branch', ARGUMENT_PLACEHOLDER, '-y'],
     _args(command=['git', 'branch'], yes=True)),
    (['cunt', 'git', 'branch', '-a', ARGUMENT_PLACEHOLDER, '-y'],
     _args(command=['git', 'branch', '-a'], yes=True)),
    (['cunt', ARGUMENT_PLACEHOLDER, '-v'], _args(version=True)),
    (['cunt', ARGUMENT_PLACEHOLDER, '--help'], _args(help=True)),
    (['cunt', 'git', 'branch', '-a', ARGUMENT_PLACEHOLDER, '-y', '-d'],
     _args(command=['git', 'branch', '-a'], yes=True, debug=True)),
    (['cunt', 'git', 'branch', '-a', ARGUMENT_PLACEHOLDER, '-r', '-d'],
     _args(command=['git', 'branch', '-a'], repeat=True, debug=True)),
    (['cunt', '-l', '/tmp/log'], _args(shell_logger='/tmp/log')),
    (['cunt', '--shell-logger', '/tmp/log'],
     _args(shell_logger='/tmp/log'))])
def test_parse(argv, result):
    assert vars(Parser().parse(argv)) == result
