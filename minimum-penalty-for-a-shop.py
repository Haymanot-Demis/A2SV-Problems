class Solution:
    def bestClosingTime(self, customers: str) -> int:
        closed_at = 0
        t_Yes = customers.count("Y")
        curr_nos = 0
        penality = t_Yes


        for i in range(len(customers)):
            if customers[i] == "N":
                curr_nos += 1

            curr_penality = curr_nos + (t_Yes - (i + 1 - curr_nos))
            if curr_penality < penality:
                closed_at = i + 1
                penality = curr_penality
            
        return closed_at