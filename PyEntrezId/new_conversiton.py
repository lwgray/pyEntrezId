#!/usr/bin/python
''' Tool to Convert IDs '''
import requests
import sys
import xmltodict
try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode


class Conversion(object):
    '''Convert between Id Types'''
    def __init__(self, email='unknown@unknown.com', idtype='Ensembl'):
        '''Must Include Email'''
        self.params = {'tool': 'PyEntrez', 'email': email}
        self.idtype = idtype

    def ensembl(self):
        ''' Use Ensembl '''
        return Ensembl(self.params)

    class Ensembl(object):
        '''Convert Ensembl Id'''
        # Submit resquest to NCBI eutils/Gene database
        def __init__(self, params, ids, database):
            self.options = None
            if not ids and not database:
                self.params = params
                self.params['term'] = 'ENST00000407559'
                self.params['db'] = 'gene'
            elif not ids:
                raise IOError
            else:
                self.params = params
                self.params['term'] = ids
                self.params['db'] = database
            self.options = urlencode(self.params, doseq=True)

        def to_entrez_gene_id(self, ensemblid):
            ''' Convert Ensembl gene id to Entrez Gene ID '''
            server = "http://eutils.ncbi.nlm.nih.gov/\
                      entrez/eutils/esearch.fcgi?"\
                     + self.options + "&db=gene&term={0}".format(ensemblid)
            req = requests.get(server, headers={"Content-Type": "text/xml"})
            if not req.ok:
                req.raise_for_status()
                sys.exit()
            # Process Request
            response = req.text
            info = xmltodict.parse(response)
            geneid = info['eSearchResult']['IdList']['Id']
            return geneid

        @staticmethod
        def to_gene_name(ensemblid):
            ''' Convert Ensembl ID to GENE NAME '''
            gene_name = ensemblid
            return gene_name


class Efetch(Conversion):
    ''' Grab data '''
    def __init__(self, database='protein', ids='', rettype='docsum',
                 retmode='json'):
        super(self.__class__, self).__init__()
        self.database = database
        self.ids = ids
        self.rettype = rettype
        self.retmode = retmode

    def fetch(self):
        ''' Grab info '''
        server = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?" \
                 + self.options + \
                 "&db={0}&id={1}&rettype={2}\
                 &retmode={3}".format(self.database, self.ids,
                                      self.rettype, self.retmode)
        req = requests.get(server,
                           headers={"Content-Type": "application/json"})
        if not req.ok:
            req.raise_for_status()
            sys.exit()
        # Process Request
        response = req.text
        info = xmltodict.parse(response)
        gene_id = info['eSearchResult']['IdList']['Id']
        return gene_id
