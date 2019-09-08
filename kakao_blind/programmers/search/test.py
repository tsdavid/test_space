"""
start point = 2019-08-29
문제 = https://programmers.co.kr/learn/courses/30/lessons/42840
정답 =
포모도로 = 2

문제 설명
수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다. 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때, 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한 조건
시험은 최대 10,000 문제로 구성되어있습니다.
문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.
입출력 예
answers	return
[1,2,3,4,5]	[1]
[1,3,2,4,2]	[1,2,3]
입출력 예 설명
입출력 예 #1

수포자 1은 모든 문제를 맞혔습니다.
수포자 2는 모든 문제를 틀렸습니다.
수포자 3은 모든 문제를 틀렸습니다.
따라서 가장 문제를 많이 맞힌 사람은 수포자 1입니다.

입출력 예 #2

모든 사람이 2문제씩을 맞췄습니다.

https://itholic.github.io/kata-supo/
로직은 대충 비슷한거 같은데 마감처리가 부실한건가 왜 다  틀릴까
다른 사람들은 문제를 풀면서 찾아보는데 난 그냥 생각만해서 그런가
나도 찾아보면서 문제를 풀어야겠어
괜히 지금 연습문제 말고 모의고사를 다시 풀고싶은 내 생각을 뭘까


"""

answersA = [1, 2, 3, 4, 5]
returnA = [1]

answersB = [1, 3, 2, 4, 2]
returnB = [1, 2, 3]

max_number = 10000

# correct default = 0
# [[index, correct, answer_sheet], ]

answer = []

first = [1, 2, 3, 4, 5]     # 5개 , 2000개
second = [2, 1, 2, 3, 2, 4, 2, 5]   # 8개 , 1250개
third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 10개 , 1000개

targets = []
for e in enumerate([first, second, third]):
	targets.append([e[0], 0, e[1]])
# targets = [[index, correct, answer_sheet], ]

# 문제 길이 맞추기, 만약 문제가 100개라면, 문제보다 정답을 더 많게해서 문제에 전체 답을 할수 있게, 정답이 남으면 처리하면됨
number = len(answersA)
first = first*int(number/len(first) + 1)

# 문제 전체를 돌면서 정답과 맞춰보고 맞으면 리스트에 저장
# 결과를 저장
for target in targets:
	correct = 0
	for i in range(len(target[2])):
		try:
			if answersA[i] == target[2][i]:
				correct += 1
		except IndexError:
			pass
	target[1] = correct
	if correct == 0:
		target[0] = -1

# 순서 산출
# 하나도 못 맞추면 리스트에 저장하지 않음
targets = sorted(targets, key = lambda target: target[1], reverse=True)

for target in targets:
	if target[0] < 0: pass
	else:answer.append(target[1])





def solution(answers):
	"""점수 = 28.6"""
	answer = []

	first, second, third = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

	# 문제 길이 맞추기, 만약 문제가 100개라면, 문제보다 정답을 더 많게해서 문제에 전체 답을 할수 있게, 정답이 남으면 처리하면됨

	main_targets = [[lst[0] + 1, 0, lst[1], int(len(answers) / len(lst[1])) + 1] for lst in enumerate([first, second, third])]
	# targets = [[index, correct, answer_sheet, 정답 길이에 따라 늘어나야할 답안지 수], ]

	# 문제 전체를 돌면서 정답과 맞춰보고 맞으면 리스트에 저장
	# 결과를 저장
	for target in main_targets:
		correct = 0
		answer_sheet = target[2] * target[3]
		for seq in range(len(answer_sheet)):
			try:
				if answers[seq] == answer_sheet[seq]:
					correct += 1
			except IndexError:
				break
		target[1] = correct
		if correct == 0:
			target[0] = -1

	# 순서 산출
	# 하나도 못 맞추면 리스트에 저장하지 않음
	# main_targets = sorted(main_targets, key=lambda target: (target[1], -target[0]), reverse=True)

	for target in sorted(main_targets, key=lambda target: (target[1], -target[0]), reverse=True):
		if target[0] < 0:
			pass
		else:
			answer.append(target[0])
	return answer

