"""
staet point = 2019.08.22 10:40
사용한 포모도로 = 4개

먹어야할 음식 수 : N, 음식은 순서대로 나옴
마지막 음식을 먹으면 다시 1번 음식이 나온다
음식을 먹을 수 있는 시간은 1초
1초 안에 다 먹지 못해도 넘어간다.
다 먹은 음식은 사라지고, 다 먹지 못한 음식이 다음으로 나옴

food_times = 각 음식을 모두 먹는데 필요한 시간이 담겨있는 배열
K = 네트워크 장애가 발생한 시간
return  = 몇 번 음식부터 다시 섭취하면 되는지

0~1초 동안에 1번 음식을 섭취한다. 남은 시간은 [2,1,2] 이다.    1번쨰
1~2초 동안 2번 음식을 섭취한다. 남은 시간은 [2,0,2] 이다.      2번쨰
2~3초 동안 3번 음식을 섭취한다. 남은 시간은 [2,0,1] 이다.     3번쨰
3~4초 동안 1번 음식을 섭취한다. 남은 시간은 [1,0,1] 이다.     4번째
4~5초 동안 (2번 음식은 다 먹었으므로) 3번 음식을 섭취한다. 남은 시간은 [1,0,0] 이다.    5번째
5초에서 네트워크 장애가 발생했다. 1번 음식을 섭취해야 할 때 중단되었으므로, 장애 복구 후에 1번 음식부터 다시 먹기 시작하면 된다.

문제 = https://www.welcomekakao.com/learn/courses/30/lessons/42891
답지 = https://geonlee.tistory.com/67
"""


food_times = [3, 1, 2]
k = 3

"""my solution"""
time_list = [time+1 for time in range(k)]
max_try = max(food_times)
food_dic = dict()

# 음식 dic 만들기
for i in enumerate(food_times):
    food_dic[str(i[0] + 1)] = {'total': i[1], 'current': i[1]}

for tries in range(max_try):    # first, second, third
    for key, v in food_dic.items():
        food_dic[str(key)]['current'] -= 1
        food_dic[str(key)][str(tries + 1)] = 1

        if food_dic[str(key)]['current'] < 0:
            food_dic[str(key)][str(tries + 1)] = 0


answer_list = []
k = int(k) + 1
for i in range(max_try):
    for key in food_dic.keys():
        k -= food_dic[key][str(i + 1)]
        if k == 0:
            answer_list.append((i+1, key))
            break
answer = answer_list[0][1]




"""
stop position = k
0 is pass
[3, 1, 2]

[1, 1, 1]   1의 개수 = 3 list(c[0]).count(1)
[1, 0, 1]   1의 개수 = 2
[1, 0, 0]   1의 개수 = 1

if k > 1층 1의 개수:
    k -= 1층 1의 개수
else: row = 0

for lst in c:
	k - list(lst).count(1)  # 3
	
{
'1': {'total': 3, 'current': 0, '1': 1, '2': 1, '3': 1}, 
'2': {'total': 1, 'current': -2, '1': 1, '2': 0, '3': 0}, 
'3': {'total': 2, 'current': -1, '1': 1, '2': 1, '3': 0}}

"""



def solution(food_times, k):
    answer = 0
    time_list = [time + 1 for time in range(k)]
    max_try = max(food_times)
    food_dic = dict()

    # 음식 dic 만들기
    for i in enumerate(food_times):
        food_dic[str(i[0] + 1)] = {'total': i[1], 'current': i[1]}

    for tries in range(max_try):  # first, second, third
        for key, v in food_dic.items():
            food_dic[str(key)]['current'] -= 1
            food_dic[str(key)][str(tries + 1)] = 1

            if food_dic[str(key)]['current'] < 0:
                food_dic[str(key)][str(tries + 1)] = 0

    answer_list = []
    k = int(k) + 1
    for i in range(max_try):
        for key in food_dic.keys():
            k -= food_dic[key][str(i + 1)]
            if k == 0:
                answer_list.append((i + 1, key))
                break
    answer = answer_list[0][1]
    return answer

print(solution(food_times,k))