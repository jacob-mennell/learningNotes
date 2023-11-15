**Decorators:**

Decorators can be used to modify or enhance the behavior of functions or methods. Getter, setter, and cache decorators are commonly used in object-oriented programming to manage class attributes. Let's break down each of them:

1. Getter and Setter Decorators:

   - In many programming languages, it's a common practice to have private class attributes and provide getter and setter methods to access and modify those attributes. In Python, you can achieve this using properties and decorators.
   - `@property` decorator is used to define a method as a getter. This method is called when you access the attribute's value.
   - `@<attribute_name>.setter` decorator is used to define a method as a setter. This method is called when you assign a value to the attribute.

   - Here's an example:

   ```python

   class MyClass:
       def __init__(self):
           self._my_var = 0  # Private variable with an underscore

       @property
       def my_var(self):
           return self._my_var
   
       @my_var.setter
       def my_var(self, value):
           if value >= 0:
               self._my_var = value
           else:
               raise ValueError("Value must be non-negative")

   obj = MyClass()
   obj.my_var = 42  # Calls the setter
   print(obj.my_var)  # Calls the getter

   ```

   In this example, the `my_var` attribute is accessed and modified through the `my_var` property methods.

2. Cache Decorators:
   - Caching is a technique used to store the results of expensive or time-consuming function calls so that subsequent calls with the same inputs can return the cached result instead of recomputing it.
   - Python provides various caching libraries and decorators for this purpose, such as `functools.lru_cache`.
   - The `@functools.lru_cache` decorator caches function results based on their input arguments.

   - Here's an example:
   ```python

   import functools

   @functools.lru_cache(maxsize=128)
   def fibonacci(n):
       if n <= 1:
           return n
       else:
           return fibonacci(n - 1) + fibonacci(n - 2)

   result = fibonacci(10)  # Computes and caches fibonacci(10)
   result_cached = fibonacci(10)  # Retrieves the cached result

   ```
   In this example, the `fibonacci` function is decorated with `@functools.lru_cache`, which caches the results of previous function calls to improve performance when calling the function with the same arguments again.

These decorators help improve code readability, maintainability, and performance by encapsulating attribute access logic and caching expensive function calls.

**Python Operators:**

In Python, `==`, `=`, and `is` are used for different purposes and have distinct meanings:

1. `==` (Equality Operator):
   - `==` is used to compare the **values** of two objects or variables to check if they are equal.
   - It returns `True` if the values are equal and `False` otherwise.
   - Example: `x == y` checks if the values stored in variables `x` and `y` are the same.

2. `=` (Assignment Operator):
   - `=` is used for **assignment** in Python.
   - It assigns a value to a variable.
   - Example: `x = 10` assigns the value `10` to the variable `x`.

3. `is` (Identity Operator):
   - `is` is used to check if two objects or variables refer to the **same memory location** (identity).
   - It returns `True` if the objects are the same (refer to the same memory location) and `False` otherwise.
   - Example: `x is y` checks if `x` and `y` reference the same object in memory.

In summary:

- `==` checks if the values of two objects are equal.
- `=` is used for variable assignment.
- `is` checks if two objects have the same identity (i.e., refer to the same memory location).

**Abstract Methods:**

```markdown
# Abstraction Example: Shape Drawing

## Abstract Class: Shape

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass
```

The abstract class `Shape` defines a common interface with an abstract method `draw`. This serves as a blueprint for various shapes, ensuring they all implement the `draw` method.

## Concrete Classes: Circle, Square, Triangle

```python
class Circle(Shape):
    def draw(self):
        return "Drawing a Circle"

class Square(Shape):
    def draw(self):
        return "Drawing a Square"

class Triangle(Shape):
    def draw(self):
        return "Drawing a Triangle"
```

Concrete classes like `Circle`, `Square`, and `Triangle` inherit from the abstract class `Shape` and provide specific implementations of the `draw` method.

## Usage: Drawing Shapes

```python
def draw_shape(shape):
    return shape.draw()

circle = Circle()
square = Square()
triangle = Triangle()

print(draw_shape(circle))    # Output: Drawing a Circle
print(draw_shape(square))    # Output: Drawing a Square
print(draw_shape(triangle))  # Output: Drawing a Triangle
```

The `draw_shape` function takes any object that conforms to the `Shape` interface, allowing you to draw different shapes without worrying about their specific implementations.

### Notes on Abstraction:

- **Encapsulation of Interface:** Abstract classes encapsulate a common interface, promoting a consistent structure across derived classes.

- **Code Flexibility:** Abstraction allows you to write functions or systems that can work with any class adhering to a specific interface, providing flexibility in code usage.

- **Promotes Modularity:** By hiding implementation details, abstraction encourages modularity and separation of concerns, making the codebase more maintainable.

- **Blueprint for Subclasses:** Abstract classes act as blueprints, guiding the implementation of concrete subclasses while ensuring adherence to a predefined structure.
```
