num = int(input())
 
line = 0 
end = 0 
while num > end: 
    line += 1  
    end += line  
    
gap = end - num 
if line % 2 == 0: # 짝수 라인 일때
    top = line - gap  #분자
    under = gap + 1  #분모
else : #홀수 라인 일때
    top = gap + 1  
    under = line - gap  
    
print(top, '/', under, sep='')