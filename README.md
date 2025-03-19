# Geometric Shapes (Lab 6 and Lab 7)

This project implements classes for various geometric shapes and finds the shapes with the largest measure (area for 2D shapes, volume for 3D shapes) from input files.

## Project Files

- **shapes_2d.py** - Contains implementation of 2D shapes only
- **shapes.py** - Contains implementation of both 2D and 3D shapes with extended functionality

## Shape Classes

### 2D Shapes
1. **Triangle** - defined by three sides (a, b, c)
2. **Rectangle** - defined by two sides (a, b)
3. **Trapeze** - defined by two bases and two sides (a, b, c, d)
4. **Parallelogram** - defined by two sides and height (a, b, h)
5. **Circle** - defined by radius (r)

### 3D Shapes
1. **Ball** - defined by radius (r)
2. **TriangularPyramid** - defined by base side length and height (side, height)
3. **QuadrangularPyramid** - defined by base sides and height (a, b, height)
4. **RectangularParallelepiped** - defined by three edges (a, b, c)
5. **Cone** - defined by base radius and height (r, height)
6. **TriangularPrism** - defined by base triangle sides and prism height (a, b, c, height)

## Shape Hierarchy

The project implements an abstract class hierarchy:
- `Shape` - abstract base class with common methods
  - `TwoDimensionalShape` - base class for 2D shapes
  - `ThreeDimensionalShape` - base class for 3D shapes

Each shape class implements methods appropriate for its dimension:
- 2D shapes: `area()` and `perimeter()`
- 3D shapes: `volume()`, `square_surface()`, `square_base()` and more

## Usage

Run the program with:

```
python shapes.py [input_file1 input_file2 ...]
```

If no input files are specified, the program will:
1. Download default input files from GitHub if they don't exist locally
2. Process each input file to find the shape with maximum measure
3. Print the results with shape type and calculated values

For 2D-only functionality:
```
python shapes_2d.py
```

## Input File Format

Each line in the input file contains:
- Shape name (Triangle, Rectangle, Trapeze, Parallelogram, Circle, Ball, TriangularPyramid, etc.)
- Shape parameters separated by spaces

Example:
```
Rectangle 22 5
Circle 20
Ball 10
TriangularPyramid 10 12
```

## Results

For each input file, the program identifies the shape with the largest measure (area for 2D shapes, volume for 3D shapes).