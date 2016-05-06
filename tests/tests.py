from PyEntrezId.Conversion import Conversion
import unittest


class TddinConversion(unittest.TestCase):
    ''' Define tests '''
    def test_email(self):
        ''' Test email address syntax '''
        email = 'lwgray.com'
        self.assertRaises(ValueError, Conversion, email)


