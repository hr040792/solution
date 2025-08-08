def strStr(haystack: str, needle: str) -> int:
    # if needle is empty, return 0 
    if needle == "":
        return 0

    # Get lengths of the strings
    len_h = len(haystack)
    len_n = len(needle)

    # Loop through haystack where needle could fit
    for i in range(len_h - len_n + 1):
        # Compare substring of haystack with needle
        if haystack[i:i+len_n] == needle:
            return i  # Found the first occurrence

    # If needle is not found
    return -1


