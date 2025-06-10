def solution(string, ending):
    return string.endswith(ending)


result1 = solution("Hello World", "World")
print(result1)  

result2 = solution("Hello World", "hello")
print(result2)  

result3 = solution("Test", "t")
print(result3)  
