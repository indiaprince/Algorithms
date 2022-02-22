def solution(numbers, hand):
    L_thumb_x ,L_thumb_y = 0,0
    R_thumb_x ,R_thumb_y = 2,0
    answer = ''
    for i in range(len(hand)):
        if(numbers[i]==1):     
            L_thumb_x ,L_thumb_y = 0,3
            answer+='L'
            continue
        elif(numbers[i]==4):     
            L_thumb_x ,L_thumb_y = 0,2
            answer+='L'
            continue
        elif(numbers[i]==7):     
            L_thumb_x ,L_thumb_y = 0,1
            answer+='L'
            continue
        elif(numbers[i]==3):     
            R_thumb_x ,R_thumb_y = 2,3
            answer+='R'
            continue
        elif(numbers[i]==6):     
            R_thumb_x ,R_thumb_y = 2,2
            answer+='R'
            continue
        elif(numbers[i]==9):     
            R_thumb_x ,R_thumb_y = 2,1
            answer+='R'
            continue
        elif(numbers[i]==1) : num_x,num_y = 1,3
        elif(numbers[i]==5) : num_x,num_y = 1,2
        elif(numbers[i]==8) : num_x,num_y = 1,1
        elif(numbers[i]==0) : num_x,num_y = 1,0
        dist_L = abs(num_x - L_thumb_x) + abs(num_y - L_thumb_y)
        dist_R = abs(num_x - R_thumb_x) + abs(num_y - R_thumb_y)
        if(dist_L>dist_R) : 
            if(numbers[i]==1):
                R_thumb_x ,R_thumb_y = 1,3
                answer+='R'
            elif(numbers[i]==5):
                R_thumb_x ,R_thumb_y = 1,2
                answer+='R'
            elif(numbers[i]==8):
                R_thumb_x ,R_thumb_y = 1,1
                answer+='R'
            elif(numbers[i]==0):
                R_thumb_x ,R_thumb_y = 1,0
                answer+='R'
        elif(dist_L<dist_R):
            if(numbers[i]==1):
                L_thumb_x ,L_thumb_y = 1,3
                answer+='L'
            elif(numbers[i]==5):
                L_thumb_x ,L_thumb_y = 1,2
                answer+='L'
            elif(numbers[i]==8):
                L_thumb_x ,L_thumb_y = 1,1
                answer+='L'
            elif(numbers[i]==0):
                L_thumb_x ,L_thumb_y = 1,0
                answer+='L'
        else:
            if(hand =='right') : 
                if(numbers[i]==1):
                    R_thumb_x ,R_thumb_y = 1,3
                    answer+='R'
                elif(numbers[i]==5):
                    R_thumb_x ,R_thumb_y = 1,2
                    answer+='R'
                elif(numbers[i]==8):
                    R_thumb_x ,R_thumb_y = 1,1
                    answer+='R'
                elif(numbers[i]==0):
                    R_thumb_x ,R_thumb_y = 1,0
                    answer+='R'
            else:
                if(numbers[i]==1):
                    L_thumb_x ,L_thumb_y = 1,3
                    answer+='L'
                elif(numbers[i]==5):
                    L_thumb_x ,L_thumb_y = 1,2
                    answer+='L'
                elif(numbers[i]==8):
                    L_thumb_x ,L_thumb_y = 1,1
                    answer+='L'
                elif(numbers[i]==0):
                    L_thumb_x ,L_thumb_y = 1,0
                    answer+='L'
