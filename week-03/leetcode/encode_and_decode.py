# def encode(strs: list[str]) -> str:
#     result_str = ':;'.join(strs)
#     print(f"Encoding {strs} to {result_str}")
#     return result_str

# def decode(s: str) -> list[str]:
#     result_list = s.split(':;')
#     print(f"Decoding {s} to {result_list}")
#     return result_list

# dummy_input = []
# encoded = encode(dummy_input)
# print(f"Encoded: {encoded}")
# decoded = decode(encoded)
# print(f"Decoded: {decoded}")
#TO-DO: try to make work

# 2nd Solution
def encode(strs: list[str]) -> str:
    result_str = ""

    for string in strs:
        result_str += str(len(string)) + "#" + string

    return result_str

def decode(s: str) -> list[str]:

    return 



dummy_input = ["Hello","World"]
encoded = encode(dummy_input)
print(f"Encoded: {encoded}")
# decoded = decode(encoded)
# print(f"Decoded: {decoded}")