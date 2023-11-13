def solution(l,t):

    if l[0] == t:
        print([0, 0])
    
    def check(i, j, t):
        while j <= (len(l)+1):
            if sum(l[i:j]) == t:
                print([i, j])
            else:
                if i <= (len(l)+1):
                    i += 1
                    check(i, j, t)
                else:
                    print([-1, -1])
    check(0, 1, t)
    
                




        
            
            
            
            
        
    
