from thickskin.registry import *

def setup_function(function):
    CommandKey.clear_all()
    CommandGroup.clear_all()
    CommandPoolKey.clear_all()


def test_clear_all():
    assert CommandKey.names() == []
    CommandKey("test")
    assert CommandKey.names() == ["test"]
    CommandKey.clear_all()
    assert CommandKey.names() == []


def test_command_key():
    a = CommandKey("one")
    b = CommandKey("two")
    c = CommandKey("one")
    d = CommandPoolKey("one")

    assert set(CommandKey.names()) == set(["one", "two"])
    assert set(CommandKey.all()) == set([a, b])

    assert a is c
    assert a is not d
    assert a == c
    assert a is not b
    assert a != b

