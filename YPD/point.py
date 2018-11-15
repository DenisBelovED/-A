class Point:
    def __init__(self, x: int, y: int) -> None:
        self._x = int(x)
        self._y = int(y)

    def __init__(self, array: list) -> None:
        self._x = int(array[0])
        self._y = int(array[1])

    def get_coord(self) -> tuple:
        return self._x, self._y

    def distance_to_point(self, p: 'Point') -> int:
        return abs(self._x - p._x) + abs(self._y - p._y)

    @staticmethod
    def distance(p1: 'Point', p2: 'Point') -> int:
        return abs(p1._x - p2._x) + abs(p1._y - p2._y)
