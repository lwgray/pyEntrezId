from distutils.core import setup
setup(
    name = 'PyEntrezId',
    packages = ['PyEntrezId'],
    version = '1.5.0',
    description = 'Converts UniProt, HGNC, and Ensembl Transcript Ids to Entrez Gene Id. Also, converts accession number to Taxonomy id',
    author = 'Larry Gray',
    author_email = 'lwgray@gmail.com',
    url = 'https://github.com/lwgray/pyEntrezId',
    download_url = 'https://github.com/lwgray/pyEntrezId/tarball/1.5.0',
    keywords = ['Ensembl', 'Entrez', 'Gene', 'HGNC', 'UniProt', 'Taxid', 'Accession', 'Taxonomy', 'Accesion Number', 'NCBI', 'NLM', 'DNA'],
    classifiers = [],
    install_requires = ['xmltodict>=0.9.2', 'requests>=2.8.1'],
)
