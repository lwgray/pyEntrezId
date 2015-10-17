#!/usr/bin/python
import requests, sys, xmltodict

class Conversion(object):
    def __init__(self):
        pass 

    def convert_ensembl_to_entrez(self, ensembl):
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

    def convert_hgnc_to_entrez(self, hgnc):
        '''Convert HGNC Id to Entrez Gene Id'''
        entrezdict = {}
        server = "http://rest.genenames.org/fetch/hgnc_id/{0}".format(hgnc)
        r = requests.get(server, headers={ "Content-Type" : "application/json"})
        if not r.ok:
            r.raise_fo_status()
            sys.exit()
        response = r.text
        info = xmltodict.parse(response)
        for data in info['response']['result']['doc']['str']:
            if data['@name'] == 'entrez_id':
                entrezdict[data['@name']] = data['#text']
            if data['@name'] == 'symbol':
                entrezdict[data['@name']] = data['#text']
        
        return entrezdict
