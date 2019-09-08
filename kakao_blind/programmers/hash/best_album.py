"""
start point = 2019.08.28
문제 = https://programmers.co.kr/learn/courses/30/lessons/42579?language=python3
정답 = https://programmers.co.kr/learn/courses/30/lessons/42579/solution_groups?language=python3
포모도로 = 4

문제 설명
스트리밍 사이트에서 장르 별로 가장 많이 재생된 노래를 두 개씩 모아 베스트 앨범을 출시하려 합니다. 노래는 고유 번호로 구분하며, 노래를 수록하는 기준은 다음과 같습니다.

속한 노래가 많이 재생된 장르를 먼저 수록합니다.(장르 우선)
장르 내에서 많이 재생된 노래를 먼저 수록합니다.(재생 순)
장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.(번호 순)
2개씩 앨범에 넣음

노래의 장르를 나타내는 문자열 배열 genres와 노래별 재생 횟수를 나타내는 정수 배열 plays가 주어질 때,
베스트 앨범에 들어갈 노래의 고유 번호를 순서대로 return 하도록 solution 함수를 완성하세요.

제한사항
genres[i]는 고유번호가 i인 노래의 장르입니다.,  i = 고유번호
plays[i]는 고유번호가 i인 노래가 재생된 횟수입니다.
genres와 plays의 길이는 같으며, 이는 1 이상 10,000 이하입니다.
장르 종류는 100개 미만입니다.
장르에 속한 곡이 하나라면, 하나의 곡만 선택합니다.
모든 장르는 재생된 횟수가 다릅니다.

입출력 예
genres	                                plays	                    return
[classic, pop, classic, classic, pop]	[500, 600, 150, 800, 2500]	[4, 1, 3, 0]
입출력 예 설명
classic 장르는 1,450회 재생되었으며, classic 노래는 다음과 같습니다.

고유 번호 3: 800회 재생
고유 번호 0: 500회 재생
고유 번호 2: 150회 재생
pop 장르는 3,100회 재생되었으며, pop 노래는 다음과 같습니다.

고유 번호 4: 2,500회 재생
고유 번호 1: 600회 재생
따라서 pop 장르의 [4, 1]번 노래를 먼저, classic 장르의 [3, 0]번 노래를 그다음에 수록합니다.

(장르, 재생 수, 고유번호)

*************************
로직은 대충 맞았는데 리스트 다중 정렬하는게 문제였음
"""
genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = [500, 600, 150, 800, 2500]
returns = [4, 1, 3, 0]

from collections import Counter
# 장르비교
answer = []
genre_dic = dict()
for i in range(len(genres)):
	if genres[i] not in list(genre_dic.keys()):
		genre_dic[str(genres[i])] = plays[i]
	else:
		genre_dic[str(genres[i])] += plays[i]       # {'classic': 1450, 'pop': 3100}

priority = [(play, genre) for genre, play in genre_dic.items()]     # [(1450, 'classic'), (3100, 'pop')]
priority.sort(reverse=True)     # [(3100, 'pop'), (1450, 'classic')]
for i in range(len(priority)):priority[i] = priority[i][1]      # ['pop', 'classic']



target_list = [(v, plays[k], k) for k, v in enumerate(genres)]
# [('classic', 500, 0), ('pop', 600, 1), ('classic', 150, 2), ('classic', 800, 3), ('pop', 2500, 4)]

# 재생수 비교
for p in priority:
	lst = []
	for e in target_list:
		if p == e[0]:
			lst.append([e[1], e[2]])    # [[800, 3], [500, 0], [150, 2]]
	lst.sort(reverse=True)
	# 리스트가 2보다 작은 경우
	if len(lst) <= 2:pass
	else: lst = lst[:2]

	if lst[0] == lst[1]:
		for i in range(len(lst)):
			lst[i] = lst[i][1]
		lst.sort()
		for l in lst: answer.append(lst[0])
	else:
		for i in lst[:2]:
			answer.append(i[1])

print(answer)



