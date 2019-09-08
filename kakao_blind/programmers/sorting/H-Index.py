"""
strat point = 2019-08-29
문제 = https://programmers.co.kr/learn/courses/30/lessons/42747
정답 =
포모도로 = 3

문제 설명
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다.
위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h가 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때, 이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

제한사항
과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
논문별 인용 횟수는 0회 이상 10,000회 이하입니다.
입출력 예
citations	    return
[3, 0, 6, 1, 5]	3
입출력 예 설명
이 과학자가 발표한 논문의 수는 5편이고, 그중 3편의 논문은 3회 이상 인용되었습니다.
그리고 나머지 2편의 논문은 3회 이하 인용되었기 때문에 이 과학자의 H-Index는 3입니다.


풀이를 봐도 이해가 안됨..
이 문제는 skip해야할듯
참고 문서 = https://itholic.github.io/kata-h-index/
"""

citations = [3, 0, 6, 1,  5]
returnA = 3


answer = 0
from math import trunc
lst = citations.copy()
# lst를 내림차순 정렬을 하고
lst = sorted(lst)
length = len(lst)
candidates = []
# h가 가능할 만한 후보군을 찾기 - 대게 중앙에 속한 값이라고 판단,
# 우선 후보군 : 중앙에 위치한 값 들
# list is odd -float
if length % 2 != 0:
	candidates.append(lst[trunc(length/2)]-1)
# list is even - int
elif length % 2 == 0:
	for e in [lst[int(length/2) -1], lst[int(length/2)]]:candidates.append(e)


# 해당 후보군이 아니라면, 점점 밖으로 넓혀감감

# h를 찾는 루프
def positive(x, y): return x >= y


def detect_h(candidates, answer):
	for candidate in candidates:
		fits = []
		for e in lst:
			fits.append(positive(e, candidate))
		pred_h = fits.count(True)
		if pred_h == candidate:
			answer += pred_h
			break
	return answer

def upload_candidate(candidates, lst):
	if len(candidates) == 1:
		index = lst.index(candidates[0])
		try:
			candidates = [e for e in [lst[index - 1], lst[index + 1]]]
		except IndexError: pass

	elif len(candidates) == 2:
		try:
			candidates[0] = lst[lst.index(candidates[0]) - 1]
			candidates[1] = lst[lst.index(candidates[0]) + 1]
		except IndexError: pass

while True:
	if detect_h(candidates, answer):
		print(answer)
		break
	upload_candidate(candidates, lst)
print(answer)
# 후보군에 h가 없으면
# 후보군을 이니시얼 하고 후보군을 다시 찾음

def solution(citations):
	"""점수 = 6.3"""
	from math import trunc
	answer = 0
	lst = citations.copy()
	lst = sorted(lst)
	length = len(lst)
	candidates = []

	if length % 2 != 0:
		candidates.append(lst[trunc(length / 2)])
	# list is even - int
	elif length % 2 == 0:
		for e in [lst[int(length / 2) - 1], lst[int(length / 2)]]:
			candidates.append(e)

	def update_candidate(candidates, lst):
		if len(candidates) == 1:
			index = lst.index(candidates[0])
			try:
				candidates = [e for e in [lst[index - 1], lst[index + 1]]]
			except IndexError:
				pass
		elif len(candidates) == 2:
			forward_index, backward_index = lst.index(candidates[0]) - 1, lst.index(candidates[1]) + 1
			candidates = []
			try:
				candidates = [lst[i] for i in [forward_index, backward_index]]
			except IndexError:
				pass
		return candidates

	while True:
		for candidate in candidates:
			fits = [element >= candidate for element in lst]
			trues = fits.count(True)
			fales = fits.count(False)
			if trues >= candidate and fales <= candidate:
				answer += candidate
				break
		break
		candidates = update_candidate(candidates, lst)

	return answer
