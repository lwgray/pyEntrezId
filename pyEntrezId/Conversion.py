import requests, sys, xmltodict

class Conversion(object):
    def __init__(self):
        pass

    def convert(self, ensembl):
        '''Convert Ensembl Id to Entrez Gene Id'''
        # Submit resquest to NCBI eutils/Gene database
        server = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=gene&term={0}".format(ensembl)
        r = requests.get(server, headers={ "Content-Type" : "text/xml"})
        if not r.ok:
            r.raise_for_status()
            sys.exit()
        # Process Request
        response = r.text
        info = xmltodict.parse(response)
        geneId = info['eSearchResult']['IdList']['Id']
        return geneId

