class CompareError(BaseException):
    pass

class KeySorter:
    keysortlist = ['caps', 'alt', 'ctrl', 'shift', 'a', 'b', 'c', 'd', 'e', 'f', 'x']
    keysortmap = {x: i for i, x in enumerate(keysortlist)}

    def compare(self, o1, o2):
        if o2 not in self.keysortmap:
            raise CompareError('this not im compare list:' + o2)
        if o1 not in self.keysortmap:
            raise CompareError('this not im compare list:' + o1)

        return self.keysortmap[o1] - self.keysortmap[o2]
