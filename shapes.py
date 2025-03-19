import math
from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Literal


class Dimension(Enum):
    TWO_DIMENSIONAL = auto()
    THREE_DIMENSIONAL = auto()


class Shape(ABC):
    @abstractmethod
    def dimension(self) -> Dimension:
        pass
    
    @abstractmethod
    def perimeter(self) -> float | None:
        pass
    
    @abstractmethod
    def area(self) -> float | None:
        pass
    
    def square(self) -> float | None:
        return self.area()
    
    def square_surface(self) -> float | None:
        if self.dimension() == Dimension.TWO_DIMENSIONAL:
            return None
        return self._square_surface()
    
    def _square_surface(self) -> float:
        return None
    
    def square_base(self) -> float | None:
        if self.dimension() == Dimension.TWO_DIMENSIONAL:
            return None
        return self._square_base()
    
    def _square_base(self) -> float:
        return None
    
    def height(self) -> float | None:
        if self.dimension() == Dimension.TWO_DIMENSIONAL:
            return None
        return self._height()
    
    def _height(self) -> float:
        return None
    
    def volume(self) -> float:
        if self.dimension() == Dimension.TWO_DIMENSIONAL:
            return self.area()
        return self._volume()
    
    def _volume(self) -> float:
        return 0.0


class TwoDimensionalShape(Shape):
    def dimension(self) -> Dimension:
        return Dimension.TWO_DIMENSIONAL
    
    def square_surface(self) -> None:
        return None
    
    def square_base(self) -> None:
        return None
    
    def height(self) -> None:
        return None


class ThreeDimensionalShape(Shape):
    def dimension(self) -> Dimension:
        return Dimension.THREE_DIMENSIONAL
    
    def perimeter(self) -> None:
        return None
    
    def area(self) -> None:
        return None


class Triangle(TwoDimensionalShape):
    def __init__(self, a: float, b: float, c: float):
        if a + b <= c or a + c <= b or b + c <= a or a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Invalid triangle sides")
        
        self.a = a
        self.b = b
        self.c = c
    
    def perimeter(self) -> float:
        return self.a + self.b + self.c
    
    def area(self) -> float:
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


class Rectangle(TwoDimensionalShape):
    def __init__(self, a: float, b: float):
        if a <= 0 or b <= 0:
            raise ValueError("Rectangle sides must be positive")
        
        self.a = a
        self.b = b
    
    def perimeter(self) -> float:
        return 2 * (self.a + self.b)
    
    def area(self) -> float:
        return self.a * self.b


class Trapeze(TwoDimensionalShape):
    def __init__(self, a: float, b: float, c: float, d: float):
        if a <= 0 or b <= 0 or c <= 0 or d <= 0:
            raise ValueError("Trapeze sides must be positive")
        
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def perimeter(self) -> float:
        return self.a + self.b + self.c + self.d
    
    def area(self) -> float:
        p = self.perimeter() / 2
        try:
            return math.sqrt((p - self.a) * (p - self.b) * (p - self.c) * (p - self.d) - 
                            0.25 * (self.a * self.b - self.c * self.d) * (self.a * self.b - self.c * self.d))
        except ValueError:
            return 0


class Parallelogram(TwoDimensionalShape):
    def __init__(self, a: float, b: float, h: float):
        if a <= 0 or b <= 0 or h <= 0:
            raise ValueError("Parallelogram parameters must be positive")
        
        self.a = a
        self.b = b
        self.h = h
    
    def perimeter(self) -> float:
        return 2 * (self.a + self.b)
    
    def area(self) -> float:
        return self.a * self.h


class Circle(TwoDimensionalShape):
    def __init__(self, r: float):
        if r <= 0:
            raise ValueError("Circle radius must be positive")
        
        self.r = r
    
    def perimeter(self) -> float:
        return 2 * math.pi * self.r
    
    def area(self) -> float:
        return math.pi * self.r**2


class Ball(ThreeDimensionalShape):
    def __init__(self, r: float):
        if r <= 0:
            raise ValueError("Ball radius must be positive")
        
        self.r = r
    
    def _square_surface(self) -> float:
        return 4 * math.pi * self.r**2
    
    def _volume(self) -> float:
        return (4/3) * math.pi * self.r**3


class TriangularPyramid(Triangle, ThreeDimensionalShape):
    def __init__(self, side: float, height: float):
        if side <= 0 or height <= 0:
            raise ValueError("Triangular pyramid parameters must be positive")
        
        super().__init__(side, side, side)
        self.h = height
    
    def dimension(self) -> Dimension:
        return Dimension.THREE_DIMENSIONAL
    
    def _height(self) -> float:
        return self.h
    
    def _square_base(self) -> float:
        return super().area()
    
    def _square_surface(self) -> float:
        slant_height = math.sqrt((self.a / (2 * math.sqrt(3)))**2 + self.h**2)
        face_area = 0.5 * self.a * slant_height
        return 3 * face_area
    
    def _volume(self) -> float:
        return (1/3) * self._square_base() * self.h


class QuadrangularPyramid(Rectangle, ThreeDimensionalShape):
    def __init__(self, a: float, b: float, height: float):
        if a <= 0 or b <= 0 or height <= 0:
            raise ValueError("Quadrangular pyramid parameters must be positive")
        
        Rectangle.__init__(self, a, b)
        self.h = height
    
    def dimension(self) -> Dimension:
        return Dimension.THREE_DIMENSIONAL
    
    def _height(self) -> float:
        return self.h
    
    def _square_base(self) -> float:
        return Rectangle.area(self)
    
    def _square_surface(self) -> float:
        slant_height_a = math.sqrt((self.a/2)**2 + self.h**2)
        slant_height_b = math.sqrt((self.b/2)**2 + self.h**2)
        
        face_area_a = 0.5 * self.a * slant_height_b
        face_area_b = 0.5 * self.b * slant_height_a
        
        return 2 * (face_area_a + face_area_b)
    
    def _volume(self) -> float:
        return (1/3) * self._square_base() * self.h


