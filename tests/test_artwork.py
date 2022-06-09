from src.artwork.artwork import paint_can_be_stolen, they_overlap
from src.artwork.sensor import Sensor

class TestPaintCanBeStolen:
    def test_ct01(self):
        m, n = 10, 22
        sensors = [
            Sensor(4, 6, 5),
            Sensor(6, 16, 5),
        ]
        assert paint_can_be_stolen(sensors, m, n)

    def test_ct02(self):
        m, n = 10, 10
        sensors = [
            Sensor(3, 7, 9),
            Sensor(5, 14, 4),
        ]
        assert paint_can_be_stolen(sensors, m, n) is False

    def test_ct03(self):
        m, n = 100, 100
        sensors = [
            Sensor(40, 50, 30),
            Sensor(5, 90, 50),
            Sensor(90, 10, 5),
        ]
        assert paint_can_be_stolen(sensors, m, n)


class TestTheyOverlap:
    def test_ct01(self):
        s1 = Sensor(x=5, y=8, range=1)
        s2 = Sensor(x=2, y=4, range=4)
        assert they_overlap(s1, s2)

    def test_ct02(self):
        s1 = Sensor(x=5, y=8, range=1)
        s2 = Sensor(x=2, y=4, range=3)
        assert they_overlap(s1, s2) is False

    def test_ct03(self):
        s1 = Sensor(x=5, y=8, range=1)
        s2 = Sensor(x=2, y=4, range=5)
        assert they_overlap(s1, s2)

