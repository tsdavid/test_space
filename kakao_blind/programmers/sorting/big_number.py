"""
start point = 2019-08-29
문제 = https://programmers.co.kr/learn/courses/30/lessons/42746
정답 = https://programmers.co.kr/learn/courses/30/lessons/42746/solution_groups?language=python3
포모도로 = 3

문제 설명
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고,
이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
순서를 재배치하여 만들 수 있는 가장 큰 수를
 "문자열" 로 바꾸어 return 하도록 solution 함수를 작성해주세요.

제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.
입출력 예
numbers	 return
[6, 10, 2]	6210
[3, 30, 34, 5, 9] 9534330


가정
1. 원소끼리 중복은 없다

풀이 전략
1. 각 원소를 chr이나 str 숫자로 바꿔서 생각해보면 어떨가 - 안됨

구굴링
https://www.geeksforgeeks.org/python-largest-number-possible-from-list-of-given-numbers/

구글링 한거에 그냥 털렸음
이거 다시 공부해야함

다른 사람들이 한것도 진짜 잘했음
나는 Method1 sorted + lambda로 함
"""

numbersA = [6, 10, 2]
returnA = 6210

numbersB = [3, 30, 34, 5, 9]
returnB = 9534330

numbers = numbersB.copy()

"""
refer other code from google
https://www.geeksforgeeks.org/python-largest-number-possible-from-list-of-given-numbers/
"""
# Method #1: Using sorted() + lambda
from functools import cmp_to_key

# printing original list
print("The original list is: " + str(numbers))

# using sorted() + lambda
# largest possible number in list
res = sorted(numbers, key=cmp_to_key(lambda i, j: -1
                                     if str(j) + str(i) < str(i) + str(j) else 1))
# printing result
print("The largest possible number : " + ''.join(map(str, res)))


# Method #2: Using itertools.permutation() + join() + max()
from itertools import permutations

# printing original list
print("Original list is : " + str(numbers))

# using itertools.permutation() + join() + max()
res = int(max((''.join(i) for i in permutations(str(i)
                                                for i in numbers)), key=int))
# permutations = 순열 구하기
# https://programmers.co.kr/learn/courses/4008/lessons/12836

# printing result
print("The largest possible number : " + str(res))

