cabinet = {3:'유재석', 100:'김태호'}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet[5])     # KeyError: 5
print(cabinet.get(5))   # none
print(cabinet.get(5, '사용가능'))
print('hi')

# 사전안에 값이 있는지 확인가능
print(3 in cabinet) # True
print(5 in cabinet) # False

# Key 값 문자열도 가능
cabinet = {'A-3':'유재석', 'B-100':'김태호'}
print(cabinet['A-3'])
print(cabinet['B-100'])

# 새 손님
print(cabinet)
cabinet['A-3'] = '김종국'
cabinet['C-20'] = '조세호'
print(cabinet)

# 간 손님
# Key 삭제
del cabinet['A-3']
print(cabinet)

# Key 들만 출력
print(cabinet.keys())

# value들만 출력
print(cabinet.values())

# Key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)




