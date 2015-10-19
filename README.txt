# PyEntrezId
Converts Ensembl Transcript Gene ID to Entrez Gene Id

Example Code 1:
---------------------------------------------------------

from PyEntrezId import Conversion

EnsemblId = 'ENST00000407559'
Id = Conversion()
EntrezId = Id.convert_ensembl_to_entrez(EnsemblId)
print(EntrezId)  # Returns a String
#########################################################

Example Code 2
---------------------------------------------------------

from PyEntrezId import Conversion

HGNCID = 9245  # hgncid ca be just the number or 'HGNC:9425'
Id = Conversion()
EntrezId = Id.convert_hgnc_to_entrez(HGNCID)
print EntrezID  # Returns a dictionary containing Symbol and Entrez Id
#########################################################

Example Code 3
---------------------------------------------------------

from PyEntrezId import Conversion

EntrezID = 39
Id = Conversion()
UniProtId = Id.convert_entrez_to_uniprot(EntrezID)
print UniProtId  # Returns a string
#########################################################

Example Code 4
---------------------------------------------------------

from PyEntrezId import Conversion

UniProtId = 'Q9BWD1'
Id = Conversion()
EntrezID = Id.convert_uniprot_to_entrez(UniProtId)
pritn EntrezID # Returns a string
########################################################

