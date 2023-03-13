class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        f_of_queries = []
        f_of_words = []
        for string in queries:
            c = Counter(string)
            f_of_queries.append(c[min(c)])

        for word in words:
            c = Counter(word)
            f_of_words.append(c[min(c)])
        
        f_of_words.sort()
        l = len(f_of_words)
        ans = []
        for f in f_of_queries:
            ans.append(l - bisect_right(f_of_words, f))
            
        return ans