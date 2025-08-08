def addBinary(self, a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2))[2:]


# convert binary string to int, add them, and convert back to binary string
# int(x,2) converts binary string x to int
# bin(x) converts int x to binary string prefixed with '0b', so we slice the first two characters