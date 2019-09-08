"""
문제를 푼다는 것 보다, 해답을 보고 문제 푸는 방법을 공부해보자
start point = 2019-08-30
문제 = https://www.welcomekakao.com/learn/courses/30/lessons/42894
정답 =

*문제설명

"""
#         0  1  2  3  4  5  6  7  8  9
borads = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
         [0, 0, 0, 0, 0, 4, 4, 0, 0, 0],
         [0, 0, 0, 0, 3, 0, 4, 0, 0, 0],
         [0, 0, 0, 2, 3, 0, 0, 0, 5, 5],
         [1, 2, 2, 2, 3, 3, 0, 0, 0, 5],
         [1, 1, 1, 0, 0, 0, 0, 0, 0, 5]]

#         0  1  2  3  4  5  6  7  8  9
# borade = [[0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
#           [0, 0, 0, 0, 0, 4, 4, 0, 0, 0],
#           [0, 0, 0, 0, 3, 9, 4, 0, 0, 0],
#           [0, 0, 0, 2, 3, 9, 9, 0, 5, 5],
#           [1, 2, 2, 2, 3, 3, 9, 0, 9, 5],
#           [1, 1, 1, 9, 9, 9, 9, 0, 9, 5]]

# 앞에서 0인 부분들은 없애고 0이 아닌 부분이 나오면 break
remove_index = 0
for borad in borads:
	if sum(borad) > 0:
		remove_index = borads.index(borad)
		break
borads = borads[remove_index:]

# 결측값 설정하기 - 세로로 비교하기 어려우니까 전치행렬로 바꿔서 좌우로 비교
# 왼쪽에서 오른쪽으로 가는데
# 0이 아닌 숫자가 발생한 후에 다음 숫자가 0이면 결측치
import numpy as np
lst = borads.copy()
lst = np.array(lst).T

# lst
# array([[0, 0, 0, 0, 1, 1],
#        [0, 0, 0, 0, 2, 1],
#        [0, 0, 0, 0, 2, 1],
#        [0, 0, 0, 2, 2, 0],
#        [0, 0, 3, 3, 3, 0],
#        [0, 4, 0, 0, 3, 0],
#        [4, 4, 4, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 5, 0, 0],
#        [0, 0, 0, 5, 5, 5]])

for l in lst:
	no_zero_list = np.where(l)[0]
	if len(no_zero_list) != 0:
		for i in range(len(l)):
			if i > no_zero_list[0]:
				if l[i] == 0: l[i] = 9
			else:pass
	else:pass

#결측치 설정 후 다시 전치행렬로 원래 행렬로 돌아오기
# lst.T
# array([[0, 0, 0, 0, 0, 0, 4, 0, 0, 0],
#        [0, 0, 0, 0, 0, 4, 4, 0, 0, 0],
#        [0, 0, 0, 0, 3, 9, 4, 0, 0, 0],
#        [0, 0, 0, 2, 3, 9, 9, 0, 5, 5],
#        [1, 2, 2, 2, 3, 3, 9, 0, 9, 5],
#        [1, 1, 1, 9, 9, 9, 9, 0, 1, 5]])

lst = lst.T
# 연속 3개인(가로,세로) 경우의 좌표 3개를 구한다.

# 가로 연속3개 좌표 찾기
for l in enumerate(lst):
	print('y= ',l[0])
	for i in range(1, len(l), 1):
		if l[i] != 0 & l[i] != 9:
			if l[i-1] == l[i] == l[i+1]:
				print('x=', i)


l = lst[-1]
true_list = np.where(l == 1)[0]
# l == 1 => [True, T1rue, True, False, False ..]
# (array([0, 1, 2, 8], dtype=int64),)

# 연속 수 인걸 확인해야 한다.
for i in range(len(true_list)):
	try:
		if int(true_list[i]) + 1 == int(true_list[i + 1]) and \
				int(true_list[i]+1) + 1 == int(true_list[i + 2]):
			print("this is succession number")
	except:
		pass


# save the point in the dict
dic = dict()
dic['lst'] = dict()
dic['lst.T'] = dict()
# lst = 가로 경우
for l in enumerate(lst):
	y = l[0]
	for num in [1, 2, 3, 4, 5]:
		true_list = np.where(l[1] == num)[0]
		for i in range(len(true_list)):
			try:
				if int(true_list[i]) + 1 == int(true_list[i + 1]) and \
						int(true_list[i] + 1) + 1 == int(true_list[i + 2]):
					xs = [true_list[i], true_list[i+1], true_list[i+2]]
					dic['lst'][str(num)] = [(y, x) for x in xs]
			except:pass

