# Unit tests for the comfort_level() function

# Fill in the blank spaces in the calls to comfort_level() below, using
# the values you've chosen for testing the function

# Then write a test_ok() function that tests the other equivalence class

from weather import comfort_level

def test_cold():
    assert comfort_level(    ) == "COLD"
    assert comfort_level(    ) == "COLD"

def test_hot():
    assert comfort_level(    ) == "HOT"
    assert comfort_level(    ) == "HOT"
