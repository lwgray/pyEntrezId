import unittest
from PyEntrezId.Conversion import Conversion


ENSEMBL_ID = 'ENST00000407559'
FAKE_ENSEMBL_ID_ONE = 'ENTT11000'
FAKE_ENSEMBL_ID_TWO = 'ENST11000'
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

    def test_ensembl_to_entrez(self):
        ''' Test Emseml to Entrez Function '''
        # Output of Ensembl to Entrez returns Correct Value
        self.assertEqual(
            Config.BIO_ID.convert_ensembl_to_entrez(ENSEMBL_ID), u'55112')
        # Test malformed Ensembl ID without 'ENST' Tag in ID
        self.assertRaises(
            IndexError,
            Config.BIO_ID.convert_ensembl_to_entrez,
            FAKE_ENSEMBL_ID_ONE)
        # Test malformed Ensembl ID with 'ENST' but remaining seq is incorrect
        self.assertRaises(
            TypeError,
            Config.BIO_ID.convert_ensembl_to_entrez,
            FAKE_ENSEMBL_ID_TWO)
