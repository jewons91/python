# mod1-test.py
def sum_(a,b):
    '''
    [summary]
    
    Args:
        a :
        b :
        
    Returns:
        return_type :
    '''
    return a + b

def safe_sum(a,b):
    '''
    [summary]
    
    Args:
        a :
        b :
        
    Returns:
        return_type :
    '''
    if type(a) == type(b):
        return sum_(a,b)
    else:
        print('같은 타입이 아님')
        return None
    
if __name__ == '__main__':
    print('mod1.py 에서 실행')
    print(safe_sum(1,5))
    print(safe_sum(1,'hi'))