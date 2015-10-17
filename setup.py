from distutils.core import setup
setup(
    name = 'PyEntrezId',
    packages = ['PyEntrezId'],
    version = '1.1',
    description = 'Converts Ensembl Transcript Gene Id to Entrez Gene Id',
    author = 'Larry Gray',
    author_email = 'lwgray@gmail.com',
    url = 'https://github.com/lwgray/pyEntrezId',
    download_url = 'https://github.com/lwgray/pyEntrezId/tarball/1.0',
    keywords = ['Ensembl', 'Entrez', 'Gene'],
    classifiers = [],
    install_requires=['xmltodict>=0.9.2', 'requests>=2.8.1']
)
