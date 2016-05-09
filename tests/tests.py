import unittest
from PyEntrezId.Conversion import Conversion


ENSEMBL_ID = 'ENST00000407559'
FAKE_ENSEMBL_ID = 'ENTT11000'
EMAIL = 'pyentrez@nowherebutup.info'
FAKE_EMAIL = 'pyentrez.info'


class Config(object):
    """Run-time configuration to be modified at set-up.

    This is a mutable stand-in to allow test set-up to modify
    global state.
    """

    BIO_ID = None


def setUpModule():
    Config.BIO_ID = Conversion(EMAIL)


class TddinConversion(unittest.TestCase):
    ''' Define tests '''
    def setUp(self):
        self.to_delete = []

    def tearDown(self):
        for doomed in self.to_delete:
            doomed.delete()

    def test_email(self):
        ''' Test email address syntax '''
        self.assertRaises(ValueError, Conversion, FAKE_EMAIL)

    def test_ensembl_to_entrez_return(self):
        entrezid = Config.BIO_ID.convert_ensembl_to_entrez(ENSEMBL_ID)
        self.assertEqual(entrezid, u'55112')

    def test_ensembl_to_entrez_param(self):
        self.assertRaises(
            IndexError,
            Config.BIO_ID.convert_ensembl_to_entrez,
            FAKE_ENSEMBL_ID)