# lst.T = 세로 경우
for l in enumerate(lst.T):
	x = l[0]
	for num in [1, 2, 3, 4, 5]:
		true_list = np.where(l[1] == num)[0]
		for i in range(len(true_list)):
			try:
				if int(true_list[i]) + 1 == int(true_list[i + 1]) and \
						int(true_list[i] + 1) + 1 == int(true_list[i + 2]):
					ys = [true_list[i], true_list[i+1], true_list[i+2]]
					dic['lst.T'][str(num)] = [(y, x) for y in ys]
			except:pass



"""
{'lst': 
{
'2': [(1, 4), (2, 4), (3, 4)], 
'1': [(0, 5), (1, 5), (2, 5)]
}, 

'lst.T': 
{
'3': [(2, 4), (3, 4), (4, 4)], 
'4': [(0, 6), (1, 6), (2, 6)], 
'5': [(3, 9), (4, 9), (5, 9)]
}
}

"""



"""
소거 가능한걸 찾기
1. 세로일 때와 가로일때 축이 다름
2. 한 축으로 위 아래 또는 좌우를 찾는다
3. 3자리 중 0이 2개 그리고 해당 숫자가 1개 있으면 해당 숫자를 0에 채워넣는다
4. 3개 2줄을 만들면 0으로 바꾼다
5. result + 1

1. 2번으로 다시간다
2. update 가 없으면 result 를 return 한다


for data in [dic['lst'], dic['lst.T']]:
	if data == dic['lst']: print(True)
"""
for data in [dic['lst'], dic['lst.T']]:
	for target_num in list(data.keys()):
		# data = dic['lst']
		# target_num = list(data.keys())[0]
		coordinate = data[target_num]
		# lst 니까 x 부분에 +-1로 같은걸 찾는다, 후보 좌표를 찾는다.
		# if data == dic['lst']:
		# 	if len(lst[0]) > x+1:
		# 		plus_candidate = [0]
		# 	else:
		# 		plus_candidate = [(x+1, y) for x, y in coordinate]
		# 	minus_candidate = [(x-1, y) for x, y in coordinate]
		# else:
		# 	plus_candidate = [(x, y+1) for x, y in coordinate]
		# 	minus_candidate = [(x, y-1) for x, y in coordinate]

		plus_candidate, minus_candidate = [], []
		for x, y in coordinate:
			if data == dic['lst.T']: # y가 변동 , y = len(lst[0])
				print('dic[lst.T]', data)
			# 	if len(lst[0]) < y + 1:
			# 		plus_candidate = [0]
			# 	else:
			# 		plus_candidate.append((x,y+1))
			# 	if len(lst[0]) > y - 1:
			# 		minus_candidate = [0]
			# 	else:
			# 		minus_candidate.append((x, y-1))

			elif data == dic['lst']: # x가 변동 , x = len(lst)
				print('dic[kst]', data)
				# if len(lst) < x +1:
				# 	plus_candidate = [0]
				# else:
				# 	plus_candidate.append((x+1, y))
				# if len(lst) > x - 1:
				# 	minus_candidate = [0]
				# else:
				# 	minus_candidate.append((x-1, y))
				#



		# 후보 좌표 중에서 소거 가능한 좌표를 찾는다.
		for c in [plus_candidate, minus_candidate]:
			if len(c) == 1:
				print('pssing c')
				pass
			else:
				print(c)
				from collections import Counter
				count_candidate = Counter([lst[x-1][y-1] for x, y in c])
				# Counter({9: 2, 3: 1})
				# 문자와 갯수 비교
				if [0, target_num] == sorted(list(count_candidate)) and count_candidate[0] == 2:
					print("we can remove it: ", 'plus or  minus: ', c, 'original_coordinate: ', coordinate, 'target_num: ', target_num)
				else:
					print("we can't ;;")








# 까만 블록이 내려올 수 없는 곳을 9로 결측치 -> 결측치 검색 - update가 필요하니까 함수로 진행
# 요소가 가로 또는 세로로 3개가 연속이 부분을 찾는다 -> 후보 검사 - update 필요, 함수화
# 가로 3개 연속일 때, 좌 우 3개를 검색 -> 0 또는 자기 요소가 아닌 (9 또는 다른 수) 가 있다면 fail -> 정답 확인
# 세로 3개 연속일 때, 위 아래 3개를 검색 -> 0 또는 자기 요소가 아닌 (9 또는 다른 수) 가 있다면 fail

# 결측치 검사 -> 후보 검사 -> 정답확인 ->

