from R1 import Rectangle, Square, Circle

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)

print (rect_1.get_area_rectangle())
print (rect_2.get_area_rectangle())

square_1 = Square(5)
square_2 = Square(10)

print(square_1.get_area_square(),
      square_2.get_area_square())

circle_1 = Circle(3)
circle_2 = Circle(7)

print(circle_1)
print(circle_2)

figures=[rect_1, rect_2, circle_1, square_1, square_2, circle_2]


for figure in figures:
    if isinstance(figure, Square):
        print("площадь квадрата"+":"+str(figure.get_area_square()))
    elif isinstance(figure, Rectangle):
        print("площадь прямоугольгика"+":"+str(figure.get_area_rectangle()))
    elif isinstance(figure, Circle):
        print("площадь круга"+":"+str(figure.get_area_circle()))
    else:
        print("не удалось определить фигуру")
