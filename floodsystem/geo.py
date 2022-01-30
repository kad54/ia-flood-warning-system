# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa

from haversine import haversine
from .station import MonitoringStation

def stations_by_distance(stations, p):
    """Return a list of (station, distance) tuples sorted by distance
    from p
    Where stations is a list of MonitoringStation objects, and p is a
    tuple of floats for a coordinate p"""
    stationList = []

    #build list of (station, distance) tuples
    for station in stations:
        coords = station.coord
        distance = haversine(coords, p) # use haversine library to calculate distance in km
        stationList.append((station.name, station.town, distance))
    
    #sort list by distance
    stationList = sorted_by_key(stationList, 2)

def rivers_with_station(stations):
    """Given a list of station objects, returns a container list with the names of the rivers 
        with a monitoring station"""

    # Create an empty list to hold the rivers
    rivers = []

    # Iterate through the stations and append the river into the list if it is not already in the list
    for station in stations:
        if station.river not in rivers:
            rivers.append(station.river)
    
    # Sort by alphabetical order
    return sorted(rivers)

def stations_by_river(stations):

    # Create an empty dict to hold the rivers
    rivers_and_stations = {}

    # Iterate through all stations
    for station in stations:

        # Add the river and station name to the dict if the river is not already in the dict
        if station.river not in rivers_and_stations.keys():
            rivers_and_stations[station.river]=[station.name]

        # Append the station name to the corresponding river (key) in the dict
        else:
            rivers_and_stations[station.river].append(station.name)

    # Iterate through all dict items and sort the lists of station names (value) in alphabetical order
    for key in rivers_and_stations:
        rivers_and_stations[key].sort()

    return rivers_and_stations

    return stationList