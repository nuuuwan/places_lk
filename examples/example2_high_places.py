
import sys
from places_lk import search_places_smart

if __name__ == '__main__':
    places = search_places_smart(lambda place_info: place_info.alt.alt_m > 2_000)
    places = sorted(places, key=lambda place_info: place_info.alt.alt_m, reverse=True)
    for place in places:
        print(place)
