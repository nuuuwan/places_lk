# Places in Sri Lanka (places_lk)

This is a utility library for returning the location (latitude and longitude) of places in Sri Lanka.

## Usage

```python
from places_lk import get_places

places = get_places('Colombo', fuzzy=True, limit=1)
print(places)

>> [{'name': 'Colombo', 'latlng': [6.93194, 79.84778]}]
```

## Install

```bash
pip install places_lk-nuuuwan
``