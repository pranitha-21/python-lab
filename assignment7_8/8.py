def decode_ways(s, index=0, path="", results=None):
    if results is None:
        results = []
    
    if index == len(s):
        results.append(path)
        return
    

    num1 = int(s[index])
    if 1 <= num1 <= 9:
        decode_ways(s, index + 1, path + chr(num1 + 64), results)

    if index + 1 < len(s):
        num2 = int(s[index:index + 2])
        if 10 <= num2 <= 26:
            decode_ways(s, index + 2, path + chr(num2 + 64), results)
    
    return results