"""
후보키(Candidate Key) = 관계 데이터베이스에서 릴레이션(Relation)의 튜플(Tuple)을 유일하게 식별할 수 있는 속성(Attribute)
						또는 속성의 집합 중, 다음 두 성질을 만족하는 것
					속성 :
						유일성(uniqueness) : 릴레이션에 있는 모든 튜플에 대해 유일하게 식별되어야 한다.
						최소성(minimality) : 유일성을 가진 키를 구성하는 속성(Attribute) 중 하나라도 제외하는 경우 유일성이 깨지는 것을 의미한다.
											즉, 릴레이션의 모든 튜플을 유일하게 식별하는 데 꼭 필요한 속성들로만 구성되어야 한다.

[
 "학번","이름", "전공", "학년",
["100","ryan","music","2"],
["200","apeach","math","2"],
["300","tube","computer","3"],
["400","con","computer","4"],
["500","muzi","music","3"],
["600","apeach","music","2"]
]


후보키는 학번, [이름, 전공]
이 릴레이션에서 후보 키의 개수를 return 하도록 solution 함수를 완성하라.

answer = https://geonlee.tistory.com/66
input = [
 "학번","이름", "전공", "학년",
["100","ryan","music","2"],
["200","apeach","math","2"],
["300","tube","computer","3"],
["400","con","computer","4"],
["500","muzi","music","3"],
["600","apeach","music","2"]
]
return = 2
"""

relation = [["100", "ryan", "music", "2"],
            ["200", "apeach", "math", "2"],
            ["300", "tube", "computer", "3"],
            ["400", "con", "computer", "4"],
            ["500", "muzi", "music", "3"],
            ["600", "apeach", "music", "2"]]


# 후보키 형식을 만들기
# 학번, [이름, 전공]
# 해당 후보키 들의 len()으로 return 하기
def solution(relation):
	answer = 0
	candidate_keys = []
	for data in relation:
		number = data[0]
		name = data[1]
		school = data[2]
		candidate_keys.append([number, [name, school]])

	answer = len(candidate_keys[-1])

	return answer


print(solution(relation))

"""*****************************************"""
"""정답"""
from itertools import combinations


def solution(relation)


"""
start point = 2019.08.21 20:21
사용한 포모도로 = 1개
내가 너무 쉽게 생각한듯
그냥 문제에 나와있는대로 진행했는데 그게 아니였네
전혀 문제를 풀 수 있는게 없어서 그냥 답지를 적고 그걸 이해해야 겠음
답을 먼저 이해하자
"""