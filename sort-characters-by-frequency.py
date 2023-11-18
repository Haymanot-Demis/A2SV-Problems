class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)

        freq_list = [(char, freq) for char, freq in counter.items()]

        freq_list.sort(key=lambda x : x[1], reverse=True)
        sorted_by_freq = []

        for char, freq in freq_list:
            sorted_by_freq += [char] * freq

        return "".join(sorted_by_freq)