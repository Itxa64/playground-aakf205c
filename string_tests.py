import unittest


class StringTests(unittest.TestCase):
    def test_to_upper(self):
        import uppercase
        self.assertEqual(uppercase.to_upper('foo'), 'FOO', "Wrong uppercase value for foo")
        self.assertEqual(uppercase.to_upper('Bar'), 'BAR')
