from hw4 import main 
import pytest

def test_values():
	assert main("Boston University") == "Boston University"
	assert main("ECE") == "ECE"
	assert main("Obama") == "Obama"
	assert main("China") == "China"
