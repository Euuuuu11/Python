# continue는 다음 반복을 진행 break는 반복문을 바로 끝는거


absent = [2, 5] # 결석
no_book = [7]   # 책 두고옴
for student in range(1, 11): # 1 ~ 10
    if student in absent:
        continue
    elif student in no_book:
        print('오늘 수업 여기까지. {0}는 교무실로 따라와'.format(student))
        break
    print('{0}, 책을 읽어봐'.format(student))