class RectangularParallelepiped(Rectangle, ThreeDimensionalShape):
    def __init__(self, a: float, b: float, c: float):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Rectangular parallelepiped parameters must be positive")
        
        Rectangle.__init__(self, a, b)
        self.c = c
    
    def dimension(self) -> Dimension:
        return Dimension.THREE_DIMENSIONAL
    
    def _height(self) -> float:
        return self.c
    
    def _square_base(self) -> float:
        return Rectangle.area(self)
    
    def _square_surface(self) -> float:
        return 2 * (self.a * self.c + self.b * self.c)
    
    def _volume(self) -> float:
        return self.a * self.b * self.c


class Cone(Circle, ThreeDimensionalShape):
    def __init__(self, r: float, height: float):
        if r <= 0 or height <= 0:
            raise ValueError("Cone parameters must be positive")
        
        Circle.__init__(self, r)
        self.h = height
    
    def dimension(self) -> Dimension:
        return Dimension.THREE_DIMENSIONAL
    
    def _height(self) -> float:
        return self.h
    
    def _square_base(self) -> float:
        return Circle.area(self)
    
    def _square_surface(self) -> float:
        slant_height = math.sqrt(self.r**2 + self.h**2)
        return math.pi * self.r * slant_height
    
    def _volume(self) -> float:
        return (1/3) * self._square_base() * self.h


class TriangularPrism(Triangle, ThreeDimensionalShape):
    def __init__(self, a: float, b: float, c: float, height: float):
        if a <= 0 or b <= 0 or c <= 0 or height <= 0:
            raise ValueError("Triangular prism parameters must be positive")
        
        Triangle.__init__(self, a, b, c)
        self.h = height
    
    def dimension(self) -> Dimension:
        return Dimension.THREE_DIMENSIONAL
    
    def _height(self) -> float:
        return self.h
    
    def _square_base(self) -> float:
        return Triangle.area(self)
    
    def _square_surface(self) -> float:
        return self.perimeter() * self.h
    
    def _volume(self) -> float:
        return self._square_base() * self.h


def parse_shape(line: str) -> Shape | None:
    parts = line.strip().split()
    if not parts:
        return None
    
    shape_type = parts[0]
    params = [float(p) for p in parts[1:]]
    
    try:
        match shape_type:
            case "Triangle":
                if len(params) == 3:
                    return Triangle(params[0], params[1], params[2])
            case "Rectangle":
                if len(params) == 2:
                    return Rectangle(params[0], params[1])
            case "Trapeze":
                if len(params) == 4:
                    return Trapeze(params[0], params[1], params[2], params[3])
            case "Parallelogram":
                if len(params) == 3:
                    return Parallelogram(params[0], params[1], params[2])
            case "Circle":
                if len(params) == 1:
                    return Circle(params[0])
            case "Ball":
                if len(params) == 1:
                    return Ball(params[0])
            case "TriangularPyramid":
                if len(params) == 2:
                    return TriangularPyramid(params[0], params[1])
            case "QuadrangularPyramid":
                if len(params) == 3:
                    return QuadrangularPyramid(params[0], params[1], params[2])
            case "RectangularParallelepiped":
                if len(params) == 3:
                    return RectangularParallelepiped(params[0], params[1], params[2])
            case "Cone":
                if len(params) == 2:
                    return Cone(params[0], params[1])
            case "TriangularPrism":
                if len(params) == 4:
                    return TriangularPrism(params[0], params[1], params[2], params[3])
    except ValueError as e:
        print(f"Error parsing shape {shape_type}: {e}")
        return None
    
    return None


def process_file(file_path: str) -> Shape | None:
    max_measure_shape = None
    max_measure = float('-inf')
    
    shapes_count = 0
    valid_shapes_count = 0
    
    try:
        with open(file_path, 'r') as f:
            for line in f:
                shapes_count += 1
                shape = parse_shape(line)
                
                if shape is None:
                    continue
                
                valid_shapes_count += 1
                
                try:
                    measure = shape.volume()
                    
                    if measure > max_measure:
                        max_measure = measure
                        max_measure_shape = shape
                except Exception as e:
                    print(f"Error calculating measure: {e}")
    
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
    
    print(f"Processed {shapes_count} shapes, {valid_shapes_count} were valid")
    return max_measure_shape


def download_input_files():
    import os
    import urllib.request
    
    base_url = "https://raw.githubusercontent.com/krenevych/oop/master/labs/lab01/home/task1/"
    files = ["input01.txt", "input02.txt", "input03.txt"]
    
    for file_name in files:
        url = base_url + file_name
        if not os.path.exists(file_name):
            try:
                urllib.request.urlretrieve(url, file_name)
                print(f"Downloaded {file_name}")
            except Exception as e:
                print(f"Error downloading {file_name}: {e}")


def main():
    import sys
    
    if len(sys.argv) > 1:
        input_files = sys.argv[1:]
    else:
        download_input_files()
        input_files = ["input01_3d.txt"]
    
    for file_path in input_files:
        print(f"\nProcessing {file_path}:")
        max_measure_shape = process_file(file_path)
        
        if max_measure_shape:
            measure_name = "Volume" if max_measure_shape.dimension() == Dimension.THREE_DIMENSIONAL else "Area"
            print(f"Shape with maximum measure: {max_measure_shape.__class__.__name__}")
            print(f"{measure_name}: {max_measure_shape.volume():.2f}")
        else:
            print("No valid shape found with maximum measure")


if __name__ == "__main__":
    main()