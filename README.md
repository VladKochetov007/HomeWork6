# Geometric Shapes

This project implements classes for various geometric shapes and finds the shapes with the largest area and perimeter from input files.

## Shape Classes

1. **Triangle** - defined by three sides (a, b, c)
2. **Rectangle** - defined by two sides (a, b)
3. **Trapeze** - defined by two bases and two sides (a, b, c, d)
4. **Parallelogram** - defined by two sides and height (a, b, h)
5. **Circle** - defined by radius (r)

Each shape class:
- Implements the abstract `Shape` base class
- Has methods to calculate `area()` and `perimeter()`
- Validates input parameters for correctness

## Usage

Run the program with:

```
python shapes.py
```

The program will:
1. Download input files from GitHub if they don't exist locally
2. Process each input file to find the shape with maximum area and perimeter
3. Print the results with shape type and calculated values

## Input File Format

Each line in the input file contains:
- Shape name (Triangle, Rectangle, Trapeze, Parallelogram, Circle)
- Shape parameters separated by spaces

Example:
```
Rectangle 22 5
Parallelogram 0 8 21
Triangle 14 16 0
```

## Results

For each input file, the program identifies:
- The shape with the largest area
- The shape with the largest perimeter

According to results from all test files, the Circle with the largest radius has both the largest area and perimeter.