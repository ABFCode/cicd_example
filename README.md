# My CI/CD Github Workflows Project

This project demonstrates a basic setup for a Python application with automated testing.
It includes a simple adding module and a corresponding test.

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone <cicd_example>
    cd cicd_example
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Code (Example Usage)

The `add.py` module provides basic addition function. You can use it in a Python script or interpreter:

```python
from src.add import Add
adder = Add()

result_add = adder.add(10, 5)
print(f"10 + 5 = {result_add}")
```
