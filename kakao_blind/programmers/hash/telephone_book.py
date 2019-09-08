"""
start point = 2019.08.27
문제 : https://programmers.co.kr/learn/courses/30/lessons/42577
정답 : https://programmers.co.kr/learn/courses/30/lessons/42577/solution_groups?language=python3
포모도로 : 4개

전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.


"""

phone_book1 = ['119', '97674223', '1195524421']     # false
phone_book2 = ['123', '456', '789']                   # true
phone_book3 = ['12', '123', '1235', '567', '88']        # false


# case1 문자 지정해서 슬라이싱 하기
# 대상 번호의 문자 길이에 맞게 , 비교 대상을 길이에 맞게 리스트로 짤라 준다
# 대상 번호가 비교 대상 리스트에 들어가 있는지 확인
# 들어가 있으면 - false / 아니면 - true


# 1. 첫번쨰 요소의 길이를 구한다
length = len(phone_book2[0])   # 3

# 2. 다른 요소들을 첫번째 요소의 길이만큼으로 변형 한다.
for i in range(len(phone_book1)):
	phone_book2[i] = phone_book2[i][:length]
if phone_book2[0] in phone_book2[1:]:
	print('false')



def solution(phone_book):
	answer = True
	length = len(phone_book[0])

	for i in range(len(phone_book)):
		phone_book[i] = phone_book[i][:length]
	if phone_book[0] in phone_book[1:]: answer = False
	return answer


def case2_solution(phone_book):
	# case 2. 제일 작은 문자로 구분하기
	a = phone_book.copy()
	# 문자열 길이에 따라 sort 하기
	a = sorted(a, key=len)  # 이건 python3에서 사라졌다고 함

	# 비교 대상인(제일 문자열이 작은거) 를 따로 리스트로 넣기
	min_len = len(a[0])
	check_list = []
	for i in range(len(a)):
		if len(a[i]) == min_len:
			check_list.append(a[i])
	# a.remove(a[i])
	for c in check_list:
		a.remove(c)

	for i in range(len(a)):
		lst = []
		for n in range(round(len(a[i]) / min_len)):
			lst.append(a[i][min_len * n: min_len * (n + 1)])
		a.append(lst)

	a = a[int(len(a) / 2):]

	for check in check_list:
		for lst in a:
			if check in lst:
				answer = False
				break
	return answer

def rank1_solution(phoneBook):
	phoneBook = sorted(phoneBook)

	for p1, p2 in zip(phoneBook, phoneBook[1:]):        # about zip = https://wikidocs.net/32
		if p2.startswith(p1):
			return False
	return True

print(
	rank1_solution(phone_book1)
)

def rank2_solution(phoneBook):
	import re
	for b in phoneBook:
		p = re.compile("^"+b)
		for b2 in phoneBook:
			if b != b2 and p.match(b2):
				return False
	return True

print(rank2_solution(phone_book1))