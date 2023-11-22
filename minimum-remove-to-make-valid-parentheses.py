class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        openned_brackets = 0
        valid_paranthesis = []
        for ch in s:
            if ch != ")" or openned_brackets > 0:
                valid_paranthesis.append(ch)
                openned_brackets -= ch == ")"

            openned_brackets += ch == "("

        temp = []
        while openned_brackets > 0:
            top = valid_paranthesis.pop()
            if top != "(":
                temp.append(top)
            else:
                openned_brackets -= 1
        
        for ch in temp[::-1]:
            valid_paranthesis.append(ch)
        
        return "".join(valid_paranthesis)