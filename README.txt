# PyEntrezId
Converts Ensembl Transcript Gene ID to Entrez Gene Id

Example Code 1:
---------------------------------------------------------

from PyEntrezId import Conversion

EnsemblId = 'ENST00000407559'
Id = Conversion()
EntrezId = Id.convert_ensembl_to_entrez(EnsemblId)
print(EntrezId)
#########################################################
Example Code 2
---------------------------------------------------------

from PyEntrezId import Conversion

HGNCID = 9245  # hgncid ca be just the number or 'HGNC:9425'
Id = Conversion()
EntrezId = Id.convert_hgnc_to_entrez(HGNCID)
print EntrezID # Returns a dictionary containing Symbol and Entrez Id


