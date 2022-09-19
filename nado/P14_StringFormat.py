# print('a' + 'b')
# print('a', 'b')


# 방법 1.
print('나는 %d살입니다.' % 20)         # %d / d는 정수를 의믜한다.
print('나는 %s을 좋아해요' % '파이썬')  # %s / s는 문자열
print('Apple 은 %c로 시작해요.' % 'A') # %c 는 캐릭터라 한글자만 받겠다.
# %s는 정수건 문자건 다 상관없다 
print('나는 %s살입니다.' % 20)         
print('나는 %s색과 %s색을 좋아해요.' %('파란', '빨간'))

# 방법 2.
print('나는 {}살입니다.'.format(20))
print('나는 {}색과 {}색을 좋아해요'.format('파란', '빨간'))
print('나는 {0}색과 {1}색을 좋아해요'.format('파란', '빨간'))
print('나는 {1}색과 {0}색을 좋아해요'.format('파란', '빨간'))

# 방벙 3.
print('나는 {age}살이며, {color}색을 좋아해요.'.format(age = 20, color='빨간'))
print('나는 {age}살이며, {color}색을 좋아해요.'.format(color='빨간', age = 20))

# 방법 4. (v3.6 이상~)
age = 20
color = "빨간"
print(f'나는 {age}살이며, {color}색을 좋아해요.')
