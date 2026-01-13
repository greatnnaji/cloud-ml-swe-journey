def encode(strs: list[str]) -> str:
    result_str = ':;'.join(strs)
    return result_str

def decode(s: str) -> list[str]:
    result_list = s.split(':;')
    return result_list

dummy_input = [""]
encoded = encode(dummy_input)
print(f"Encoded: {encoded}")
decoded = decode(encoded)
print(f"Decoded: {decoded}")