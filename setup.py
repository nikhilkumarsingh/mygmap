from setuptools import setup

# specify requirements of your package here
REQUIREMENTS = ['requests']

# some more details
CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Internet',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    ]

# calling the setup function 
setup(name='mygmap',
      version='1.0.0',
      description='A small wrapper around google maps api',
      url='https://github.com/nikhilkumarsingh/mygmap',
      author='Nikhil Kumar Singh',
      author_email='nikhilksingh97@gmail.com',
      license='MIT',
      packages=['geo'],
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='maps location address'
      )
