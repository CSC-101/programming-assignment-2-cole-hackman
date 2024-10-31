import data
import hw2
import unittest
from data import Point, Rectangle, Duration, Song
from hw2 import create_rectange, shorter_duration_than, songs_shorter_than, running_time, validate_cityLinks, longest_repetition


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle_1(self):
        result = create_rectange(Point(2,2), Point(10,10))
        expected = Rectangle(Point(2,10), Point(10,2))
        self.assertEqual(result, expected)

    def test_create_rectangle_2(self):
        result = create_rectange(Point(8,7), Point(3,5))
        expected = Rectangle(Point(3,7), Point(8,5))
        self.assertEqual(result, expected)

    # Part 2
    def test_shorter_duration_than_1(self):
        duration1 = Duration(3, 15)
        duration2 = Duration(4, 10)
        self.assertTrue(shorter_duration_than(duration1, duration2))

    def test_shorter_duration_than_2(self):
        duration1 = Duration(5, 0)
        duration2 = Duration(5, 0)
        self.assertFalse(shorter_duration_than(duration1, duration2))

    # Part 3
    def test_songs_shorter_than_1(self):
        song1 = Song("NA","Song A", Duration(3, 15))
        song2 = Song("NA","Song B", Duration(2, 45))
        song3 = Song("NA","Song C", Duration(4, 0))
        songList = [song1, song2, song3]
        result = songs_shorter_than(songList, Duration(3, 0))
        expected = [song2]
        self.assertEqual(result, expected)

    def test_songs_shorter_than_2(self):
        song1 = Song("NA", "Song X", Duration(1, 30))
        song2 = Song("NA","Song Y", Duration(2, 10))
        songList = [song1, song2]
        result = songs_shorter_than(songList, Duration(3, 0))
        expected = [song1, song2]
        self.assertEqual(result, expected)

    # Part 4
    def test_running_time_1(self):
        song1 = Song("NA","Song A", Duration(2, 30))
        song2 = Song("NA","Song B", Duration(3, 45))
        song3 = Song("NA","Song C", Duration(1, 15))
        songList = [song1, song2, song3]
        playlist = [0, 1, 2]
        result = running_time(songList, playlist)
        expected = Duration(7, 30)
        self.assertEqual(result, expected)

    def test_running_time_2(self):
        song1 = Song("NA","Song D", Duration(0, 45))
        song2 = Song("NA","Song E", Duration(1, 30))
        songList = [song1, song2]
        playlist = [0, 1, 0]
        result = running_time(songList, playlist)
        expected = Duration(3, 0)
        self.assertEqual(result, expected)

    # Part 5
    def test_validate_cityLinks_1(self):
        cityLinks = [["A", "B"], ["B", "A"], ["C", "D"], ["D", "C"]]
        cityNames = ["A", "B", "C", "D"]
        self.assertTrue(validate_cityLinks(cityLinks, cityNames))

    def test_validate_cityLinks_2(self):
        cityLinks = [["A", "B"], ["C", "D"]]
        cityNames = ["A", "B", "C", "D"]
        self.assertFalse(validate_cityLinks(cityLinks, cityNames))

    # Part 6
    def test_longest_repetition_1(self):
        nums = [1, 1, 2, 2, 2, 3, 3]
        result = longest_repetition(nums)
        expected = 2
        self.assertEqual(result, expected)

    def test_longest_repetition_2(self):
        nums = [4, 4, 4, 4, 5, 5, 5]
        result = longest_repetition(nums)
        expected = 0
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
