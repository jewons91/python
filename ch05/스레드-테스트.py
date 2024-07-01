import threading
import time

# 스레드로 실행될 함수 선언
def say(msg):
    while True: # 무한반복
        print(msg)
        time.sleep(1)

# 3개 스레드 생성, 시작
for msg in ['you','need','python']:
    t = threading.Thread(target=say, args=(msg,)) # 스레드 생성
    # main thread 주된 스레드, t 자식 스레드 => 메인스레드 종료시 자식도 종료
    t.daemon = True 
    t.start()

# main thread 안에서 실행되는 코드
for i in range(100): # 0~99
    print(i)
    time.sleep(0.1)