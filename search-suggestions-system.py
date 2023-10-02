class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        answer = []
        start = 0
        for i in range(len(searchWord)):
            prefix = searchWord[:i + 1]
            start = bisect_left(products, prefix, start)
            result = []
            for j in range(start, min(len(products), start + 3)):
                k = min(len(prefix), len(products[j]))
                if products[j][:k] == prefix:
                    result.append(products[j])
            
            answer.append(result)
        
        return answer