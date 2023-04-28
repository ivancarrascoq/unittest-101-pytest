import requests
from random import randint

def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None


class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


def rand_numbers(a):
    return randint(0, a)


def calculate_average(numbers: list):
    total = sum(numbers)
    count = len(numbers)
    return total / count

