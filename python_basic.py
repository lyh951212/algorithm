# itertools

# 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)을 계산해준다.
# permutations는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다.
from itertools import permutations

data = ['A', 'B', 'C']
result = list(permutations(data, 2)) # 모든 순열 구하기

print(result)

# combinations는 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 
    # 나열하는 모든 경우(조합)을 계산한다.
# combinations는 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용한다.

from itertools import combinations

data = ['A', 'B', 'C']
result = list(combinations(data, 2)) # 2개를 뽑는 모든 조합 구하기

print(result)

# 힙
import heapq

def heapsort(arr):
    h = []
    result = []

    for value in arr:
        heapq.heappush(h, -value)

    for _ in range(len(h)):
        print(-heapq.heappop(h), end = ' ')
    print()

heapsort([1,2,3,4,5])

# 파이썬에서는 이진 탐색을 쉽게 구현할 수 있도록 bisect 라이브러리를 제공한다. 
# bisect 라이브러리는 '정렬된 배열'에서 특정한 원소를 찾아야 할 때 매우 효과적으로 사용된다.
# 이 두 메서드는 시간 복잡도 O(logN)에 동작한다.
from bisect import bisect_left, bisect_right
# bisect_left(a, x) #정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
# bisect_right(a, x) #정렬된 순서를 유지하도록 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드

# 예를 들어 정렬된 리스트 [1, 2, 4, 4, 8]이 있을 때, 새롭게 데이터 4를 삽입하려 한다.
arr = [1, 2, 4, 4, 8]

bisect_left(arr, 4) # 2 반환
bisect_right(arr, 4) # 4 반환

# math
print("!!!!math!!!")
import math

print(math.factorial(5)) # 5! 출력

print(math.sqrt(7)) # 루트7 출력

print(math.gcd(21, 14)) # 21과 14의 최대 공약수 출력

print(math.pi) # 파이(pi) 출력

print (math.e) # 자연상수 e 출력

# 문자열
data =  "Don't you know \"Python\"?"
print(data) # Don't you know "Python"?

# set자료형
## 집합 자료형 초기화 방법 
a = set([1,2,3,4,5])
b = {3,4,5,6,7}

a | b # 합집합 {1,2,3,4,5,6,7}
a & b # 교집합 {3,4,5}
a - b # 차집합 {1,2}

data = set([1,2,3])
print(data)

# 새로운 원소 추가
data.add(4)

# 새로운 원소 여러 개 추가
data.update([5,6])

# 특정한 값을 갖는 원소 삭제
data.remove(3)

print(data)

# 내장함수들
result = eval( "(3+5) * 7" )
print(result)

data = [('홍길동', 35), ('이순신', 17), ('아무개', 88)]
result = sorted(data, key = lambda x : x[1], reverse = True)
print(result)

data = ["23", "59", "59"]
print(":".join(data))
# 23:59:59

#itertools
from itertools import permutations, combinations, product,combinations_with_replacement

data = ['a', 'b', 'c'] # 데이터 준비
# 리스트에서 3개를 뽑아 나열하는 모든 경우를 출력
result = list(permutations(data,3)) # 모든 순열 구하기
print(result)
# [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]

result = list(combinations(data,2)) # 2개를 뽑는 모든 조합 구하기
print(result)
# [('a', 'b'), ('a', 'c'), ('b', 'c')]

result = list(product(data,repeat = 2)) # 2개를 뽑는 모든 순열 구하기 (중복 허용)
print (result)
# [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'b'), ('b', 'c'), ('c', 'a'), ('c', 'b'), ('c', 'c')]

result = list(combinations_with_replacement(data,2)) # 2개를 뽑는 모든 조합 구하기 (중복 허용)
print (result)
# [('a', 'a'), ('a', 'b'), ('a', 'c'), ('b', 'b'), ('b', 'c'), ('c', 'c')]


# print 원하는 방식으로 하기
arr = [1,3,5,7,9]
print('<', end='')
print(*arr, sep=', ' ,end= '') # <1, 3, 5, 7, 9>
print('>')

# 두 리스트의 교집합을 순서를 유지해서 구하기
a = [1,2,3,4,5]
b = [5,4,3]
c = [3,4,5]

[_ for _ in a if _ in c] # a순서 기준
# Output: [3, 4, 5]

[_ for _ in b if _ in c] # b순서 기준
# Output: [5, 4, 3]