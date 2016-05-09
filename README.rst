PyEntrezId
==========

    Python package to convert between various gene or protein IDs

.. image:: https://travis-ci.org/lwgray/pyEntrezId.svg?branch=master
   :target: https://travis-ci.org/lwgray/pyEntrezId
.. image:: https://coveralls.io/repos/github/lwgray/pyEntrezId/badge.svg?branch=master
   :target: https://coveralls.io/github/lwgray/pyEntrezId?branch=master    
.. image:: https://img.shields.io/pypi/v/pyEntrezId.svg
   :target: https://pypi.python.org/pypi/pyEntrezId
.. image:: https://img.shields.io/pypi/pyversions/PyEntrezId.svg
   :target: https://pypi.python.org/pypi/PyEntrezId
.. image:: https://img.shields.io/badge/license-MIT-blue.svg
   :target: https://raw.githubusercontent.com/lwgray/lwgray/pyEntrezId/master/LICENSE


Summary
-------

This is the first package I am releasing into the wild. Any feedback would be greatly appreciated!

I created this package because there is a lack of a simple developer tool to convert between the numerous IDs used to identify genes, proteins, etc.  This is important because databases hosted by various scientific institutions (NIH, EMBL, etc) sometimes have different nomenclature to describe the same exact thing(gene, protein, dna, rna, etc).

I think this project is unique because it provides open access to the conversion code and has a singular goal.

Quick Start
-----------

::

    $ pip install --upgrade pyEntrezId

Examples
--------

Convert Ensemble Transcript Gene Id to Entrez Gene Id
-----------------------------------------------------

.. code:: python

    from PyEntrezId import Conversion
    
    EnsemblId = 'ENST00000407559'
    # include your email address
    Id = Conversion('dummyemail@dummybunny.info')
    EntrezId = Id.convert_ensembl_to_entrez(EnsemblId)
    # Returns a string 
    print(EntrezId)


Convert HGNC ID to Entrez Gene Id
---------------------------------

.. code:: python

    from PyEntrezId import Conversion
    
    # HGNCID can be just the number or 'HGNC:9425'
    HGNCID = 9245
    # include your email address
    Id = Conversion('dummyemail@dummybunny.info')
    EntrezId = Id.convert_hgnc_to_entrez(HGNCID)
    # Returns a dictionary containing Symbol and Entrez Id
    print EntrezID


Convert Entrez Gene Id to Uniprot ID
------------------------------------

.. code:: python

    from PyEntrezId import Conversion
    
    EntrezID = 39
    # include your email address
    Id = Conversion('dummyemail@dummybunny.info')
    UniProtId = Id.convert_entrez_to_uniprot(EntrezID)
    # Returns a string
    print UniProtId


Convert Uniprot Id to Entrez Gene Id
------------------------------------

.. code:: python

    from PyEntrezId import Conversion
    
    UniProtId = 'Q9BWD1'
    # include your email address
    Id = Conversion('dummyemail@dummybunny.info')
    EntrezID = Id.convert_uniprot_to_entrez(UniProtId)
    # Returns a string
    print EntrezID


Convert Accession Id to Taxonomy Id
-----------------------------------

.. code:: python

    from PyEntrezId import Conversion
    
    AccessionId = 'AC131209'
    # include your email address
    Id = Conversion('dummyemail@dummybunny.info')
    TaxID = Id.convert_accesion_to_taxid(AccesionId)
    # Returns a string
    print TaxID

Contributing
------------

Contributions to this library are always welcome and highly encouraged.

See `CONTRIBUTING`_ for more information on how to get started.

.. _CONTRIBUTING: https://github.com/GoogleCloudPlatform/gcloud-python/blob/master/CONTRIBUTING.rst

License
-------

The MIT License (MIT) - See `LICENSE`_ for more information.

.. _LICENSE: https://github.com/lwgray/PyEntrezID/blob/master/LICENSE
