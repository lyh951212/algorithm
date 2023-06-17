def solution(skill, skill_trees):
    answer = 0
    skillset = list(map(str, skill))
    
    for st in skill_trees:
        
        stset = list(map(str, st))
        # 두리스트의 교집합을 순서를 보장해서 출력
        # stset 앞에 것에 대해서만 순서가 보장된다.
        intersection = [x for x in stset if x in skillset]
        intersection = ''.join(intersection)
        
        if intersection == "":
            answer +=1
        elif intersection in skill:
            if skill[0] in intersection:
                print(st)
                answer += 1
                
    
    return answer

print(solution("CBDK", ["CB", "CXYB", "BD", "AECD", "ABC", "AEX", "CDB", "DBKD", "IJCB", "LMDK"]))