import pytest
from chinese_zodiac import chinese_zodiac

def test_rat_year():
    """Test years that should return Rat (e.g., 2020, 2008)"""
    assert chinese_zodiac(2020) == "Rat"
    assert chinese_zodiac(2008) == "Rat"
    assert chinese_zodiac(1996) == "Rat"

def test_ox_year():
    """Test years that should return Ox (e.g., 2021, 2009)"""
    assert chinese_zodiac(2021) == "Ox"
    assert chinese_zodiac(2009) == "Ox"
    assert chinese_zodiac(1997) == "Ox"

def test_tiger_year():
    """Test years that should return Tiger (e.g., 2022, 2010)"""
    assert chinese_zodiac(2022) == "Tiger"
    assert chinese_zodiac(2010) == "Tiger"
    assert chinese_zodiac(1998) == "Tiger"

def test_rabbit_year():
    """Test years that should return Rabbit (e.g., 2023, 2011)"""
    assert chinese_zodiac(2023) == "Rabbit"
    assert chinese_zodiac(2011) == "Rabbit"
    assert chinese_zodiac(1999) == "Rabbit"

def test_dragon_year():
    """Test years that should return Dragon (e.g., 2024, 2012)"""
    assert chinese_zodiac(2024) == "Dragon"
    assert chinese_zodiac(2012) == "Dragon"
    assert chinese_zodiac(2000) == "Dragon"

def test_snake_year():
    """Test years that should return Snake (e.g., 2025, 2013)"""
    assert chinese_zodiac(2025) == "Snake"
    assert chinese_zodiac(2013) == "Snake"
    assert chinese_zodiac(2001) == "Snake"

def test_horse_year():
    """Test years that should return Horse (e.g., 2026, 2014)"""
    assert chinese_zodiac(2026) == "Horse"
    assert chinese_zodiac(2014) == "Horse"
    assert chinese_zodiac(2002) == "Horse"

def test_goat_year():
    """Test years that should return Goat (e.g., 2027, 2015)"""
    assert chinese_zodiac(2027) == "Goat"
    assert chinese_zodiac(2015) == "Goat"
    assert chinese_zodiac(2003) == "Goat"

def test_monkey_year():
    """Test years that should return Monkey (e.g., 2028, 2016)"""
    assert chinese_zodiac(2028) == "Monkey"
    assert chinese_zodiac(2016) == "Monkey"
    assert chinese_zodiac(2004) == "Monkey"

def test_rooster_year():
    """Test years that should return Rooster (e.g., 2029, 2017)"""
    assert chinese_zodiac(2029) == "Rooster"
    assert chinese_zodiac(2017) == "Rooster"
    assert chinese_zodiac(2005) == "Rooster"

def test_dog_year():
    """Test years that should return Dog (e.g., 2030, 2018)"""
    assert chinese_zodiac(2030) == "Dog"
    assert chinese_zodiac(2018) == "Dog"
    assert chinese_zodiac(2006) == "Dog"

def test_pig_year():
    """Test years that should return Pig (e.g., 2031, 2019)"""
    assert chinese_zodiac(2031) == "Pig"
    assert chinese_zodiac(2019) == "Pig"
    assert chinese_zodiac(2007) == "Pig"
