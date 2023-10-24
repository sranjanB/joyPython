import csv
from gmplot import gmplot

gmap = gmplot.GoogleMapPlotter(12.9531555370789, 77.6186963390851, 17)
gmap.coloricon = "http://www.googlemapsmarkers.com/v1/009900/"

# Store the coordinates in a list
coordinates = []

with open('route.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        lat = float(row[0])
        long = float(row[1])
        coordinates.append((lat, long))

# Plot the path using coordinates and specify linewidth
gmap.plot(*zip(*coordinates), color='blue', edge_width=10)

print("MAP GENERATED SUCCESSFULLY!!")
gmap.draw("mymap.html")
