# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon
    def __str__(self):
        return str(self.__dict__)

position = LatLon(42,3)
print(position)
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon): 
    def __init__(self, lat, lon, name):
        super().__init__(lat, lon)
        self.name = name
    def __str__(self):
        return str(self.__dict__)
        
testWay = Waypoint(42,3,'my name')
print(testWay)
# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE

class Geocache(Waypoint):
    def __init__(self, lat, lon, name, size, difficulty):
        super().__init__(lat,lon,name)
        self.size = size
        self.difficulty = difficulty
    def __str__(self):
        return str(self.__dict__)
        

testGeo = Geocache(123123.1313, 1323.444, 'name', 42,'really')
print(testGeo)
# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = Waypoint(41.70505, -121.51521, "Catacombs")


# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, 44.052137

# YOUR CODE HERE
geocache = Geocache(44.052137, 44.052137, "Newberry Views", 2, 1.5)
# Print it--also make this print more nicely
print(geocache)
