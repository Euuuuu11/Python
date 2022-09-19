python = 'Python is Amazing'
print(python.lower())   # 모든문자 소문자
print(python.upper())   # 모든문자 대문자
print(python[0].isupper())  # python이라는 변수의 첫번째 값이 대문자인지
print(len(python))  # python이라는 변수의 길이
print(python.replace('Python', 'Java')) # Python을 찾고, Java로 바꿔라.

index = python.index('n')   # python이라는 변수안에  n이 몇번째 위치에 있는지.
print(index) 
index = python.index('n', index + 1)    #   python이라는 변수안에 두번째 n을 찾아라
print(index)

print(python.find('Java'))  # 원하는 값이 없을떄 -1 반환
# print(python.index('Java')) # ValueError: substring not found

print(python.count('n'))    # python 이라는 변수안에 n이 있는 횟수

