# C++

Runnable notes about C++ syntax, STL, and modern C++ features.

## Files

- `basics.cpp` — Core C++ syntax: types, variables, references, pointers, control flow, containers (vector, map, set), functions, lambdas, classes, templates, smart pointers, std::optional, std::variant, algorithms, exceptions, and enums.

## Build & Run

Using Makefile targets (recommended):

```bash
make cpp        # Compile + run all programs
make cpp-check  # Syntax check only (from cpp directory)
```

Or compile and run directly:

```bash
g++ -std=c++20 -Wall -Wextra -o basics.o basics.cpp
./basics
```

## Compiler Requirements

- **C++20** or later support
- Tested with:
  - GCC 10+ (`g++`)
  - Clang 10+ (`clang++`)
  - Apple Clang 12+ (macOS)

## Topics Covered

### Core C++

- Types and variables (auto, const, constexpr)
- References and pointers
- Strings and string operations
- Control flow (if/else, switch, loops, range-for)
- Functions (overloading, default arguments, pass by reference)

### STL Containers

- `std::vector` - dynamic arrays
- `std::map` - ordered key-value pairs
- `std::set` - ordered unique elements
- Iterators and algorithms

### Modern C++ (C++11/14/17/20)

- Lambda expressions
- Smart pointers (`unique_ptr`, `shared_ptr`)
- `std::optional` - optional values
- `std::variant` - type-safe unions
- Structured bindings (C++17)
- Range-based for loops

### Object-Oriented Programming

- Classes and structs
- Constructors and member functions
- Access control (public, private)
- Templates (functions and classes)

### STL Algorithms

- `sort`, `find`, `count`
- `accumulate`, `min_element`, `max_element`
- `all_of`, `any_of`, `none_of`
- `transform` with lambdas

## Testing

C++ programs are automatically compiled and tested via `make test` and in CI to ensure they build without errors and run successfully.
