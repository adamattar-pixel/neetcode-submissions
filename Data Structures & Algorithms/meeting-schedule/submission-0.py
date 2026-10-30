"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        l = sorted(intervals, key = self.myfunc)
        for i, interval in enumerate(l[1:]):
            if l[i].end > interval.start: return False
        return True

    def myfunc(self, i: Interval) -> int:
        return i.start