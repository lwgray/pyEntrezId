# PyEntrezId
Converts Ensembl Transcript Gene ID to Entrez Gene Id

Example Code:
---------------------------------------------------------

from PyEntrezId import Conversion

EnsemblId = 'ENST00000407559'
Id = Conversion()
EntrezId = Id.convert(EnsemblId)
print(EntrezId)

