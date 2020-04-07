from setuptools import setup, find_packages


packages = find_packages(exclude=['tests'])

print('packages')
print(packages)

setup(
    name='carte_blanche_utils',

    version='1.2.1',

    url='https://github.com/huffmsa/carte-blanche-python-utils',

    license='MIT',

    author='Sam Huffman',

    author_email='huffmsa@gmail.com',

    description='Collection of commonly used utilities at the Carte Blanche companies',

    packages=find_packages(exclude=['tests']),

    long_description=open('README.md').read(),

    zip_safe=False,

    setup_requires=[
        "atomicwrites==1.1.5",
        "attrs==18.1.0",
        "coloredlogs==10.0",
        "humanfriendly==4.16.1",
        "jsonschema==2.6.0",
        "more-itertools==4.3.0",
        "pluggy==0.7.1",
        "py==1.5.4",
        "pytest==3.7.2",
        "six==1.11.0"
    ],

    install_requires=[
        "astroid==2.3.3",
        "atomicwrites==1.1.5",
        "attrs==18.1.0",
        "coloredlogs==10.0",
        "entrypoints==0.3",
        "humanfriendly==4.16.1",
        "isort==4.3.21",
        "jsonschema==2.6.0",
        "lazy-object-proxy==1.4.3",
        "more-itertools==4.3.0",
        "pluggy==0.7.1",
        "psycopg2==2.8.4",
        "psycopg2-binary==2.8.4",
        "py==1.5.4",
        "redis==3.4.1",
        "six==1.14.0",
        "SQLAlchemy==1.3.15",
        "wrapt==1.11.2",
        "pymongo==3.10.1",
        "falcon==2.0.0"
    ],

    test_suite=''
)
