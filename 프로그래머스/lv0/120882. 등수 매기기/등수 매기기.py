def solution(score):
    answer = []
    li = []
    for i in score :
        li.append(sum(i)/len(i))
        
    arr_sort = sorted(li, reverse = True)
    
    for i in li :
        answer.append(arr_sort.index(i)+1)
        
    return answer