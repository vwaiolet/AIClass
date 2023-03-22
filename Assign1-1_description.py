#3개의 배열에서 3개의 요소(각각 배열에서)의 합이 목표 값과 같은지 확인하는 
#Python 프로그램을 작성하십시오. 
#3요소 조합을 모두 인쇄하십시오.
'''
샘플 데이터:
/*
X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]
목표 = 70
*/
'''

'''
X = [10, 20, 20, 20]
Y = [10, 20, 30, 40]
Z = [10, 30, 40, 20]
T = 70
RESULT = []
for i in range(len(X)):
    for j in range(len(Y)):
        for k in range(len(Z)):
            if X[i] + Y[j] + Z[k] == T:
                RESULT.append([X[i], Y[j], Z[k]])  

# 모든 case
# print(RESULT)
# 중복 제거
result = set(map(tuple, RESULT))
print(result)       
'''