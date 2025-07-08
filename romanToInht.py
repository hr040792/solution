def romanToInt(self, s : str ) -> int:
    romanToInt = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0 
    store_val = 0
    for ch in reversed(s):
        val = romanToInt[ch]
        if val < store_val :
            total -= val 
        else:
            total += val
        store_val = val
    return total