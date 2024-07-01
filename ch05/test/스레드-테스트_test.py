import threading
import time

def say(msg):
    while True:
        print(msg)
        time.sleep(1)
        
for msg in ['you', 'need', 'python']:
    t = threading.Thread(target = say, args = (msg,))
    t.daemon = True
    t.start()

for i in range(100):
    print(i)
    time.sleep(0.1)