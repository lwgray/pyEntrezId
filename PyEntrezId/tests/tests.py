from .. Conversion import Conversion
import unittest


class TddinConversion(unittest.TestCase):
    ''' Define tests '''
    def test_b(self):
        self.assertEqual('b', 'b')

    def test_email(self):
        ''' Test that email raises error when not correct '''
        email = 'lwgray.com'
        self.assertRaises(ValueError, Conversion, email)


# re.compile(r"[^@]+@[^@]+\.[^@]+")
