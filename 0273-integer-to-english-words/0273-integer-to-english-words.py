class Solution:
    def numberToWords(self, num: int) -> str:
        """
        the main idea behind this solution is we have to divide the whole number into 3 digit units then convert them in to word that is gives some hundreds then based on their position give their respective word naming
        i.e for example 1,234,567,879
        879 no extra naming just Eight Hundred Nine
        567 is thousands division Five Hundred Sixty Seven Tousand etc..
        the only diffence between each division is the last naming thousand, Million, Billion ...
        """
        if num == 0:
            return "Zero"
        nums = str(num)[::-1]
        result = ""
        division = ["","Thousand ", "Million ", "Billion "]
        for i in range(0, len(nums), 3):
            res = self.numberToWordsHelper(nums[i:i+3])
            if res:
                result = res + division[i//3] + result
        return result.strip()

    def numberToWordsHelper(self, digits:str):
        digitToWord = ["","One ","Two ", "Three ", "Four ", "Five ", "Six ", "Seven ", "Eight ", "Nine "]
        tenth = ["","Ten ", "Twenty ", "Thirty ", "Forty ", "Fifty ", "Sixty ", "Seventy ", "Eighty ", "Ninety "]
        teens = ["Ten ", "Eleven ","Twelve ", "Thirteen ", "Fourteen ", "Fifteen ", "Sixteen ", "Seventeen ", "Eighteen ", "Nineteen "]

        result = ""
        for i, digit in enumerate(digits):
            digit = int(digit)
            if i == 0:
                result = digitToWord[digit] + result
            elif i == 1:
                if digit == 1:
                    result = teens[int(digits[i - 1])]
                else:
                    result = tenth[digit] + result
            else:
                if digit != 0:
                    result = digitToWord[digit]  + "Hundred " + result
        return result
