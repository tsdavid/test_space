"""목적 : 다양한 사람들이 들어오고, 나가는 것을 지켜볼 수 있는 관리자창을 만들기로 했다.
1. 채팅방을 나가거나, 들어가면 알려줘라
2. 유저는 두개 이상의 닉네임을 사용할 수 있다.
3. 닉네임은 중복이 될 수 있다.
4. 닉네임을 변경하는 방법은
    4-1. 채팅방을 나갔다가 다시 들어오기
    4-2. 채팅방에서 닉네임 변경
5. 닉네임을 변경하면 기존 로그에 닉네임도 변경되야한다.

매개변수 : record = 채팅방에 들어오고 나가거나, 닉네임을 변경한 기록이 담긴 문자열 배열 record
해답 : https://geonlee.tistory.com/56
문제 : https://www.welcomekakao.com/learn/courses/30/lessons/42888
https://geonlee.tistory.com/85

"""
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]


def solution(record):
    anwear = []
    userDict = dict()
    for user in record:
        userLst = user.split(" ")
        if userLst[1] not in userDict.keys():
            # 저장 안되있는 경우
            userDict[userLst[1]] = [userLst[2]]
        else:
            # 저장 되있는 경우
            try:
                userDict[userLst[1]].append(userLst[2])
            except IndexError:
                userDict[userLst[1]].append("None")

    for action in record:
        act = action.split(" ")
        basic_msg = ['님이 들어왔습니다.', '님이 나갔습니다.']

        if act[0] == 'Enter':
            anwear.append(str(userDict[act[1]][-1]) + basic_msg[0])
        if act[0] == 'Leave':
            anwear.append(str(userDict[act[1]][-1]) + basic_msg[1])

    return anwear


"""*****************************************"""
"""정답 코드"""


def answer_solution(record):
    answer = []
    userDict = dict()
    chatLog = []
    for info in record:
        infoLst = info.split(" ")   # 매개변수 record를 띄어쓰기 분리해서 저장하기

        # action 경우에 따라
        if infoLst[0] == 'Enter':   # Enter이라면
            if infoLst[1] not in userDict.keys():   # Dict에 아이디가 없으면
                userDict[infoLst[1]] = infoLst[2]   # 아이디에 맞게 닉네임 저장
            else: userDict[infoLst[1]] = infoLst[2] #
            chatLog.append(['님이 들어왔습니다.', infoLst[1]])

        elif infoLst[0] == 'Leave':
            chatLog.append(['님이 나갔습니다.', infoLst[1]])
        elif infoLst[0] == 'Change':
            userDict[infoLst[1]] = infoLst[2]

    for log in chatLog:
        answer.append(userDict[log[1] + log[0]])
    return answer

print(answer_solution(record))
