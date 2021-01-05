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


class FigureO:
    def rotate(self):
        return

    def get(self):
        return (
            (1, 1), (1, 1)
        )


