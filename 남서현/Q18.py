#문자열 p를 u,v로 분리

def divide(p):
    open = 0
    close = 0

    for i in range(len(p)):
        if p[i] == "(":
            open += 1
        else:
            close += 1
        if open == close:
            return p[:i + 1], p[i+1:]

# 문자열 u가 올바른 괄호 문자열인지 확인하는 함수
def check(u):
    stack = []

    for p in u:
        if p == '(':
            stack.append(p):
        else:
            if not stack:
                return False
            stack.pop()

    return True

def solution(p):
    #과정1
    if not p:
        return ""
    
    # 과정 2
    u, v = divide(p)

    # 과정 3
    if check(u):
        # 과정 3-1
        return u + solution(v)
    # 과정 4
    else:
        # 과정 4-1
        answer = '('
        # 과정 4-2
        answer += solution(v)
        # 과정 4-3
        answer += ')'

        # 과정 4-4
        for p in u[1:len(u) - 1]:
            if p == '(':
                answer += ')'
            else:
                answer += '('

        # 과정 4-5
        return answer

