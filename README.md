
mygmap
======

A simple python wrapper for Google Maps API.
Use it to get the formatted address or co-ordinates of any location.

The code is Python 2, but Python 3 compatible.

Installation
============

Fast install:

```
pip install mygmap
```

For a manual install get this package:

```
wget https://github.com/nikhilkumarsingh/mygmap/archive/master.zip
unzip master.zip
rm master.zip
cd mygmap-master
```

Install the package:
```
python setup.py install    
````

Example
=======

```python

from geo import locator

# get formatted address of any location
print locator.get_address("rohini, delhi")

# get co-ordinates of location
print locator.get_coordinates("delhi")
```    
    

Here is the output:
```
Rohini, New Delhi, Delhi, India
(28.7040592, 77.10249019999999)
```
    