
words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
result = [3, 2, 4, 1, 0]

answer_list = []
# 물음표 삭제 text.replace("?", "")
for query in queries:   # fro??
	answer = 0
	for word in words:  # frodo, front, frost, frozen ...
		# 단어 수와 문자가 거기에 포함 한다면
		if len(query) == len(word) and query.replace("?", "") in word:
			# 새로운 기준, 위치도 맞아야함
			lst = []    # query에서 ? 인 부분
			for i in enumerate(query):
				if i[1] == '?':
					lst.append(i[0])

			word = list(word)
			for index in lst:
				word[index] = '?'
			word = str(word)
			if word == query:
				answer += 1
	print(query, answer)
	answer_list.append(answer)


def solution(words, queries):
	answer_list = []
	# 물음표 삭제 text.replace("?", "")
	for query in queries:   # fro??
		answer = 0
		for word in words:  # frodo, front, frost, frozen ...
			if len(query) == len(word) and query.replace('?', '') in word:

				# 새로운 기준, 위치도 맞아야함
				lst = []  # query에서 ? 인 부분
				for i in enumerate(query):
					if i[1] == '?':
						lst.append(i[0])

				word = list(word)
				for index in lst:
					word[index] = '?'
				word = ''.join(word)

				if query == word:
					answer += 1
		answer_list.append(answer)
	return answer_list





words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
result = [3, 2, 4, 1, 0]

def solution(words, queries):
	answer_list = []
	for query in queries:   # fro??
		answer = 0
		target = [i for i, ltr in enumerate(query) if ltr != '?']       # query like "???"
		if len(target) == 0:
			answer += len(words)
		else:
			for word in words:  # frodo, front, frost, frozen ...
				if len(query) == len(word) and query.replace('?', '') in word:
					if query[target[0]:target[-1] + 1] == word[target[0]:target[-1] + 1]:
						answer += 1
		answer_list.append(answer)
	return answer_list

