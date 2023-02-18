class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailsRecievedEmail = set()
        for email in emails:
            temp = ""
            for indx, char in enumerate(email):
                if char == "+":
                    atIndx = email[indx:].index("@")
                    temp += email[atIndx + indx:]
                    emailsRecievedEmail.add(temp)
                    break
                if char == "@":
                    temp += email[indx:]
                    emailsRecievedEmail.add(temp)
                    break
                if char != ".":
                    temp += char
        return len(emailsRecievedEmail)