from PyEntrezId.Conversion import Conversion
import unittest


class TddinConversion(unittest.TestCase):
    ''' Define tests '''
    def _getTargetClass(self):
        from PyEntrezId.Conversion import Conversion
        return Conversion

    def test_email(self):
        ''' Test email address syntax '''
        email = 'lwgray.com'
        self.assertRaises(ValueError, Conversion, email)

    def test_conversion_object(self):
        conversion_object = Conversion('lwgray@gmail.com')
        assert isinstance(conversion_object, self._getTargetClass)
