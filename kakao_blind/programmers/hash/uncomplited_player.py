"""
문제 : https://programmers.co.kr/learn/courses/30/lessons/42576
정답 : https://programmers.co.kr/learn/courses/30/lessons/42576/solution_groups?language=python3

start_point = 2019-08-23 14:10
fomorodo =

수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와
완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,

완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

제한사항
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.


"""
# participant2 = ["marina", "josipa", nikola, vinko, filipa]
# completion2 =

participant3 = ["mislav", "stanko", "mislav", "ana"]
completion3 = ["stanko", "ana", "mislav"]

# 참가자 중에 완료가 있으면 pop
# participant에 1명이 남으면 break 하고 return


def solution(participant, completion):
	answer = ''
	for player in completion:
		if player in participant:
			participant.remove(player)
	answer = participant[0]
	return answer

print(solution(participant3, completion3))


"""***********************************"""
"""solution from 
https://dreamhollic.tistory.com/entry/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4-10-%EC%99%84%EC%A3%BC%ED%95%98%EC%A7%80-%EB%AA%BB%ED%95%9C-%EC%84%A0%EC%88%98-JAVA
"""
from operator import eq
# about operator = https://docs.python.org/3/library/operator.html
def dream_solution(participant, completion):
	answer = ''
	participant.sort()
	completion.sort()
	flag = True

	for i in range(len(completion)):
		if not eq(participant[i], completion[i]):
			answer = participant[i]
			flag = False
			break
	if flag:
		answer = participant[len(participant) - 1]

	return answer

print(dream_solution(participant3, completion3))
""" 평가
각 리스트를 sort해서 알파벳으로 만든거같은데
이 방법이 안전한 걸까? 알파벳 순서가 다를 수도 있지 않나

"""


def other_solution(participant, completion):
	import collections
	# about collections = https://docs.python.org/3/library/collections.html?highlight=collections#module-collections
	answer = collections.Counter(participant) - collections.Counter(completion)
	return list(answer.keys())[0]

print(other_solution(participant3, completion3))