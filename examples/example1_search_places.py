from places_lk import search_places

if __name__ == '__main__':
    places = search_places("Colombo", limit=10)
    for place in places:
        print(places)
