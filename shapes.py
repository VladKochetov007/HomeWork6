import math
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def perimeter(self) -> float:
        pass
    
    @abstractmethod
    def area(self) -> float:
        pass


class Triangle(Shape):
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


class Rectangle(Shape):
    def __init__(self, a: float, b: float):
        if a <= 0 or b <= 0:
            raise ValueError("Rectangle sides must be positive")
        
        self.a = a
        self.b = b
    
    def perimeter(self) -> float:
        return 2 * (self.a + self.b)
    
    def area(self) -> float:
        return self.a * self.b


class Trapeze(Shape):
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


class Parallelogram(Shape):
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


class Circle(Shape):
    def __init__(self, r: float):
        if r <= 0:
            raise ValueError("Circle radius must be positive")
        
        self.r = r
    
    def perimeter(self) -> float:
        return 2 * math.pi * self.r
    
    def area(self) -> float:
        return math.pi * self.r**2


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
    except ValueError:
        return None
    
    return None


def process_file(file_path: str) -> tuple[Shape | None, Shape | None]:
    max_area_shape = None
    max_area = float('-inf')
    
    max_perimeter_shape = None
    max_perimeter = float('-inf')
    
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
                    area = shape.area()
                    perimeter = shape.perimeter()
                    
                    if area > max_area:
                        max_area = area
                        max_area_shape = shape
                    
                    if perimeter > max_perimeter:
                        max_perimeter = perimeter
                        max_perimeter_shape = shape
                except Exception as e:
                    print(f"Error calculating area or perimeter: {e}")
    
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")
    
    print(f"Processed {shapes_count} shapes, {valid_shapes_count} were valid")
    return max_area_shape, max_perimeter_shape


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
    download_input_files()
    
    input_files = ["input01.txt", "input02.txt", "input03.txt"]
    
    for file_path in input_files:
        print(f"\nProcessing {file_path}:")
        max_area_shape, max_perimeter_shape = process_file(file_path)
        
        if max_area_shape:
            print(f"Shape with maximum area: {max_area_shape.__class__.__name__}")
            print(f"Area: {max_area_shape.area():.2f}")
        else:
            print("No valid shape found for maximum area")
        
        if max_perimeter_shape:
            print(f"Shape with maximum perimeter: {max_perimeter_shape.__class__.__name__}")
            print(f"Perimeter: {max_perimeter_shape.perimeter():.2f}")
        else:
            print("No valid shape found for maximum perimeter")


if __name__ == "__main__":
    main()