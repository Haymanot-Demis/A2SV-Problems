"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        # let build a dictionary that has the id as a key and the whole data as a value
        employee_of = {}

        for indx, value in enumerate(employees):
            employee_of[value.id] = value

        return self.dfs(employee_of, id)

    def dfs(self, employee_of, curr):
        def visited(id):
            if employee_of[id].importance == 101:
                return True
            return False

        importances = employee_of[curr].importance
        employee_of[curr].importance = 101

        for subordinate in employee_of[curr].subordinates:
            if not visited(subordinate):
                importances += self.dfs(employee_of, subordinate)
                
        return importances