from collections import defaultdict
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domainVisitCountHash = defaultdict(int)
        for cpdomain in cpdomains:
            visitCount, domain = cpdomain.split()
            visitCount = int(visitCount)
            domainVisitCountHash[domain] += visitCount
            dot = domain.find(".")
            while dot != -1:
                domain = domain[dot+1:]
                domainVisitCountHash[domain] += visitCount
                dot = domain.find(".")

        return [str(visitCount) + " " + domain for domain, visitCount in domainVisitCountHash.items()]