#!/usr/bin/python
import requests
import sys
import xmltodict
try:
    from urllib import urlencode
except:
    from urllib.parse import urlencode


class Conversion(object):
    def __init__(self, email):
        '''Must Include Email'''
        self.params = {}
        self.params['tool']='PyEntrez'
        self.email = email
        self.params["email"] = self.email
        self.options = urlencode(self.params, doseq=True) 
        return

    def convert_ensembl_to_entrez(self, ensembl):
        '''Convert Ensembl Id to Entrez Gene Id'''
        # Submit resquest to NCBI eutils/Gene database
        server = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + self.options + "&db=gene&term={0}".format(ensembl)
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
            r.raise_for_status()
            sys.exit()
        response = r.text
        info = xmltodict.parse(response)
        for data in info['response']['result']['doc']['str']:
            if data['@name'] == 'entrez_id':
                entrezdict[data['@name']] = data['#text']
            if data['@name'] == 'symbol':
                entrezdict[data['@name']] = data['#text']
        return entrezdict

    def convert_entrez_to_uniprot(self, entrez):
        '''Convert Entrez Id to Uniprot Id'''
        server = "http://www.uniprot.org/uniprot/?query=%22GENEID+{0}%22&format=xml".format(entrez)
        r = requests.get(server, headers={ "Content-Type" : "text/xml"})
        if not r.ok:
            r.raise_for_status()
            sys.exit()
        response = r.text
        info = xmltodict.parse(response)
        try:
            data = info['uniprot']['entry']['accession'][0]
            return data
        except TypeError:
            data = info['uniprot']['entry'][0]['accession'][0]
            return data

    def convert_uniprot_to_entrez(self, uniprot):
        '''Convert Uniprot Id to Entrez Id'''
        #Submit request to NCBI eutils/Gene Database
        server = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?" + self.options + "&db=gene&term={0}".format(uniprot)
        r = requests.get(server, headers={ "Content-Type" : "text/xml"})
        if not r.ok:
            r.raise_for_status()
            sys.exit()
        # Process Request
        response = r.text
        info = xmltodict.parse(response)
        geneId = info['eSearchResult']['IdList']['Id']
        # check to see if more than one result is returned
        # if you have more than more result then check which Entrez Id returns the same uniprot Id entered.
        if len(geneId) > 1:
            for x in geneId:
                c = self.convert_entrez_to_uniprot(x)
                c = c.lower()
                u = uniprot.lower()
                if c==u:
                    return x
        else:
            return geneId

    def convert_accession_to_taxid(self, accessionid):
        '''Convert Accession Id to Tax Id '''
        # Submit request to NCBI eutils/Taxonomy Database
        server = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?" + self.options + "&db=gene&id={0}&retmode=xml".format(accessionid)
        r = requests.get(server, headers={ "Content-Type" : "text/xml"})
        if not r.ok:
            r.raise_for_status()
            sys.exit()
        # Process Request
        response = r.text
        records = xmltodict.parse(response)
        taxid = records['Entrezgene-Set']['Entrezgene']['Entrezgene_source']['BioSource']['BioSource_org']['Org-ref']['Org-ref_db']['Dbtag']['Dbtag_tag']['Object-id']['Object-id_id']
        return taxid
