import pytest
import pandas as pd
from app import (
    add,
    subtract,
    mulitply,
    divide,
    power,
    load_iris,
    get_species_count,
)

def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 2) == 3


def test_multiply():
    assert mulitply(2, 3) == 6

def test_divide():
    assert divide(10, 2) == 5

def test_divide_by_zero():
    assert divide(10, 0) == "Cannot divide by zero"

def test_powert():
    assert power(2, 3) == 8

# ------- Fixture ------
@pytest.fixture
def data():
    return load_iris()

# Dataset tests
def test_data_loaded(data):
    assert not data.empty

def test_species_count(data):
    assert get_species_count(data) == 3

def test_columns_exist(data):
    assert "species" in data.columns

def test_empty_data():
    df = pd.DataFrame()
    assert get_species_count(df) == 0