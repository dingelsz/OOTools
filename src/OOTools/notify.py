from collections import defaultdict
import warnings

def notify(cls):
    class Wrapper():
        def __init__(self, *args):
            self.__dict__['_notify'] = defaultdict(list)
            self.__dict__['_wrapped'] = cls(*args)

        def __setattr__(self, attr, value):
            if attr in self._notify:
                for listener, context in self._notify[attr]:
                    info = {'new': value}
                    if attr in self._wrapped.__dict__:
                        info['old'] = self._wrapped.__dict__[attr]
                    listener._alert(self, attr, info, context)
            self._wrapped.__dict__[attr] = value

        def watch(self, object, attr, context):
            object._notify[attr].append((object, context))
            
        def _alert(self, obj, attr, info, context):
            if hasattr(self._wrapped, '_alert'):
                self._wrapped._alert(obj, attr, info, context)
            else:
                raise NotImplementedError("_alert hasn't been implemented.")

    return Wrapper

class NotImplementedError(Exception):
    pass

