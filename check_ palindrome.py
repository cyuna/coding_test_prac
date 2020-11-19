def check_count(st):
    li = []
    for i in range(len(st)):
        li.append(st[i:i+1])
    digits = 0
    space = 0
    alphas = 0
    
    for i in li:

        if i == ' ':
            space += 1
        elif(ord(i) >= 48 and ord(i) <= 57):  
           digits +=1
        elif ord(i) >= 65 and ord(i) <= 90 :
            alphas +=1
        elif(ord(i) >= 97 and ord(i) <= 122):               
           alphas +=1

           
    print(digits)
    print(space)
    print(alphas)
    
    


while(1):
    st = input("문자열을 입력하세요")
    check_count(st)
        
