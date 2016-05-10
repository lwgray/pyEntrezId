# coding: utf-8
import json
def full_ensembl_report(ensembl):
    id = Conversion('lwgray@gmail.com')
    entrez = id.convert_ensembl_to_entrez(ensembl)
    uniprot = id.convert_entrez_to_uniprot(entrez)
    return json.dumps({'Ensembl':ensembl, 'Entrez':entrez, 'Uniprot': uniprot})
