from collections import defaultdict
import warnings


class Notify():
    def __init__(self):
        self.__dict__['_notify'] = defaultdict(list)

    def __setattr__(self, attr, value):
        if attr in self._notify:
            for listener, context in self._notify[attr]:
                info = {'new': value}
                if attr in self.__dict__:
                    info['old'] = self.__dict__[attr]
                listener._alert(self, attr, info, context)
        self.__dict__[attr] = value

    def watch(self, object, attr, context):
        object._notify[attr].append((object, context))
            
    def _alert(self, obj, attr, info, context):
        warnings.warn("_alert has not been overwritten.")

