# ddaaiillyy ddoouubbllee

def crunch(s):
    if(len(s) <= 1): return s
    result = s[0]
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            result += s[i]
    return result

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')