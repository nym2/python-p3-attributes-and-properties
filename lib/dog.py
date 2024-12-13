#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Unknown", breed="Unknown breed"):
        self.name = name  # Calls the setter for validation
        self.breed = breed  # Calls the setter for validation

    @property
    def name(self):
        return self._name  # Getter for name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value  # Assign valid name
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = "Unknown"  # Default fallback

    @property
    def breed(self):
        return self._breed  # Getter for breed

    @breed.setter
    def breed(self, value):
        if value == "Unknown breed":
            self._breed = value  # Skip validation for default case
        elif value in APPROVED_BREEDS:
            self._breed = value  # Assign valid breed
        else:
            print("Breed must be in list of approved breeds.")
            self._breed = "Unknown breed"  # Default fallback
