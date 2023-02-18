"""
Polycarp, a renowned competitive programmer, is always in search of a challenge. His friend has given him a task to solve an interesting problem.
The problem is as follows:  given a string s consisting of only lowercase English letters, 
you need to find the number of substrings in s that begin and end with the same character. 

A substring is a contiguous non-empty sequence of characters within a string.
As Polycarp loves to take on challenging problems, he decided to solve this one too. 
Can you help Polycarp by writing a program that solves this problem?

Example: 
Input: s = "bacbab" --> b, a, c, b, a, ba, cb, ba, bac, bacb, acba
Output: 7
 
Explanation:
The substrings of length 1 that start and end with the same letter are: "a", "b", "c", "b", and "a".
The substring of length 3 that starts and ends with the same letter is: "bacb".
The substring of length 5 that starts and ends with the same letter is: "acba".
abacad
"""

from collections import Counter


def count_substrings(input_string):
    counter = Counter(input_string)
    substr_count = 0
    for freq in counter.values():
        substr_count += freq*(freq + 1) // 2
    return substr_count


print(count_substrings("bacba"))
