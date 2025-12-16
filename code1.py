# # # # # # problem no 1
 
# # # # # a = (input("Enter The Number "))

# # # # # b = list(map(int, a.split()))  # This line was convert string to integer..

# # # # # b.sort()



# # # # # problem no 2 

# # # # a = int(input("enter the first subject makrs"))

# # # # b = int(input("enter the second subject makrs"))

# # # # c = int(input("enter the third subject makrs"))

# # # # if(a>40 and b>40 and c>40):
# # # #     print("You are passed")

# # # # else:
# # # #     print("You are failed")

# # # # problem no 3

# # # passage =''' in the last period we have seen that the story of the,
# # #     and the name is yogesh is good name in india. and if you subscribe this
# # #     channel then i will give 500 rupees extra reward then you will make a lot of money '''
    
# # # word= "subscribe this" and "make a lot of money" and "india" and " yogesh"

# # # if word in passage:
# # #     print("word in found")
    
# # # else:
# # #     print("word in not found")

# # # problem no 4 

# # username = input("Enter the username:")

# # if len(username) < 10:
# #     print("username have less than 10 characters")
# # else:
# #     print("username have more than 10 character")

# # problem no 5
# lists = ''' in the last period we have seen that the story of the tea.
# cow in a animal and they have a four legs and two eyes also.'''


# # b = lists.find("cow")

# # print(b)

# word = "cow" and "period"

# if word in lists :
#     print("this is available in this lists.")
# else:
#     print("this words is not available in this lists")

# problem no 6

students = int(input("Enter Your marks here"))

if students < 35 :
    print("Failed")
    
elif (35<students<50):
    print("Grade C")
elif(50<students<70):
    print("Grade B") 
elif(70<students<90):
    print("Grade A")
elif(90<students<=100):
    print("Grade A+")
else:
    print("makrs not found bro")