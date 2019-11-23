import re
import string


class CompareError(BaseException):
    pass


class KeySorter:
    keysortmap = {}
    keysortlist = []

    def __init__(self):

        self.keysortlist = ['caps', 'tab', 'alt', 'ctrl', 'shift', '\;']
        self.keysortlist.extend(list(string.letters))
        self.keysortlist.extend(['ifwinact', 'catchall'])
        self.keysortmap = {x: i for i, x in enumerate(self.keysortlist)}

    def compare(self, o1, o2):
        o1 = re.sub('\(.*\)', '', o1)
        o2 = re.sub('\(.*\)', '', o2)
        if o2 not in self.keysortmap:
            raise CompareError('this not im compare list:' + o2)
        if o1 not in self.keysortmap:
            raise CompareError('this not im compare list:' + o1)
        return self.keysortmap[o1] - self.keysortmap[o2]
