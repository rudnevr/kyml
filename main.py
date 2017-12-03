class ConfigurationContructor:
    tab = '  '
    filePath = ''

    def resolveKeymap(self, mapName):
        return ""

    def findKey(self, c):
        res = c.lstrip().split(':')[0]
        if not res:
            raise Exception('error')
        return res

    def findVal(self, c):
        if len(c.lstrip().split(':')) > 1:
            return c.split(':')[1]
        return ""

    def __init__(self, tab, filePath):
        self.tab = tab
        self.filePath = filePath

    def indentLevel(self, c):
        return (len(c) - len(c.lstrip())) / len(self.tab)

    def createConfig(self):
        with open(self.filePath, 'r') as conf:
            content = conf.readlines()

        content = [x.rstrip("\n") for x in content if x.rstrip("\n")]

        currentKey = list()  # ["sh", "ctrl", "c"]

        previousVal = ""
        result = dict()

        for c in content:
            # if c.startswith('import:'):
            #     resolveKeymap(c.split(':')[1])
            # resolve and import keymaps
            print c
            k = self.findKey(c)  # shift
            indent_level = self.indentLevel(c)
            if len(currentKey) == indent_level and previousVal:
                raise NonLeafValue("Configuration Error:there shouldnt be a value in line preceding " + c)
            if len(currentKey) > indent_level and not previousVal:
                raise EmptyLeafValue(c)
            if len(currentKey) > indent_level and previousVal:
                result["".join(currentKey)] = previousVal
            currentKey = currentKey[:indent_level]
            currentKey.append(k)
            previousVal = self.findVal(c)

        if previousVal:
            result["".join(currentKey)] = previousVal
        else:
            raise EmptyLeafValue(c)

        return result


class ConfigurationError(BaseException):
    pass


class EmptyLeafValue(ConfigurationError):
    def __init__(self, value):
        print "Empty leaf value " + value


class NonLeafValue(ConfigurationError):
    def __init__(self, value):
        print "Node value is not leaf" + value
