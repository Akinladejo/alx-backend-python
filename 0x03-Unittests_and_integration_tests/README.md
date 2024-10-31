# Unittests and Integration Tests

This project is focused on writing unit and integration tests for various utility functions and classes. It involves parameterizing tests, mocking HTTP calls, and creating fixtures for integration tests.

## Table of Contents

- [Description](#description)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Tests](#tests)
- [License](#license)

## Description

This project aims to practice and demonstrate the following concepts:

- Parameterizing unit tests
- Mocking HTTP calls
- Using `unittest.mock.patch` to replace parts of your system under test
- Writing integration tests with fixtures

## Requirements

- Python 3.7
- `unittest`
- `parameterized`
- `requests`
- `mock` (if not using Python 3.7)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/alx-backend-python.git
    cd alx-backend-python/0x03-Unittests_and_integration_tests
    ```

2. Install the required packages:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Running the Tests

To run the unit and integration tests, execute the following command in the project directory:

```sh
python -m unittest discover
