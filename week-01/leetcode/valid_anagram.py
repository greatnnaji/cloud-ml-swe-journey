from collections import Counter

def isAnagram(s: str, t: str) -> bool:
    print(Counter(s) == Counter(t))
    
    return Counter(s) == Counter(t)

isAnagram("anagram", "nagaram")
