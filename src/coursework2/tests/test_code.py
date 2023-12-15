def test_get_prepared_lad_data():
    """
    Test Case: Retrieve all LAD data

    GIVEN the REST API design
    WHEN a GET request is made to /api/v1/prepared_lad
    THEN ensure that all LAD data is retrieved successfully without any missing data and the format of the output  
    matches the expected data set. Make sure the returned code is appropriate such as 200 OK.

    """

def test_get_specific_prepared_lad_data():
    """
    Test Case: Retrieve specific LAD data

    GIVEN the REST API design
    WHEN a GET request is made to /api/v1/prepared_lad/{Country}/{Region}/{extract_date}
    THEN ensure that LAD data for a specific country, region, and extract date is retrieved correctly by checking if 
    the wanted specific country, region and extract date is returned. Make sure the returned code is appropriate 
    such as 200 OK.
"""

def test_post_prepared_lad_data():
    """
    Test Case: Add new LAD data

    GIVEN the REST API design
    WHEN a POST request is made to /api/v1/prepared_lad
    THEN ensure that the new data is in the correct format and in the data set without encountering and errors or 
    data corruption in the main data. Make sure the returned code is appropriate such as 201 Created.
    """

def test_update_prepared_lad_data():
    """
    Test Case: Update existing specific LAD data

    GIVEN the REST API design
    WHEN a PUT request is made to /api/v1/prepared_lad/{Country}/{Region}/{extract_date}
    THEN ensure that existing LAD data is updated without any data loss or any errors and the specific update 
    matches the format of the dataset.  Make sure the returned code is appropriate such as 200 OK or 204 No 
    Content. 
"""

def test_delete_prepared_lad_data():
    """
    Test Case: Delete LAD data

    GIVEN the REST API design
    WHEN a DELETE request is made to /api/v1/prepared_lad/{Country}/{Region}/{extract_date}
    THEN ensure that the specified LAD data is deleted by checking if that data is no longer in the dataset and   
    there are no unintentional residues. Make sure the returned code is appropriate such as 204 No Content due 
    to it being deleted.

    """
 
#Similar test cases can be written for other data sets such as prepared_itl, prepared_rgn, and prepared_ctry
