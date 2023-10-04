from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.calander = SortedList([])
        
    def book(self, start: int, end: int) -> bool:
        if not self.calander:
            self.calander.add((start, end))
            return True
        else:
            pos = self.calander.bisect_left((start, end))
            if pos == len(self.calander):
                if self.calander[pos - 1][1] <= start:
                    self.calander.add((start, end))
                    return True
                else:
                    return False
            elif pos == 0:
                if self.calander[0][0] >= end:
                    self.calander.add((start, end))
                    return True
                else:
                    return False
            else:
                if self.calander[pos][0] >= end and self.calander[pos - 1][1] <= start:
                    self.calander.add((start, end))
                    return True
                

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)