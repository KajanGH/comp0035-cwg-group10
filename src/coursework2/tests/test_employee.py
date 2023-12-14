import pytest
from your_module import RestAPI  # Import the RestAPI class from your module

# Test to retrieve all LAD data from the REST API
def test_get_all_lad_data():
    rest_api = RestAPI()  # Initialise the RestAPI instance
    lad_data = rest_api.retrieve_all_lad_data()
    assert len(lad_data) > 0  # Check if LAD data is retrieved successfully

# Test to retrieve specific LAD data from the REST API
def test_get_specific_lad_data():
    rest_api = RestAPI()  # Initialise the RestAPI instance
    country = "England"
    region = "London"
    extract_date = "2023-01-01"
    specific_lad_data = rest_api.retrieve_specific_lad_data(country, region, extract_date)
    assert specific_lad_data is not None  # Check if specific LAD data is retrieved successfully

# Test to add new LAD data to the REST API
def test_add_new_lad_data():
    rest_api = RestAPI()  # Initialise the RestAPI instance
    new_lad_data = {...}  # Define your sample LAD data
    response = rest_api.add_new_lad_data(new_lad_data)
    assert response == "Success"  # Assuming the response is expected to be "Success"

# Test to update existing LAD data in the REST API
def test_update_existing_lad_data():
    rest_api = RestAPI()  # Initialise the RestAPI instance
    updated_lad_data = {...}  # Define your sample updated LAD data
    response = rest_api.update_existing_lad_data(updated_lad_data)
    assert response == "Updated"  # Assuming the response is expected to be "Updated"

def test_delete_specific_lad_data():
    rest_api = RestAPI()  # Initialise the RestAPI instance
    country = "England"
    region = "London"
    extract_date = "2023-01-01"
    response = rest_api.delete_specific_lad_data(country, region, extract_date)
    assert response == "Deleted"  # Assuming the response is expected to be "Deleted"

#USED Chatgpt AI for the creation of the tests using the 3.1 template. Then edited the tests so it is correct and makes sense for our project. 