def solution1(genres, plays):
	"""점수 = 86.7
	2차 점수 = 53.3
	"""
	answer = []
	genre_dic = dict()
	for i in range(len(genres)):
		if genres[i] not in list(genre_dic.keys()):
			genre_dic[str(genres[i])] = plays[i]
		else:
			genre_dic[str(genres[i])] += plays[i]
	# genre_dic = {'classic': 1450, 'pop': 3100}

	priority = [(play, genre) for genre, play in genre_dic.items()]  # [(1450, 'classic'), (3100, 'pop')]
	priority.sort(reverse=True)  # [(3100, 'pop'), (1450, 'classic')]
	for i in range(len(priority)): priority[i] = priority[i][1]
	# priority = ['pop', 'classic']

	target_list = [(v, plays[k], k) for k, v in enumerate(genres)]
	# (장르, 재생 수, 고유번호)
	# target_list = [('classic', 500, 0), ('pop', 600, 1), ('classic', 150, 2), ('classic', 800, 3), ('pop', 2500, 4)]

	# 재생수 비교
	for p in priority:  # pop or classic
		lst = []
		for e in target_list:
			if p == e[0]:   # pop == pop?
				lst.append([e[1], e[2]])  # [[800, 3], [500, 0], [150, 2]]
		lst.sort(reverse=True)  # sort by plays in pop or classic list
		# 리스트가 2보다 작은 경우
		if len(lst) > 2: lst = lst[:2]
		# lst = [[800, 3], [150, 2]]

		# 고유번호 비교
		if lst[0][0] == lst[1][0]:  # if play same?
			for i in range(len(lst)):lst[i] = lst[i][1]     # [3, 2]
			lst.sort()  # [2, 3]
			for l in lst: answer.append(l)
		else:   # play not same!
			for i in lst:
				answer.append(i[1])
	return answer


def retry_solution(genres, plays):
	"""점수 = 100"""
	answer = []

	# 장르 우선순위를 만든다
	dic = dict()
	for genre, play in zip(genres, plays):
		if genre not in dic.keys():
			dic[genre] = play
		else:
			dic[genre] += play
	# {'classic': 1450, 'pop': 3100}

	genre_ranking = [(play, genre) for genre, play in dic.items()]
	genre_ranking.sort(reverse=True)
	for i in range(len(genre_ranking)):
		genre_ranking[i] = genre_ranking[i][1]
	# ['pop', 'classic']

	# [장르, 재생수, 고유번호]로 리스트를 만든다
	targets = [[genre, plays[index], index] for index, genre in enumerate(genres)]
	# [['classic', 500, 0], ['pop', 600, 1], ['classic', 150, 2], ['classic', 800, 3], ['pop', 2500, 4]]

	# 장르 우선순위 안에서 위에서 만든 리스트를 살펴본다
	for rank in genre_ranking:  # 1: pop, 2: classic
		lst = []
		# 같이 장르끼리 묶은다음에
		for target in targets:
			if target[0] == rank:
				lst.append(target[1:])  # 장르끼리 모으니까 장르는 필요없음, 재생수와 고유번호만 필요
		# 재생 순으로 만들고
		lst.sort(reverse=True)  # 재생 순 높은 쪽이 앞쪽으로
		# 파이썬 리스트 다중 조건 = https://dailyheumsi.tistory.com/67
		lst = sorted(lst, key=lambda x: (x[0], -x[1]), reverse=True)
		# lambda를 이용하면 원하는 키로 넣을 수 있다. -를 붙이면 기존 방향에서 반대로 시행

		# 2개로 슬라이싱 하고 - 2개 이하 일때, 예외
		if len(lst) <= 2:
			pass
		else:
			lst = lst[:2]
		for e in lst:
			answer.append(e[1])
	return answer
"""
way to make it short

for genre, play in zip(genres, plays):print(genre, play)  # classic 500
genre_type = list(dict.fromkeys(genres))    # ['classic', 'pop']    
--way to remove duplicate in list = https://www.w3schools.com/python/python_howto_remove_duplicates.asp
"""

"""others' solution"""
"""solution from 
=https://itholic.github.io/kata-best-album/
"""


from collections import defaultdict
from operator import itemgetter

# def solution(genres, plays):

genre_play_dict = defaultdict(lambda: 0)
for genre, play in zip(genres, plays):
	genre_play_dict[genre] += play
# what is defaultdict, how it works

genre_rank = [genre for genre, play in sorted(genre_play_dict.items(), key=itemgetter(1), reverse=True)]