==========
PyEntrezId
==========


Example Code 1
--------------
Converts Ensemble Transcript Gene Id to Entrez Gene Id ::
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    from PyEntrezId import Conversion

    EnsemblId = 'ENST00000407559'
    Id = Conversion('sampleemail@nih.gov') #include your email address
    EntrezId = Id.convert_ensembl_to_entrez(EnsemblId)
    print(EntrezId)  # Returns a String


Example Code 2
--------------
Converts HGNC ID to Entrez Gene Id ::
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    from PyEntrezId import Conversion

    HGNCID = 9245  # hgncid ca be just the number or 'HGNC:9425'
    Id = Conversion('sampleemail@nih.gov') #include your email address
    EntrezId = Id.convert_hgnc_to_entrez(HGNCID)
    print EntrezID  # Returns a dictionary containing Symbol and Entrez Id


Example Code 3
--------------
Converts Entrez Gene Id to Uniprot ID ::
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    from PyEntrezId import Conversion

    EntrezID = 39
    Id = Conversion('sampleemail@nih.gov') #include your email address
    UniProtId = Id.convert_entrez_to_uniprot(EntrezID)
    print UniProtId  # Returns a string


Example Code 4
--------------
Converts Uniprot Id to Entrez Gene Id ::
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    from PyEntrezId import Conversion

    UniProtId = 'Q9BWD1'
    Id = Conversion('sampleemail@nih.gov') #include your email address
    EntrezID = Id.convert_uniprot_to_entrez(UniProtId)
    print EntrezID # Returns a string

