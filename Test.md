<h1>PYTHON ASSERTION TYPES</h1>

---

- `assert`  =>  allows us to check if the condition is true
    
```python
assert 1 == 1
```
---

- `assert_never`  =>  allows us to check if two values are equal
          
```python
from typing import Union, assert_never

def handle_value(value: Union[int, str, float]):
    if isinstance(value, int):
        print("Handling an integer...")
    elif isinstance(value, str):
        print("Handling a string...")
    elif isinstance(value, float):
        print("Handling a float...")
    else:
        assert_never(value)

handle_value([])
```
---


## unittest.TestCase  assertions

<div style="background-color:#333; padding:20px; color:snow;">
NOTE: Please note that 
assertNotEqual, assertTrue, assertFalse, assertIs, assertIsNone, assertIn, and sertIsInstance
are part of the unittest module in Python and are not built-in assertions like assert. 
They need to be used within the context of a unittest.TestCase class.
</div>

1. `assertNotEqual(a, b)`: This assertion checks if a is not equal to b.

2. `assertTrue(x)`: This assertion checks if the value of x is True.

3. `assertFalse(x)`: This assertion checks if the value of x is False.

4. `assertIs(a, b)`: This assertion checks if a is b.

5. `assertIsNone(x)`: This assertion checks if the value of x is None.

6. `assertIn(a, b)`: This assertion checks if a is in b.

7. `assertIsInstance(a, b)`: This assertion checks if a is an instance of b.