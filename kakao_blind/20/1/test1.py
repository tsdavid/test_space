"""


"""

s = ["aabbaccc",                # 8
     "ababcdcdababcdcd",        # 16
     "abcabcdede",              # 10
     "abcabcabcabcdededededede",# 24
	 "xababcdcdababcdcd"        # 17
     ]
results = [7, 9, 8, 14, 17]


# 2, len(st) = 16
st = "ababcdcdababcdcd"

# pivot, p는 테스트하는 구분 수, p need update
# p = int(len(st)/2)

# 구분 range = p 만큼 씩 증가, 전체 범위 돌릴 수 있는 횟수는 len(st) / p 의 반내림,
# 나머지는 나머지 그냥 뒤에 붙여줌
# max_iter = len(st)/p
import math
# math.floor() 내림 사용
# max_iter = math.floor(len(st) / p)



# 일단 정답 맞추기
p = 8
max_iter = 2
# 후보 리스트 만들기 c_list = max_iter만큼 p범위로 늘려진것
c_list = [st[p*i:p*(i+1)] for i in range(int(max_iter)+1)]
lst = c_list.copy()
# 각 element 끼리 비교하기
# if lst[0] == lst[1] if true -> lst[1] ==lst[2]


same_list = []
while True:
	i = 0
	time = 1
	if lst[i] == lst[i+1]:
		print('True', time, i)
	else:
		print(
			'False',
			str(time) + lst[i]
		)
		break
	time += 1
	i += 1


for i in range(len(lst)):
	while True:
		time = 0
		if lst[i] == lst[i+1]:
			print(lst[i],'it is same')
			time += 1




# 일단 정답 맞추기
p = 2
max_iter = len(st)/p
# 후보 리스트 만들기 c_list = max_iter만큼 p범위로 늘려진것
c_list = [st[p*i:p*(i+1)] for i in range(int(max_iter)+1)]
lst = c_list.copy()
# 각 element 끼리 비교하기
# if lst[0] == lst[1] if true -> lst[1] ==lst[2]

same_list = []
while True:
	time = 1
	try:
		for i in range(len(lst)):
			if lst[i] == lst[i + 1]:
				print(lst[i], 'it is same')
				time += 1

			else:
				break
		lst = lst[i:]
		print('not same')
		target = str(time) + lst[i]
		same_list.append(target)
		break

	except IndexError:
		break




s = ["aabbaccc",                # 8
     "ababcdcdababcdcd",        # 16
     "abcabcdede",              # 10
     "abcabcabcabcdededededede",# 24
	 "xababcdcdababcdcd"        # 17
     ]
results = [7, 9, 8, 14, 17]

text = "ababcdcdababcdcd"
p = 8



max_iter = len(text) / p
c_list = [text[p * i:p * (i + 1)] for i in range(int(max_iter) + 1)]
lst = c_list.copy()
same_list=[]
while True:
	try:
		count = 1
		i = 0
		while True:
			if lst[i] == lst[i+1]:
				count += 1
				i += 1
			else:
				print(
					'i: ', i,
					'count: ', count
				)
				element = lst[i]
				lst = lst[i + 1:]
				print(lst)
				break
		if count == 1:
			target = element
		else:
			target = str(count) + element
		same_list.append(target)
		print(same_list)
	except IndexError:

		if count == 1 or len(lst[0]) < p:
			target = lst[0]
		else:
			target = str(count) + lst[0]
		same_list.append(target)
		print(same_list)
		break
a = ''.join(same_list)
print(len(a))



def compare(text, p):
	max_iter = len(text) / p
	c_list = [text[p * i:p * (i + 1)] for i in range(int(max_iter) + 1)]
	lst = c_list.copy()
	same_list = []
	while True:
		try:
			count = 1
			i = 0
			while True:
				if lst[i] == lst[i + 1]:
					count += 1
					i += 1
				else:
					print(
						'i: ', i,
						'count: ', count
					)
					element = lst[i]
					lst = lst[i + 1:]
					print(lst)
					break
			if count == 1:
				target = element
			else:
				target = str(count) + element
			same_list.append(target)
			print(same_list)
		except IndexError:

			if count == 1 or len(lst[0]) < p:
				target = lst[0]
			else:
				target = str(count) + lst[0]
			same_list.append(target)
			print(same_list)
			break

	return ''.join(same_list)



def solution(s):
    answer_list=[]
    for p in range(len(s)):
        answer_list.append(len(compare(s,p+1)))
    return min(answer_list)