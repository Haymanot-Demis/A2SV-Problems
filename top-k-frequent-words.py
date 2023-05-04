class Solution:
    def compare(self, word1, word2):
        if word1[1] > word2[1]:
            return True
        if word1[1] == word2[1] and word1[0] <= word2[0]:
            return True
        return False
    def heapify(self, words, parent):
        left = 2 * parent + 1
        right = 2 * parent + 2
        if left < len(words):
            largest = parent
            if self.compare(words[left], words[largest]):
                largest = left
            if right < len(words) and self.compare(words[right], words[largest]):
                largest = right
            
            if largest != parent:
                words[largest], words[parent] = words[parent], words[largest]
                self.heapify(words, largest)
    def heappop(self, heap):
        heap[0], heap[-1] = heap[-1], heap[0]
        popped = heap.pop()
        self.heapify(heap, 0) 
        return popped

    def nlargest(self, heap, k):
        top_k = []
        
        for _ in range(k):
            top_k.append(self.heappop(heap))
        return top_k

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq_hash_table = defaultdict(int)
        for word in words:
            freq_hash_table[word] += 1
        
        word_freq = []

        for word, freq in freq_hash_table.items():
            word_freq.append((word, freq))

        last_parent = len(word_freq) // 2 - 1

        for parent in range(last_parent, -1, -1):
            self.heapify(word_freq, parent)

        top_K_freq = self.nlargest(word_freq,k)

        return list(zip(*top_K_freq))[0]