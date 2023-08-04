import random
i=0
pc_number=random.randint(0,20)
for i in range(100) :
  user_number = int(input("Enter yor num:"))
  i=i+1
  if user_number==pc_number:
    print("Barande shodi")
    print("*******")
    print("Number of prediction:    ",    end="")
    print(i)
    break
  if user_number<pc_number:
    
    print("Boro balatar")
  if user_number>pc_number:
    print("Boro payintar")
