#PCCE 5번 /심폐소생

# def solution(cpr):
#     answer = []
#     basic_order = ["check", "call", "pressure", "respiration", "repeat"]
#     for action in #####:
#         for i in #### :
#             if action == basic_order[i]:
#                 answer.append(####)
#     print(answer)
#     return answer
#
# cpr = ["call", "respiration", "repeat", "check", "pressure"]
# solution(cpr)


def solution(cpr):
    answer = []
    basic_order = ["check", "call", "pressure", "respiration", "repeat"]
    for action in cpr:
        for i in range(len(cpr)) :
            if action == basic_order[i]:
                answer.append(i+1)
    print(answer)
    return answer

cpr = ["call", "respiration", "repeat", "check", "pressure"]
solution(cpr)