This takes a datetime object with a timezone and converts it to be using a timezone that is from pytz. 
    
It is not efficient, but it should be a stop gap measure 

Installation:

```
pip install -e git+git://github.com/rchrd2/pytzconvert.git#egg=pytzconvert
```

 

Example usage:

```
start = dateutil.parser.parse(full_event['start']['dateTime'])
if start.tzinfo:
    start = pytzconvert.convert(start)
```
    
