"""
start time = 2019-08-21 11:40

problem = 원인은 신규 사용자와 기존 사용자 사이에 스테이지 차이가 너무 큰 것이 문제였다. - 실패율을 구해라
실패율이란 - 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
			전체 플레이어 수 중 - 스테이지에 도달하지 못한 플레이어 = 스테이지에 도달한 플레이어 수
			스테이지에 도달한 플레이어 수  = (도달 함) 클리어 못함 + (도달 함) 클리어 함

NOTATION =	N = 전체 스테이지의 개수
			stages = 플레이어가 현재 멈춰있는 스테이지의 번호가 담긴 배열

Return = 실패율이 높은 스테이지 부터 내림차순으로 스테이지의 번호가 담겨있는 배열

단, N + 1 은 마지막 스테이지(N 번째 스테이지) 까지 클리어 한 사용자를 나타낸다.
스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다

(5, [2, 1, 2, 6, 2, 4, 3, 3]) -> [3,4,2,1,5]
(4, [4,4,4,4,4]	) -> 	[4,1,2,3]
"""

"""
case study #1
(5, [2, 1, 2, 6, 2, 4, 3, 3]) -> [3,4,2,1,5]

총 스테이지는 5개
1번 스테이지 : 1 -> 1/8 = 0.125
2번 스테이지 : 3 -> 3/7 = 0.428
3번 스테이지 : 2 -> 2/4 = 0.5
4번 스테이지 : 1 -> 1/2 = 0.5
5번 스테이지 : 0 -> 0/1   = 0
모두 클리어  : 1 -> 1   = 무시
전체 플레이어 수, 플레이어가
"""

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
# [1, 2, 2, 2, 3, 3, 4, 6]

N1 = 4
stages1 = [4, 4, 4, 4, 4]

answer = []
stage_info = dict()
for stage in range(N):
	current_stage = stage + 1
	# save info about fail rate
	stage_info[str(current_stage)] = stages.count(current_stage) / len(stages)

	# remove used players
	for i in range(stages.count(current_stage)):
		stages.remove(current_stage)

# 정리
list = []
for item in stage_info.items():
	item = tuple(reversed(item))
	list.append(item)
list.sort(reverse=True)

for i in range(N):
	try:
		if list[i][0] == list[i + 1][0] and int(list[i][1]) > int(list[i + 1][1]):
			list.insert(i + 1, list.pop(i))  # 리스트에서 위치 바꾸기.
	except IndexError:
		pass


def solution(N, stages):
	answer = []
	stage_info = dict()
	for stage in range(N):
		current_stage = stage + 1
		# save info about fail rate
		stage_info[str(current_stage)] = stages.count(current_stage) / len(stages)

		# remove used players
		for i in range(stages.count(current_stage)):
			stages.remove(current_stage)

	# 정리
	list = []
	for item in stage_info.items():
		item = tuple(reversed(item))
		list.append(item)
	list.sort(reverse=True)

	for i in range(N):
		try:
			if list[i][0] == list[i + 1][0] and int(list[i][1]) > int(list[i + 1][1]):
				list.insert(i + 1, list.pop(i))  # 리스트에서 위치 바꾸기.
		except IndexError:
			pass

	for i in list:
		answer.append(i[1])

	return answer


print("me: ", solution(N, stages), "\n", "label: [3,4,2,1,5]")
print("me :", solution(N1, stages1), "\n", "label: [4,1,2,3]")

"""
마지막
print("me :", solution(N1, stages1), "\n", "label: [4,1,2,3]")
여기에서 실패율이 같을 떄, 인덱스 작은 순으로 하는 거에서 막힘
나는 2개씩만 비교했는데, 문제는 3개를 비교해야 함.
내가 개 털림
https://geonlee.tistory.com/57
정답을 보니까 함수를 썼는데
처음 보는 함수임
다음에 해당 함수 먼저 공부해야 할듯
일단 오늘은 이걸로 마무리 
1차 마무리 = 2019.08.21 18:51
1차 사용한 포모도로 개수 = 5개

"""
solution_from = "https://github.com/ChungminPark/_problem_solving/blob/master/KakaoBlind2019/KakaoBlind2019-2.py"


def answer_solution(N, stages):
	answer = []
	num_user = len(stages)  # 도전한 사용자 수
	stage = [0] * (N + 1)  # 스테이지에 도달했지만, 클리어하지 못한 사용자 수 -> 이해가 안됨
	num_hitted_user = num_user  # 스테이지에 도달한 사용자 수
	failure_rate = [0] * N  # 실패율: 스테이지에 도달했으나 아직 클리어 하지 못한 사용자 수 / 스테이지에 도달한 사용자 수

	for i in stages:
		stage[i - 1] += 1  # 각 스테이지 별 도전 중인 사용자 수 = [1, 3, 2, 1, 0, 1]


