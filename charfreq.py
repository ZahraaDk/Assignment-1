def char_frquency(n):
    dict = {}
    for char in n:
        if char in dict:
            dict[char] += 1 
        else:
            dict[char] = 1
    return dict

print(char_frquency("hello"))