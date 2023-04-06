class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        groups = list(Counter(deck).values())
        
        gcd_ = 0
        for freq in groups:
            gcd_ = gcd(gcd_, freq)

        return gcd_ != 1