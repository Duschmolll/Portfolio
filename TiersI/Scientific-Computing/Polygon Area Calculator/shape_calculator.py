class Rectangle:
    def __init__(self, w, h) -> None:
        self.width = w
        self.height = h

    def __str__(self) -> str:
        return "Rectangle(width={}, height={})".format(self.width, self.height)

    def set_width(self, x):
        self.width = x

    def set_height(self, y):
        self.height = y

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width**2 + self.height**2) ** 0.5

    def get_picture(self):
        picture = ""
        if self.width > 50 or self.height > 50:
            picture = "Too big for picture."
        else:
            for i in range(self.height):
                for x in range(self.width):
                    picture += "*"
                picture += "\n"
        return picture

    def get_amount_inside(self, shape):
        return int((self.height / shape.height) * (self.width / shape.width))


class Square(Rectangle):
    def __init__(
        self,
        w,
    ) -> None:
        self.set_width(w)
        self.set_height(w)

    def __str__(self) -> str:
        return "Square(side={})".format(self.height)

    def set_side(self, s):
        self.set_width(s)
        self.set_height(s)

    def set_height(self, y):
        super().set_height(y)
        super().set_width(y)

    def set_width(self, x):
        super().set_width(x)
        super().set_height(x)
