# def encode(strs: list[str]) -> str:
#     result_str = ':;'.join(strs)
#     print(f"Encoding {strs} to {result_str}")
#     return result_str

# def decode(s: str) -> list[str]:
#     result_list += s.split(':;')
#     print(f"Decoding {s} to {result_list}")
#     return result_list

# dummy_input = []
# encoded = encode(dummy_input)
# print(f"Encoded: {encoded}")
# decoded = decode(encoded)
# print(f"Decoded: {decoded}")
#TO-DO: try to make work
# The above fails edge case when input [] is given, if logic is changed to handle that, 
# it fails edge case where [""] is given
# Solution would be to use length of string as delimiter and add split logic as opposed to
# using .split() alone

# 2nd Solution
def encode(strs: list[str]) -> str:
    result_str = ""

    for string in strs:
        result_str += str(len(string)) + "#" + string

    return result_str

def decode(s: str) -> list[str]:
    result_list = []
    i = 0
    while i < len(s):
        j = i
        new_str = ""
        while s[j] != "#":
            j += 1
        
        length = int(s[i:j])
        new_str = s[j+1:j+1+length]
        result_list.append(new_str)
        i = j + 1 + length

    return result_list

# dummy_input = ["HelloGreatest","World"]
# encoded = encode(dummy_input)
# print(f"Encoded: {encoded}")
# decoded = decode(encoded)
# print(f"Decoded: {decoded}")