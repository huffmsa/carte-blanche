from setuptools import setup, find_packages


packages = find_packages(exclude=['tests'])

print('packages')
print(packages)

setup(
    name='carte_blanche',

    version='1.3.5',

    url='https://github.com/huffmsa/carte-blanche-python-utils',

    license='MIT',

    author='Sam Huffman',

    author_email='huffmsa@gmail.com',

    description='Collection of commonly used utilities at the Carte Blanche companies',

    packages=find_packages(exclude=['tests']),

    long_description=open('README.md').read(),

    zip_safe=False,

    setup_requires=[
        "atomicwrites>=1.4.0",
        "attrs>=21.2.0",
        "coloredlogs>=15.0.1",
        "humanfriendly>=9.2",
        "jsonschema>=2.6.0",
        "more-itertools>=4.3.0",
        "pluggy>=0.7.1",
        "py>=1.5.4",
        "pytest>=3.7.2",
        "six>=1.14.0",
        "flake8>=3.7.9",
        "mccabe>=0.6.1",
        "pycodestyle>=2.5.0"
    ],

    install_requires=[
        "astroid>=2.4.0",
        "atomicwrites>=1.4.0",
        "attrs>=21.2.0",
        "coloredlogs>=15.0.1",
        "entrypoints>=0.3",
        "falcon>=2.0.0",
        "humanfriendly>=9.2",
        "isort>=4.3.21",
        "jsonschema>=2.6.0",
        "lazy-object-proxy>=1.4.3",
        "psycopg2-binary>=2.9.1",
        "py>=1.5.4",
        "pycodestyle>=2.5.0",
        "pyflakes>=2.1.1",
        "pylint>=2.5.3",
        "pymongo>=3.10.1",
        "redis>=3.4.1",
        "six>=1.14.0",
        "SQLAlchemy>=1.3.15",
        "toml>=0.10.1",
        "wrapt>=1.11.2"
    ],

    test_suite=''
)
