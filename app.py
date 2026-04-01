# pylint: disable=missing-module-docstring

import pandas as pd

def add(a, b):
    "Return sum of two numbers"
    return a + b

def subtract(a, b):
    "Return the difference of two numbers"
    return a - b

def mulitply(a, b):
    "Return product of two numbers"
    return a * b

def divide(a, b):
    "Return division result"
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def power(a,b):
    "Return power of a number"
    return a ** b

def load_iris():
    "Load iris dataset"
    return pd.read_csv("iris.csv")

def get_species_count(df):
    "Return number of unique species"
    if df.empty:
        return 0
    return df["species"].nunique()

if __name__ == "__main__":
    print(add(2, 3))
    print(subtract(5, 2))
    print(mulitply(2, 3))
    print(divide(10, 2))
    print(power(2, 3))
