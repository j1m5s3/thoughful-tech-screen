# README: Running the `thoughtful-ai-tech-screen.py` Script

## Overview
The `thoughtful-ai-tech-screen.py` script is a Python program designed to classify packages based on their dimensions and mass. It reads input data from a JSON file, processes the data, and outputs the classification results to another JSON file.

## Prerequisites
Before running the script, ensure the following requirements are met:

1. **Python Version**: Python 3.7 or higher is installed on your system.
2. **Dependencies**: No external libraries are required; the script uses Python's standard library.
3. **Input File**: A JSON file containing package data (e.g., `test_data.json`) must be available.

## Input File Format
The input JSON file should have the following structure:

```json
{
  "test1": {
    "width": 800,
    "height": 600,
    "length": 1000,
    "mass": 50
  },
  "test2": {
    "width": 1024,
    "height": 768,
    "length": 1500,
    "mass": 75
  }
}
```

Each package entry must include `width`, `height`, `length`, and `mass` as positive numbers.

## How to Run

1. **Clone or Download the Repository**:
   Ensure the script and the input file (`test_data.json`) are in the same directory.

2. **Run the Script**:
   Open a terminal or command prompt, navigate to the directory containing the script, and execute the following command:

   ```bash
   python thoughtful-ai-tech-screen.py
   ```

   By default, the script reads from `test_data.json` in the current directory.

3. **Specify a Custom Input File (Optional)**:
   If you want to use a different input file, provide the file path using the `--file` argument:

   ```bash
   python thoughtful-ai-tech-screen.py --file path/to/your/input_file.json
   ```

4. **Output**:
   - The script prints the classification results for each package to the terminal.
   - The results are saved to `test_results.json` in the same directory.

   Example output in `test_results.json`:

   ```json
   {
       "test1": "REJECTED",
       "test2": "REJECTED"
   }
   ```

## Notes
- Ensure the input file contains valid JSON data.
- The script will raise an error if any dimensions or mass are non-positive or if the file format is incorrect.

## Troubleshooting
- **Error: `FileNotFoundError`**: Ensure the input file exists and the path is correct.
- **Error: `AssertionError`**: Check that all dimensions and mass in the input file are positive numbers.

## License
This script is provided under the MIT License.