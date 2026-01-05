def groupAnagrams(strs: list[str]) -> list[list[str]]:
    anagrams_dict = dict()
    for string in strs:
        sorted_chars = sorted(string)
        key = ''.join(sorted_chars)

        if key in anagrams_dict:
            anagrams_dict[key].append(string)
        else:
            anagrams_dict[key] = [string]
        
    result = []
    for value in anagrams_dict.values():
        result.append(value)
    print(result)
    return result

strs = ["act","pots","tops","cat","stop","hat"]
groupAnagrams(strs)

# note: .add for sets, .append for lists