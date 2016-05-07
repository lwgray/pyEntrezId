from PyEntrezId.Conversion import Conversion
import unittest


class TddinConversion(unittest.TestCase):
    ''' Define tests '''
    def test_email(self):
        ''' Test email address syntax '''
        email = 'lwgray.com'
        self.assertRaises(ValueError, Conversion, email)
    
    def test_ensembl_to_entrez(self):
        geneid = 'ENST00000407559'
        transcriptid = Conversion('lwgray@gmail.com')
        entrezid = transcriptid.convert_ensemble_to_entrez(geneid)
        assert entrezid == 'b'
    
    def test_conversion_object(self):
        conversion_object = Conversion('lwgray@gmail.com')
        assert isinstance(conversion_object, class)
