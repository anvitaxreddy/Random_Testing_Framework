import random
import string
import time
import os

# === Utility Functions for File Management === #

def write_to_file(filename, content):
    """Writes content to a file."""
    with open(filename, 'w') as f:
        f.write(content)

# === 1. Basic Test Generator === #

def generate_random_integer():
    """Generates random integers: positive, negative, or zero."""
    return random.choice([random.randint(-1000, -1), 0, random.randint(1, 1000)])

def generate_random_string():
    """Generates random strings: empty, single character, or multiple characters."""
    options = [
        "",  # Empty string
        random.choice(string.ascii_letters),  # Single character
        ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(2, 20)))  # Multiple characters
    ]
    return random.choice(options)

def generate_random_array():
    """Generates random arrays with integers or strings (mixing both types)."""
    length = random.randint(1, 10)
    return [random.choice([generate_random_integer(), generate_random_string()]) for _ in range(length)]

def generate_random_boolean():
    """Generates random boolean values: True or False."""
    return random.choice([True, False])

def generate_random_float():
    """Generates random floating-point numbers."""
    return random.uniform(-1000, 1000)

# === 2. Simple Test Runner === #

def run_test(test_function, input_generator, num_tests=100):
    """Runs a test function with inputs generated by the input generator."""
    passed, failed = 0, 0
    failure_cases = []

    for _ in range(num_tests):
        test_input = input_generator()
        try:
            result = test_function(test_input)
            passed += 1
        except Exception as e:
            failed += 1
            failure_cases.append((test_input, str(e)))

    return {"passed": passed, "failed": failed, "failure_cases": failure_cases}

def run_test_with_metrics(test_function, input_generator, num_tests=100):
    """Runs tests and records execution time."""
    start_time = time.time()
    results = run_test(test_function, input_generator, num_tests)
    end_time = time.time()
    results["time_taken"] = end_time - start_time
    return results

# === 3. Result Reporting === #

def generate_report(results, description, manual_results=None):
    """Generates a detailed report for the test results."""
    report = [
        f"Description: {description}",
        f"Total Tests Run: {results['passed'] + results['failed']}",
        f"Passed: {results['passed']}",
        f"Failed: {results['failed']}",
        "Failure Cases:"
    ]
    for case in results['failure_cases']:
        report.append(f"Input: {case[0]}, Error: {case[1]}")

    # Add comparison with manual testing
    if manual_results is not None:
        report.append("\nComparison with Manual Testing:")
        report.append(f"Manual Testing Total: {manual_results['total']}")
        report.append(f"Manual Testing Passed: {manual_results['passed']}")
        report.append(f"Manual Testing Failed: {manual_results['failed']}")
        report.append(f"Manual Testing Time Taken: {manual_results['time_taken']:.2f} seconds")
        report.append("\nManual Testing Inputs and Outputs:")

        # Adding manual test inputs, status (passed/failed) to the report
        for input_val, status in manual_results['inputs_outputs']:
            report.append(f"Input: {input_val}, Status: {status}")

    return "\n".join(report)

# === 4. Evaluation Plan === #

def evaluate_with_metrics(test_function, input_generators, num_tests, output_dir, manual_results=None):
    """Evaluates multiple input types and writes results to files."""
    # Create the data_types folder if it doesn't exist
    data_types_dir = os.path.join(output_dir, "data_types")
    os.makedirs(data_types_dir, exist_ok=True)

    for input_type, generator in input_generators.items():
        description = f"Testing {test_function.__name__} with {input_type} inputs."
        print(f"\n{description}")
        results = run_test_with_metrics(test_function, generator, num_tests)
        report = generate_report(results, description, manual_results)
        
        # Write report to the respective file in the data_types folder
        output_file = os.path.join(data_types_dir, f"{test_function.__name__}_{input_type}_results.txt")
        write_to_file(output_file, report)
        print(f"Results written to: {output_file}")

# === Manual Testing Framework === #

def manual_testing_with_user_input(test_function, input_type):
    """Performs manual testing where the user provides inputs."""
    print(f"\nStarting manual testing for {test_function.__name__} with {input_type} inputs.")
    print("Enter 'q' to quit manual testing.")

    passed, failed = 0, 0
    failure_cases = []
    inputs_outputs = []
    start_time = time.time()

    while True:
        try:
            # Prompt user for input
            user_input = input(f"Enter a {input_type} value: ")
            if user_input.lower() == 'q':
                break

            # Convert input to the correct type
            if input_type == "Integers":
                test_input = float(user_input)
                if test_input.is_integer():
                    test_input = int(test_input)  # Convert to int if it's a whole number
                else:
                    raise ValueError("Input is not an integer")
            elif input_type == "Strings":
                test_input = user_input
            elif input_type == "Arrays":
                try:
                    test_input = eval(user_input)  # e.g., "[1, 'a', 3]"
                    if not isinstance(test_input, list):
                        raise ValueError("Input is not a valid array")
                except:
                    raise ValueError("Invalid array format")
            elif input_type == "Booleans":
                test_input = user_input.lower() == 'true'  # Convert input to boolean (True or False)
            else:
                print(f"Unsupported input type: {input_type}")
                continue

            # Test the function with the input
            output_val = test_function(test_input)
            inputs_outputs.append((user_input, "passed"))  # Storing input and status
            print("Test passed.")
            passed += 1
        except Exception as e:
            print(f"Test failed with error: {e}")
            failed += 1
            inputs_outputs.append((user_input, "failed"))  # Storing input and status
            failure_cases.append((user_input, str(e)))

    end_time = time.time()

    return {
        "total": passed + failed,
        "passed": passed,
        "failed": failed,
        "failure_cases": failure_cases,
        "time_taken": end_time - start_time,
        "inputs_outputs": inputs_outputs  # Storing manual test inputs and their status
    }

# === Buggy Functions for Testing === #

def buggy_function_int(x):
    if isinstance(x, float):
        if x.is_integer():
            x = int(x)
        else:
            raise ValueError("Input must be a whole number")
    
    if not isinstance(x, int):
        raise ValueError("Input is not an integer")
    
    return x * 2

def buggy_function_string(s):
    if s == "":
        raise ValueError("Empty string not allowed!")
    return len(s)

def buggy_function_array(arr):
    if not isinstance(arr, list):
        raise ValueError("Input is not a list")
    if any(not isinstance(x, (int, str, bool)) for x in arr):
        raise ValueError("Array contains invalid element types")
    return sum([len(str(x)) for x in arr])

def buggy_function_boolean(b):
    """A buggy function for booleans that checks if the input is a boolean."""
    if not isinstance(b, bool):
        raise ValueError("Input is not a boolean")
    return b


# === Main Execution === #

if __name__ == "__main__":
    output_dir = "test_results"
    os.makedirs(output_dir, exist_ok=True)

    input_generators = {
        "Integers": generate_random_integer,
        "Strings": generate_random_string,
        "Arrays": generate_random_array,
        "Booleans": generate_random_boolean,
        "Floats": generate_random_float
    }

    evaluate_with_metrics(buggy_function_int, input_generators, num_tests=150, output_dir=output_dir)
    evaluate_with_metrics(buggy_function_string, input_generators, num_tests=150, output_dir=output_dir)
    evaluate_with_metrics(buggy_function_array, input_generators, num_tests=150, output_dir=output_dir)
    evaluate_with_metrics(buggy_function_boolean, {"Booleans": generate_random_boolean}, num_tests=150, output_dir=output_dir)
