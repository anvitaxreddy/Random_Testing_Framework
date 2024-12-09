# Random_Testing_Framework


## Description
This project is a **Random Testing Framework** that automates the process of generating random inputs for various data types and running tests on functions to verify their correctness. The framework supports testing for multiple data types like integers, strings, arrays, booleans, and floating-point numbers. The results are stored in the `data_types` folder under `test_results` for easy access and analysis.

## Installation Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/random-testing-framework.git
   cd random-testing-framework
2. pip install -r requirements.txt
3. python main.py

   

## Implementation of Techniques

The **Random Testing Framework** is implemented using Python and employs a variety of **random input generation techniques** to test various functions for different data types, including integers, strings, arrays, booleans, and floats. The core components of the framework include:

- **Random Input Generators**: Functions like `generate_random_integer`, `generate_random_string`, `generate_random_array`, and `generate_random_boolean` generate random inputs for testing.
- **Testing Functions**: The framework runs the generated inputs through various target functions, such as `buggy_function_int`, `buggy_function_string`, and `buggy_function_array`, to check if they handle the inputs correctly.
- **Error Handling and Reporting**: The framework captures any errors during testing, logs the failure cases, and stores them in separate text files under the `data_types` folder in `test_results`.

No external libraries are required for this project, as it uses only Python's built-in libraries such as `random`, `string`, `time`, and `os`.



## Experiment Artifacts

### Subject Programs
The subject programs in this project are several **buggy functions** designed to simulate common issues with handling different data types. These functions include:

- **`buggy_function_int(x)`**: This function tests integer handling, including handling of negative values and float-like integers.
- **`buggy_function_string(s)`**: This function tests string handling, specifically rejecting empty strings.
- **`buggy_function_array(arr)`**: This function tests array handling, ensuring that arrays contain valid types (integers, strings, booleans) and calculating the sum of element lengths.
- **`buggy_function_boolean(b)`**: This function tests Boolean input validation, ensuring that the input is a boolean.

### Results
The results of running the random tests are saved in the **`test_results/data_types`** folder. Each test result is stored in a separate file corresponding to the data type being tested, for example:

- `buggy_function_int_Integers_results.txt`
- `buggy_function_string_Strings_results.txt`
- `buggy_function_array_Arrays_results.txt`
- `buggy_function_boolean_Booleans_results.txt`

Each file includes:
- Total number of tests run
- Number of tests passed/failed
- Specific failure cases with input values and error messages

These results help analyze how well the functions handle a wide range of randomly generated inputs and identify any edge cases or bugs.

