class FigureL:
    def __init__(self):
        self.versions = (
            ((1, 1, 0), (0, 1, 0), (0, 1, 0)),
            ((0, 0, 1), (1, 1, 1), (0, 0, 0)),
            ((0, 1, 0), (0, 1, 0), (0, 1, 1)),
            ((0, 1, 0), (0, 1, 0), (0, 1, 1))
        )
        self.current_version = 0

    def rotate(self):
        if self.current_version == 3:
            self.current_version = 0
        else:
            self.current_version += 1

    def get(self):
        return self.versions[self.current_version]


# figure = FigureL()
# print(figure.get())
# figure.rotate()
# print(figure.get())
# figure.rotate()
# print(figure.get())
# figure.rotate()
# print(figure.get())
# figure.rotate()
# print(figure.get())
