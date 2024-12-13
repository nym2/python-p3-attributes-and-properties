#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="Give me your name!", job="What is your Job!!!"):
        self.name = name  # Calls the setter
        self.job = job  # Calls the setter

    @property
    def name(self):
        return self._name  # Getter for name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()  # Save valid name in title case
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = "Unknown"  # Default fallback for invalid names

    @property
    def job(self):
        return self._job  # Getter for job

    @job.setter
    def job(self, value):
        if value == "What is your Job!!!":
            self._job = value  # Allow the default value without validation
        elif value in APPROVED_JOBS:
            self._job = value  # Save valid job
        else:
            print("Job must be in list of approved jobs.")
            self._job = "Unknown job"  # Default fallback for invalid jobs
