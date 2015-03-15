This takes a datetime object with a timezone and converts it to be using a timezone that is from pytz. 
    
It is not efficient, but it should be a stop gap measure 

Installation:

```
pip install -e git+git://github.com/rchrd2/pytzconvert.git#egg=pytzconvert
```

 

## Example usage:

```
start = dateutil.parser.parse("2012-11-28T20:00:00-05:00")
if start.tzinfo:
    start = pytzconvert.convert(start)
```
    



## Running tests

    make test