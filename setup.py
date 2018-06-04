from setuptools import setup, find_packages
 
 
packages = find_packages(exclude=['tests'])

print('packages')
print(packages)

setup(name='skeleton_utils',
 
      version='0.1',
 
      url='https://github.com/the-skeleton-company/skeleton-python-utils',
 
      license='MIT',
 
      author='Sam Huffman',
 
      author_email='huffmsa@gmail.com',
 
      description='Collection of commonly used utilities at the skeleton company',
 
      packages=find_packages(exclude=['tests']),
 
      long_description=open('README.md').read(),
 
      zip_safe=False,
 
      setup_requires=[],
 
      test_suite='')