class FigureL:
    def __init__(self):
        self.versions = (
            ((1, 1, 0), (0, 1, 0), (0, 1, 0)),
            ((0, 0, 1), (1, 1, 1), (0, 0, 0)),
            ((0, 1, 0), (0, 1, 0), (0, 1, 1)),
            ((0, 0, 0), (1, 1, 1), (1, 0, 0))
        )
        self.current_version = 0

    def rotate(self):
        if self.current_version == 3:
            self.current_version = 0
        else:
            self.current_version += 1

    def get(self):
        return self.versions[self.current_version]

    def get_rotated(self):
        a = self.current_version
        self.rotate()
        b = self.versions[self.current_version]
        self.current_version = a
        return b


class FigureJ:
    def __init__(self):
        self.versions = (
            ((0, 1, 1), (0, 1, 0), (0, 1, 0)),
            ((0, 0, 0), (1, 1, 1), (0, 0, 1)),
            ((0, 1, 0), (0, 1, 0), (1, 1, 0)),
            ((1, 0, 0), (1, 1, 1), (0, 0, 0))
        )
        self.current_version = 0

    def rotate(self):
        if self.current_version == 3:
            self.current_version = 0
        else:
            self.current_version += 1

    def get(self):
        return self.versions[self.current_version]

    def get_rotated(self):
        a = self.current_version
        self.rotate()
        b = self.versions[self.current_version]
        self.current_version = a
        return b


class FigureT:
    def __init__(self):
        self.versions = (
            ((0, 1, 0), (1, 1, 1), (0, 0, 0)),
            ((0, 1, 0), (0, 1, 1), (0, 1, 0)),
            ((0, 0, 0), (1, 1, 1), (0, 1, 0)),
            ((0, 1, 0), (1, 1, 0), (0, 1, 0))
        )
        self.current_version = 0

    def rotate(self):
        if self.current_version == 3:
            self.current_version = 0
        else:
            self.current_version += 1

    def get(self):
        return self.versions[self.current_version]

    def get_rotated(self):
        a = self.current_version
        self.rotate()
        b = self.versions[self.current_version]
        self.current_version = a
        return b


class FigureZ:
    def __init__(self):
        self.versions = (
            ((0, 0, 0), (1, 1, 0), (0, 1, 1)),
            ((0, 1, 0), (1, 1, 0), (1, 0, 0)),
            ((1, 1, 0), (0, 1, 1), (0, 0, 0)),
            ((0, 0, 1), (0, 1, 1), (0, 1, 0))
        )
        self.current_version = 0

    def rotate(self):
        if self.current_version == 3:
            self.current_version = 0
        else:
            self.current_version += 1

    def get(self):
        return self.versions[self.current_version]

    def get_rotated(self):
        a = self.current_version
        self.rotate()
        b = self.versions[self.current_version]
        self.current_version = a
        return b


class FigureS:
    def __init__(self):
        self.versions = (
            ((0, 0, 0), (0, 1, 1), (1, 1, 0)),
            ((1, 0, 0), (1, 1, 0), (0, 1, 0)),
            ((0, 1, 1), (1, 1, 0), (0, 0, 0)),
            ((0, 1, 0), (0, 1, 1), (0, 0, 1))
        )
        self.current_version = 0

    def rotate(self):
        if self.current_version == 3:
            self.current_version = 0
        else:
            self.current_version += 1

    def get(self):
        return self.versions[self.current_version]

    def get_rotated(self):
        a = self.current_version
        self.rotate()
        b = self.versions[self.current_version]
        self.current_version = a
        return b


class FigureI:
    def __init__(self):
        self.versions = (
            ((0, 1, 0, 0), (0, 1, 0, 0), (0, 1, 0, 0), (0, 1, 0, 0)),
            ((0, 0, 0, 0), (1, 1, 1, 1), (0, 0, 0, 0), (0, 0, 0, 0)),
            ((0, 0, 1, 0), (0, 0, 1, 0), (0, 0, 1, 0), (0, 0, 1, 0)),
            ((0, 0, 0, 0), (0, 0, 0, 0), (1, 1, 1, 1), (0, 0, 0, 0))
        )
        self.current_version = 0

    def rotate(self):
        if self.current_version == 3:
            self.current_version = 0
        else:
            self.current_version += 1

    def get(self):
        return self.versions[self.current_version]

    def get_rotated(self):
        a = self.current_version
        self.rotate()
        b = self.versions[self.current_version]
        self.current_version = a
        return b


class FigureO:
    def rotate(self):
        return

    def get(self):
        return (
            (1, 1), (1, 1)
        )

    def get_rotated(self):
        return self.get()
