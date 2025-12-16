# import random

# def game():
#     print("You are playing the game..")
#     score = random.randint(1, 62)
    
#     with open("hiscore.txt") as f:
#         hiscore = f.read()
#         if(hiscore!=""):
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0
    
#     print(f"Your score: {score}")
#     if(score>hiscore):
#         with open("hiscore.txt", "w") as f:
#             f.write(str(score))
            
            
#     return score
    
# game()


def generateTable():
    table = ""
     
for i in range(1, 11):
    table += f"{n} x {i} = {n*i}\n"
    
    with open(f"tables/table_{n}.text", "w") as f:
        f.wrtie(table)
        
        
        
for i in range(2, 21):
    generateTable(i)