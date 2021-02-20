import unittest
import proxy
import iterator
import singleton


class TestCalc(unittest.TestCase):

    def test_proxy(self):
        result = proxy.am.words('parola123')
        self.assertIsNotNone(result)
        _result = proxy.am.words('')
        self.assertIsNone(_result)

    def test_iterator(self):
        result = iterator.count_to_max
        self.assertEqual(result, list(range(26)))

    def test_isupper(self):
        self.assertTrue(singleton.wrd.isupper())

    def test_singleton(self):
        self.assertTrue(singleton.the_word, singleton.the_word_2)


if __name__ == '__main__':
    unittest.main()
