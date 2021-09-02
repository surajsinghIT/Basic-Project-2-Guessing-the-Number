#guessing the number
#quit() is used to clear the console  screen
import random
n=random.randrange(1,10)
limit=0
while (n!="guess"):
    if (limit==5):
        print("you crossed the limit,YOU LOOSE!!")
        break
    guess=int(input("enter an integer from 1 to 10:"))
    if guess>n:
        print("guess is high")
        
    elif guess<n:
        print("guess is low")
        
    else:
        print("you guessed it!")
        break
    limit+=1
        
    
    
        
        
    
    
    

                
