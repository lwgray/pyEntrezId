import unittest

class TddinConversion(unittest.TestCase):
    ''' Define tests '''
    def test_email(self):
        ''' Test email address syntax '''
        from PyEntrezId.Conversion import Conversion
        email = 'lwgray.com'
        self.assertRaises(ValueError, Conversion, email)
