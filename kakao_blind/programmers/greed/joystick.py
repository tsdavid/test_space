"""
start point: 2019.08.22 16:04
포모도로 :
ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

만들고자 하는 이름 name이 매개변수로 주어질 때,
이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.
"""

name = "JEROEN"  # return 56


from string import ascii_uppercase
letter_list = [ l for l in ascii_uppercase]

name_list = [l for l in str(name)]
index_list = [letter_list.index(name) for name in name_list]

answer_list = ['A'] * len(name)

move = 0
# for index in enumerate(index_list):
# 	# 처음 인덱스는 그냥 더하고
# 	if index[0] == 0: move += index[1]
#
# 	# 처음이 아니라면
# 	if index


# def solution(name):
#     answer = 0
#     return answer

"""** 풀지 못함 **"""
"""다른 사람 코드 봄 
https://codedrive.tistory.com/28
"""


def codedrive_solution(name):
	answer = 0
	name = [l for l in str(name)]   # ['J', 'E', 'R', 'O', 'E', 'N']
	base = ['A'] * len(name)    # ['A', 'A', 'A', 'A', 'A', 'A']
	idx = 0
	while True:
		rightidx = 1
		leftidx = 1
		if name[idx] != 'A':
			if ord(name[idx]) - ord("A") > 13:  # 13 이상이면 앞에서 가는게 아니라 뒤에서 가는게 맞지
				# about ord = https://docs.python.org/ko/3/library/functions.html#ord, ex) ord('a') = 97
				answer += 26 - ord(name[idx]) - ord("A")
			else:
				answer += ord(name[idx]) - ord("A")
			name[idx] = "A"     #? 이걸 왜 하는지 이해가 안감

		if name == base:
			break
		else:
			for i in range(1, len(name)):       # idx 첫번째를 처리했으니까, 1번을 제외해야함
				if name[idx + 1] == "A":    # 다음 idx가 A와 같다면
					rightidx += 1
				else:                       #? 다음 idx가 A와 같지 않다면? break? - 이해 안감
					break
				if name[idx - i] == "A":
					leftidx += 1
				else:
					break
			if rightidx > leftidx:
				answer += leftidx
				idx -= leftidx
			else:
				answer += rightidx
				idx += rightidx
	return answer
