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
    Id = Conversion('sampleemail@nih.gov') #include your email address
    EntrezId = Id.convert_ensembl_to_entrez(EnsemblId)
    print(EntrezId)  # Returns a String


Convert HGNC ID to Entrez Gene Id
---------------------------------

.. code:: python
    from PyEntrezId import Conversion

    HGNCID = 9245  # HGNCID can be just the number or 'HGNC:9425'
    Id = Conversion('sampleemail@nih.gov') # include your email address
    EntrezId = Id.convert_hgnc_to_entrez(HGNCID)
    print EntrezID  # Returns a dictionary containing Symbol and Entrez Id


Convert Entrez Gene Id to Uniprot ID
------------------------------------

.. code:: python
    from PyEntrezId import Conversion

    EntrezID = 39
    Id = Conversion('sampleemail@nih.gov') #include your email address
    UniProtId = Id.convert_entrez_to_uniprot(EntrezID)
    print UniProtId  # Returns a string


Convert Uniprot Id to Entrez Gene Id
------------------------------------

.. code:: python
    from PyEntrezId import Conversion

    UniProtId = 'Q9BWD1'
    Id = Conversion('sampleemail@nih.gov') #include your email address
    EntrezID = Id.convert_uniprot_to_entrez(UniProtId)
    print EntrezID # Returns a string


Convert Accession Id to Taxonomy Id
-----------------------------------

.. code:: python
    from PyEntrezId import Conversion

    AccessionId = 'AC131209'
    Id = Conversion('sampleemail@nih.gov') #include your email address
    TaxID = Id.convert_accesion_to_taxid(AccesionId)
    print TaxID # Returns a string

Contributing
------------

Contributions to this library are always welcome and highly encouraged.

See 'CONTRIBUTING'_ for more information on how to get started.

.. _CONTRIBUTING: https://github.com/lwgray/PyEntrezId/blob/master/CONTRIBUTING.rst

License
-------

The MIT License (MIT)

.. _LICENSE: https://github.com/lwgray/PyEntrezID/blob/master/LICENSE