class Circle:
    def draw(self):
        return "Drawing a Circle"

class Square:
    def draw(self):
        return "Drawing a Square"

class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        if shape_type == "square":
            return Square()
        else:
            return None


factory = ShapeFactory()
shape = factory.create_shape("triangle")   
print(shape.draw())  
#Direct object creation throughout the codebase leads to tight coupling, code duplication, and maintenance headaches, as every change requires modifying multiple locations.
#In contrast, the factory pattern centralizes object creation logic, promoting loose coupling, easier extensibility,
#consistent behavior, and better testability by encapsulating instantiation details in a single place.
