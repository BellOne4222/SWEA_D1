# 2056 연월일 달력

T = int(input())
for tc in range(1, T + 1):
    data = input()
    Y = data[0:4]
    M = data[4:6]
    D = data[6:8]
 
    if (int(M) in [1, 3, 5, 7, 8, 10, 12]) and (0 <int(D)<32):
        ans = str(Y) + '/' + str(M) + '/' + str(D)
    elif (int(M) in [4, 6, 9, 11]) and (0<int(D)<31):
        ans = str(Y) + '/' + str(M) + '/' + str(D)
    elif int(M) == 2 and (0<int(D)<29):
        ans = str(Y) + '/' + str(M) + '/' + str(D)
    else:
        ans = '-1'
    print('#{} {}'.format(tc, ans))



# 사실 이 문제는 어떻게 간결하게 푸냐가 관건인거 같다. 사실 문제는 쉬운데 간결하게 풀려고 하다보니 시간이 좀 걸렸던 문제였다. 처음에는 그냥 일단 적어보고 줄일 수 있는 방법을 생각하자 싶어, M == '4' or M == '6' ... 이런식으로 적었었는데 너무 코드가 쓸데없이 길어져 책이나 검색을 통해 위와 같은 방법을 찾았다. 저런 식으로 int(M) in [4, 6, 9, 11]에서 in을 써 중복없이 한번에 조건문을 설정 가능하다는 것을 배웠다.