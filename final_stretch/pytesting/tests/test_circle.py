import pytest

import source.shapes as shapes
import math

class TestCircle:


    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = shapes.Circle(10)


    def teardown_method(self, method):
        print(f"tearing down {method}")

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2


    def test_perimeter(self):
        assert self.circle.perimeter() == 2 * math.pi * self.circle.radius    



        