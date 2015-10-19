from distutils.core import setup
setup(
    name = 'PyEntrezId',
    packages = ['PyEntrezId'],
    version = '1.4.1',
    description = 'Converts Entrez Gene Id to UniProt, HGNC ID to Entrez Gene Id, Ensembl gene Transcript Id to Entrez Gene Id',
    author = 'Larry Gray',
    author_email = 'lwgray@gmail.com',
    url = 'https://github.com/lwgray/pyEntrezId',
    download_url = 'https://github.com/lwgray/pyEntrezId/tarball/1.4.1',
    keywords = ['Ensembl', 'Entrez', 'Gene', 'HGNC', 'UniProt'],
    classifiers = [],
    install_requires=['xmltodict>=0.9.2', 'requests>=2.8.1']
)
