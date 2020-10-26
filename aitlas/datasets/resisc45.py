import os

import torchvision.transforms as transforms

from ..utils import pil_loader, tiff_loader
from .multi_class_csv import MultiClassCsvDataset


CLASSES_TO_IDX = {
    "airplane": 0,
    "airport": 1,
    "baseball_diamond": 2,
    "basketball_court": 3,
    "beach": 4,
    "bridge": 5,
    "chaparral": 6,
    "church": 7,
    "circular_farmland": 8,
    "cloud": 9,
    "commercial_area": 10,
    "dense_residential": 11,
    "desert": 12,
    "forest": 13,
    "freeway": 14,
    "golf_course": 15,
    "ground_track_field": 16,
    "harbor": 17,
    "industrial_area": 18,
    "intersection": 19,
    "island": 20,
    "lake": 21,
    "meadow": 22,
    "medium_residential": 23,
    "mobile_home_park": 24,
    "mountain": 25,
    "overpass": 26,
    "palace": 27,
    "parking_lot": 28,
    "railway": 29,
    "railway_station": 30,
    "rectangular_farmland": 31,
    "river": 32,
    "roundabout": 33,
    "runway": 34,
    "sea_ice": 35,
    "ship": 36,
    "snowberg": 37,
    "sparse_residential": 38,
    "stadium": 39,
    "storage_tank": 40,
    "tennis_court": 41,
    "terrace": 42,
    "thermal_power_station": 43,
    "wetland": 44,
}


class Resisc45Dataset(MultiClassCsvDataset):

    classes_to_idx = CLASSES_TO_IDX
