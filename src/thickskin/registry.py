__all__ =  ['CommandKey', 'CommandGroup', 'CommandPoolKey']


@classmethod
def _create_flyweight_instance_if_needed(cls, *args, **kargs):
    assert len(args) > 1
    name = intern(args[1])
    return cls.__instances.setdefault(name, super(type(cls), cls).__new__(*args, **kargs))

@classmethod
def _get_flyweights(cls):
    return cls.__instances.values()

@classmethod
def _get_flyweights_name(cls):
    return cls.__instances.keys()

@classmethod
def _clear_flyweights(cls):
    for flyweight in cls.all():
        if hasattr(flyweight, "clear") and callable(flyweight.clear):
            flyweight.clear()
    cls.__instances.clear()

def registry(decoree):
    decoree.__instances = dict()
    decoree.__new__ = _create_flyweight_instance_if_needed
    decoree.all = _get_flyweights
    decoree.names = _get_flyweights_name
    decoree.clear_all = _clear_flyweights
    return decoree


class Key(object):
    def __init__(self, name=None):
        assert name is not None
        assert isinstance(name, str)
        self.name = intern(name)

    def __repr__(self):
        return "<%s:'%s'>" % (self.__class__.__name__, self.name)


@registry
class CommandKey(Key): pass


@registry
class CommandPoolKey(Key): pass


@registry
class CommandGroup(Key): pass
