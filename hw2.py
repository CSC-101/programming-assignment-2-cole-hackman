import data
from data import Point, Duration, Song, Rectangle

# Write your functions for each part in the space below.

# Part 1: Creates a rectangle using two points by defining the top-left and bottom-right corners.

#Parameters:
# point1 (Point): The first point defining one corner of the rectangle.
# point2 (Point): The second point defining the opposite corner of the rectangle.

#Returns:A rectangle object defined by the calculated top-left and bottom-right points.
def create_rectange(point1: Point, point2: Point) -> Point:
    topLeft = Point(min(point1.x, point2.x), max(point1.y, point2.y))
    bottomRight = Point(max(point1.x, point2.x), min(point1.y, point2.y))
    return Rectangle(topLeft, bottomRight)


# Part 2: Compares two durations and checks if the first duration is shorter than the second.

#Parameters:
# duration1 (Duration): The first duration to compare.
# duration2 (Duration): The second duration to compare against.

#Returns: True if duration1 is shorter than duration2, otherwise False.
def shorter_duration_than(duration1: Duration, duration2: Duration) -> bool:
    return (duration1.minutes*60 + duration1.seconds) < (duration2.minutes*60 + duration2.seconds)


# Part 3: Filters a list of songs to return only those with durations shorter than a specified length.

# Parameters:
# songList (list[Song]): List of Song objects to filter.
# songLength (Duration): The maximum duration a song can have to be included in the result.

#Returns: list[Song]: A list of Song objects that are shorter than the specified songLength.
def songs_shorter_than(songList: list[Song], songLength: Duration) -> list[Song]:
    shorterSongs = []
    for song in songList:
        if shorter_duration_than(song.duration, songLength):
            shorterSongs.append(song)
    return shorterSongs


# Part 4: Calculates the total running time of a playlist based on the durations of selected songs.

#Parameters:
# songList (list[Song]): List of Song objects with their respective durations.
# playlist (list[int]): List of indices corresponding to songs in songList to include in the playlist.

#Returns: The total running time of the selected playlist as a Duration object.
def running_time(songList: list[Song], playlist: list[int]) -> Duration:
    totalLength = Duration(0,0)
    for index in playlist:
        if 0 <= index < len(songList):
            totalLength.minutes += songList[index].duration.minutes
            totalLength.seconds += songList[index].duration.seconds
    if totalLength.seconds >= 60:
        totalLength.minutes += totalLength.seconds // 60
        totalLength.seconds = totalLength.seconds % 60
    return totalLength


# Part 5: Checks if each city link is bi-directional by ensuring each pair of city links exists in both directions.

#Parameters:
# cityLinks (list[list[str]]): List of pairs representing linked cities.
# cityNames (list[str]): List of valid city names.

#Returns: True if every link is bi-directional, otherwise False.
def validate_cityLinks(cityLinks: list[list[str]], cityNames: list[str]) -> bool:
    if len(cityLinks) <= 1:
        return True

    count = 0
    for link in cityLinks:
        link_reversed = [link[1], link[0]]
        if link_reversed in cityLinks:
            count += 1

    return count == len(cityLinks)


# Part 6: Finds the starting index of the longest repetition in a list of integers.

#Parameters:
#nums (list[int]): List of integers to analyze for consecutive repetitions.

#Returns: The starting index of the longest consecutive repetition in the list. If list is empty, returns None.
def longest_repetition(nums: list[int]) -> int:
    if nums == []:
        return None

    max_start_idx = 0
    start_idx = 0
    length = 1
    max_length = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            length += 1
        else:
            if length > max_length:
                max_length = length
                max_start_idx = start_idx
            length = 1
            start_idx = i

    return max_start_idx