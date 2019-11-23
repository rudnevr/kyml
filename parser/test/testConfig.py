import unittest

from parser.keysorters import *
from parser import \
    main


class testConfigCreator(unittest.TestCase):
    def test_fine(self):
        constructor = main.ConfigurationContructor('  ', 't.yml')
        result = constructor.createConfig()
        for key, value in result.iteritems():
            print key + ": " + value
        self.assertEqual(len(result.items()), 4)

    def test_tab(self):
        constructor = main.ConfigurationContructor('  ', 'tab.yml')
        result = constructor.createConfig()
        for key, value in result.iteritems():
            print key + ": " + value
        self.assertEqual(len(result.items()), 27)

    def test_emptyLeaf(self):
        constructor = main.ConfigurationContructor('  ', 'confError2.yml')
        with self.assertRaises(
                main.EmptyLeafValue):
            result = constructor.createConfig()

    def test_NonLeaf(self):
        constructor = main.ConfigurationContructor('  ', 'confError.yml')
        with self.assertRaises(
                main.NonLeafValue):
            result = constructor.createConfig()

    def test_indentlevel(self):
        c = main.ConfigurationContructor('  ', 'c.yml')
        assert c.indentLevel('    a') == 2
        assert c.indentLevel('  a') == 1
        assert c.indentLevel('a') == 0

    def test_compare(self):
        c = KeySorter()
        assert c.compare('ctrl', 'alt') > 0
        assert c.compare('ctrl', 'ctrl') == 0
        assert c.compare('alt', 'ctrl') < 0


if __name__ == '__main__':
    unittest.main()
