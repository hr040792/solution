def isValid(self, s:str) -> bool:
    store = []
    mapp = {')': '(', '}': '{', ']': '['}
    for ch in s:
        if ch is mapp:
            if not store :
                return False
            topEle = store.pop()
            if mapp[ch] != topEle:
                return False
            else:
                store.append(ch)
    return not store
            