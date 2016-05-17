'''Setup file'''
# import os
from distutils.core import setup

# HERE = os.path.abspath(os.path.dirname(__file__))

# with open(os.path.join(HERE, 'README.rst')) as f:
#     README = f.read()


REQUIREMENTS = [
    'colorama==0.3.7',
    'nose==1.3.7',
    'Pygments==2.1.3',
    'python-termstyle==0.1.10',
    'rednose==1.1.1',
    'requests==2.10.0',
    'xmltodict==0.10.1',
    ]

setup(
    name='PyEntrezId',
    packages=['PyEntrezId'],
    version='1.5.8.2',
    description='Converts UniProt, HGNC, and Ensembl Transcript Ids to \
        Entrez Gene Id. Also, converts accession number to Taxonomy id',
    author='Larry Gray',
    author_email='lwgray@gmail.com',
    scripts=[],
    url='https://github.com/lwgray/pyEntrezId',
    download_url='https://github.com/lwgray/pyEntrezId/tarball/1.5.8.2',
    keywords=['Ensembl', 'Entrez', 'Gene', 'HGNC', 'UniProt', 'Taxid',
              'Accession', 'Taxonomy', 'Accesion Number', 'NCBI', 'NLM',
              'DNA', 'Convert', 'Genomics', 'Biology'],
    install_requires=REQUIREMENTS,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python',
        'Intended Audience :: Science/Research',
        'Topic :: Utilities',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ]
)
