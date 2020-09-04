"""
Examples tests using standard documentation.
https://docs.python.org/3/library/unittest.html
"""


import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # Check that s.split fails when the seperator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_in(self):
        s = 'Lambda School Rocks!'
        self.assertTrue('L' in s)
        self.assertIn('L', s)

if __name__ == '__main__':
    unittest.main()
