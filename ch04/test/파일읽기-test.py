with open('./새파일.txt','r',encoding='utf-8') as f:
    while True:
        line = f.readline()
        print(line)
        if not line:
            break
        
with open('./새파일.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
for line in lines:
    print(line)
    
with open('./새파일.txt','r',encoding='utf-8') as f:
    lines = f.read()
print(lines)