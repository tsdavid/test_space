"""
start point =
문제 = https://programmers.co.kr/learn/courses/30/lessons/42578#
정답 = https://programmers.co.kr/learn/courses/30/lessons/42578/solution_groups?language=python3
포모도로 = 4

결국 남의 코드 보고 품... 근데 코드작성 문제가 아니라 문제 자체를 어렵게 생각해서 그런거같음
내가 논리적으로 풀이를 못하네.
수학을 공부해야하나..
너무 어려운걸, 문제를 쉽게 생각하자 쉽게게
"""

clothesA = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
returnA = 5

clothesB = [["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]
returnB = 3

clothes = clothesA
answer = 0

import collections
# 경우에 수
# 첫번째 각 아이템 한번 씩 착용
answer += len(clothes)
# 두번째 중복되는 아이템은 교차로 착용 가능
type_list = []
for e in clothes:
	type_list.append(e[-1])

# 경우의 수 계산
mul = 1
lst = list(collections.Counter(type_list).values())
if len(lst) <= 1: mul = 0
elif len(lst) > 1:
	for i in range(len(lst)):
		mul *= lst[i]

print(answer + mul)

def solution1(clothes):
	"""28.6점 나옴"""
	answer = 0
	import collections
	# 경우에 수
	# 첫번째 각 아이템 한번 씩 착용
	answer += len(clothes)
	# 두번째 중복되는 아이템은 교차로 착용 가능
	type_list = []
	for e in clothes:
		type_list.append(e[-1])

	# 경우의 수 계산
	mul = 1
	lst = list(collections.Counter(type_list).values())
	if len(lst) <= 1:
		mul = 0
	elif len(lst) > 1:
		for i in range(len(lst)):
			mul *= lst[i]
	return answer + mul

"""
1. 전체 의상을 하나씩 입을 때(의상 이름 기준) - len(clothes)
(의상 종류 기준, 의상이 2개 이상인 종류가 존재)
2. 2개씩 입을 때 - nC2 * 중복된 개수
3. 3개씩 입을 때 - nC3 * 중복된 개수
4. n개씩 입을 때(n은 전체 의상종류) - 1 * 의상이 2개인 개수

최대 n개씩, 최소1 개씩  입음
n = 전체 의상종류
if n=5, 중복 2개, 2개, n = len(dic.keys())
최소 1개씩 = len(clothes)
	2개씩 = 5C2 * 2 * 2
	3개씩 = 5C3 * 2 * 2
	4개씩 = 5C4 * 2 * 2
	n개씩 = 5C5 = 1 * 2 * 2
	sum()
nCr = n! / r!(n-r)!

1, 1+1 , 1+1+1, if n > len(dic.keys()) -> break
"""
answer = 0
dic = dict()
for e in clothes:
	if e[1] not in dic.keys():
		dic[str(e[1])] = {
			'lst': [e[0]],
			'above': False,
			'count': 1
		}
	else:
		dic[str(e[1])]['lst'].append(e[0])
		dic[str(e[1])]['count'] = len(dic[str(e[1])]['lst'])
		dic[str(e[1])]['above'] = True

# 1번, 각 의상을 한번 씩 입는 수
answer += len(clothes)
# 2번 ~ n번까지
exn = len(dic.keys()) # 전체 의상종류
dpn = [] # 전체 의상 중 중복 되는 수
for key in list(dic.keys()):
	if dic[key]['above']:dpn.append(dic[key]['count'])
from math import factorial as fact
for i in range(exn)[1:]:
	answer += fact(exn)/fact(i+1)*fact(exn-(i+1)) * sum(dpn)     # nCr * 중복수
	# print(i+1)  #2,3,4,5



def solution2(clothes):
	"""14.3점 나옴"""
	answer = 0
	dic = dict()
	for e in clothes:
		if e[1] not in dic.keys():
			dic[str(e[1])] = {
				'lst': [e[0]],
				'above': False,
				'count': 1
			}
		else:
			dic[str(e[1])]['lst'].append(e[0])
			dic[str(e[1])]['count'] = len(dic[str(e[1])]['lst'])
			dic[str(e[1])]['above'] = True

	# 1번, 각 의상을 한번 씩 입는 수
	answer += len(clothes)
	# 2번 ~ n번까지
	exn = len(dic.keys())  # 전체 의상종류
	dpn = []  # 전체 의상 중 중복 되는 수
	for key in list(dic.keys()):
		if dic[key]['above']: dpn.append(dic[key]['count'])
	from math import factorial as fact
	for i in range(exn)[1:]:
		answer += fact(exn) / fact(i + 1) * fact(exn - (i + 1)) * sum(dpn)  # nCr * 중복수
	# print(i+1)  #2,3,4,5
	return int(answer)

print(solution2(clothesB))

def solution3(clothes):
	from collections import Counter as con
	answer = 1
	counter = con([value for _, value in clothes])
	for key in counter:
		answer *= (counter[key] + 1)
	return answer - 1


"""************************************"""
"""다른 사람 풀이"""
"""
https://itholic.github.io/kata-camouflage/
각 아이템에는 해당하는 카테고리가 있고,
카테고리별로 아이템을 한 개씩 조합해야 하는 문제이다.
단순히 생각하면 다음과같이 각 카테고리별 아이템 갯수를 구해서 다 곱하면 될 것 같다.
(모자의갯수) * (바지의갯수) * (안경의갯수)
하지만 이렇게하면 각 카테고리의 아이템이 “하나씩은 반드시 포함”되는 경우만 계산된다.
예를들어 모자는 쓰지 않고 바지만 입는다거나 하는 경우는 고려되지 않는다.
모자랑 안경만 쓰고 바지는 입지 않는 경우도 고려되지 않는다.
하지만 우리는 이러한 경우도 모두 고려해야한다.
따라서 각 카테고리별로 다음과 같이 “해당 카테고리의 아이템을 장착하지 않는 경우” 한개를 더 추가해서 계산해야한다.
(모자의갯수 + 1) * (바지의갯수 + 1) * (안경의갯수 + 1)
이렇게하면 특정 카테고리가 제외되는 경우까지 모두 고려된다.
하지만 여기서 끝내면 안된다.
스파이는 반드시 한 개의 아이템은 장착해야 하므로,
어떤 아이템도 장착하지 않는 한 개의 경우는 결과에서 빼줘야한다.
즉, 최종 계산은 다음과 같은 형태가 된다.
(모자의갯수 + 1) * (바지의갯수 + 1) * (안경의갯수 + 1) - 1
"""
from collections import Counter

def kata_solution(clothes):
	counter_each_category = Counter([cat for _, cat in clothes])
	all_possible = 1

	for key in counter_each_category:
		all_possible *= (counter_each_category[key] + 1)
	return all_possible - 1
