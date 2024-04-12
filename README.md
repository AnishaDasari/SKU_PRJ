# SKU_PRJ
# Strategy:
1. Retrieve Records:
    Use requests.get to fetch all records from the API.
   
2. Filter Records:
      2.1 Parse the response JSON and filter records based on the createdAt field.
      2.2 Convert the timestamp of January 1, 2022, to Unix time and compare it with the createdAt field to filter records     created on or after that date.
3. Count Filtered Records:
    Count the number of filtered records.
4. Save Filtered Records:
    Save the filtered records to a file in JSON format.
5. Testing:
    Write unit tests to cover normal and abnormal conditions, including testing for successful API responses, filtering correctness, and file saving.
   
**Implementation in Python:**
1. Dependencies:
  requests: For making HTTP requests.
Code Structure:
project/
│
├── src/
│ ├── main.py # Main script to retrieve, filter, count, and save records
│ ├── api_client.py # Module to interact with the API
│ ├── utils.py # Utility functions
│ └── tests/
│ ├── test_main.py # Test cases for main script
│ 
│
├── requirements.txt # Dependencies
└── README.md # Documentation

api_client.py: Contains functions to interact with the API.
utils.py: Contains utility functions for filtering records, counting records, and saving records to a file.
main.py:
  1. Retrieves all records from the API.
  2. Filters records created on or after January 1, 2022.
  3. Counts the filtered records.
  4. Saves the filtered records to a file.
tests/: Contains test cases for the main script and utility functions.
tests/test_main.py: Test cases for the main script.

Testing:

Write unit tests using Python's unittest module to cover the main script's functionality and edge cases.

*********************************************************************************************************
* Execution Steps
*********************************************************************************************************
Option 1:

## Setup

1. **Clone the Repository:**
   
   ```bash
   git clone <repository_url>
   cd project


Option 2:
1. Install Dependencies:
If you haven't already installed the dependencies globally, you can do so using pip:
**pip install requests**

2. Run the Main Script: after cloning the repo go to the src folder 
You can execute the main script directly:
**python main.py**
This command will run the main script, which will retrieve records from the API, filter them, count them, and save them to a file.

3. Run Tests (Optional):
Similarly, you can run the test script directly:
**python tests/test_main.py**
This command will execute the unit tests and display the results.

<img width="330" alt="image" src="https://github.com/AnishaDasari/SKU_PRJ/assets/166729919/e582fbc1-c0bc-440b-bb77-f272ec6e0222">

**Note**
Ensure you have Python installed on your system.
