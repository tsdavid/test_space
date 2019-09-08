lst = [[0, 0, 0, 0, 0, 0, 4, 0, 0, 0],  # x1 = 0
       [0, 0, 0, 0, 0, 4, 4, 0, 0, 0],  # x2 = 1
       [0, 0, 0, 0, 3, 9, 4, 0, 0, 0],  # x3 = 2
       [0, 0, 0, 2, 3, 9, 9, 0, 5, 5],  # x4 = 3
       [1, 2, 2, 2, 3, 3, 9, 0, 9, 5],  # x5 = 4
       [1, 1, 1, 9, 9, 9, 9, 0, 9, 5]]  # x6 = 5
	#  y1  y2 y3 y4 y5 y6 y7 y8 y9 y10
coordinate = [(6, 1), (6, 2), (6, 3)]
coordinate_type = 'lst'
# plus_candidate = [(5, 1), (5, 2), (5, 3)]
# minus_candidate = [(3, 1), (3, 2), (3, 3)]


plus_candidate = [(x + 1, y) for x, y in coordinate]
minus_candidate = [(x-1, y) for x, y in coordinate]

for candidate in [plus_candidate, minus_candidate]:
	for x,y in candidate:
		try:
			print(lst[x][y])
		except IndexError:
			print('this coordinate  is out of index :', x,y)

"""re write"""
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

"""make functional"""
# remove useless part
remove_index = 0
for borad in borads:
	if sum(borad) > 0:
		remove_index = borads.index(borad)
		break
borads = borads[remove_index:]

# use transform matrix for vertical part
import numpy as np
lst = borads.copy()
lst = np.array(lst).T

# mark the missing value
for l in lst:
	no_zero_list = np.where(l)[0]
	if len(no_zero_list) != 0:
		for i in range(len(l)):
			if i > no_zero_list[0]:
				if l[i] == 0: l[i] = 9
			else:pass
	else:pass
lst = lst.T

# save coordinate data in dic which is dictionary separate with vertical and horizontal case
dic = dict()
dic['lst'] = dict()
dic['lst.T'] = dict()

# case horizontal
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

# case vertical
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

# make candidate plus and minus candidate
for key in dic.keys():
	for case in dic[key]:
		for target_num in case:
			print('target_number: ', target_num)
			coordinate = dic[key][target_num]
			# make candidate coordinate
			if target_num in list(dic['lst']):  # case horizontal
				plus_candidate = [(x+1, y)for x, y in coordinate]
				minus_candidate = [(x-1, y)for x, y in coordinate]

			if target_num in list(dic['lst.T']): # case vertical
				plus_candidate = [(x, y+1) for x, y in coordinate]
				minus_candidate = [(x, y-1) for x, y in coordinate]
			# check candidate coordinate
			for candidate in [plus_candidate, minus_candidate]:
				print('candidate coordiante: ', candidate)
				from collections import Counter
				try:
					count_candidate = Counter([lst[c[0]][c[1]] for c in candidate])
					# condition
					if [0, target_num] == sorted(list(count_candidate)) and	count_candidate[0] == 2:
						print('we can eliminate it', 'original_coordinate', coordinate, 'target number: ', target_num)
				except IndexError as e:
					print(e, ' Occur, need to pass')
					pass
