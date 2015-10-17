from pyEntrezId import Conversion

geneid = 'ENST00000407559'
transcriptid = Conversion()
entrezid = transcriptid.convert(geneid)

print "Ensembl Gene Transcript Id:  {0}".format(geneid)
print "Entrez Gene Id: {0}".format(entrezid)
