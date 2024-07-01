PI = 3.141592 # 대문자로 표기 : 상수다 의미를 부여

class Math:
    '''
    [summary]
    수학관련 기능 클래스
    '''
    def solv(self,r):
        return PI * (r ** 2)
    
def sum_(a,b): # function
    '''
    [summary]
    
    '''
    return a + b

if __name__ == '__main__':
    print(PI)
    a = Math()
    print(a.solv(2))
    print(sum_(PI,4.4))