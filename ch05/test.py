# import mod1 # 가져올 위치 지정
# from 패키지.모듈명 import 변수, 함수, 클래스
# from mod1 import safe_sum
# from mod1 import sum_
# from mod1 import *    사용하지 마세요

# from mod1 import safe_sum, sum_
# name space => mod2 저장
# import mod2
from mod2 import PI, Math, sum_

# print(mod1.sum1(1,2))
# print(mod1.safe_sum(1,'3'))
# print(mod1.safe_sum('hi','Hello'))

# print(mod2.PI)
print(PI)
# a = mod2.Math()
a = Math()
print(a.solv(2))
# print(mod2.sum_(1,2))
print(sum_(1,2))
print('Test.py 에서 실행')