import random
rock = ''' 
                                          _____
                                       /\| | | |
                                      / /|_|_|_|
                                      \        |
            (  ( ) ) ( )  )            \_______/
           ( ( ( ( )  )  ) )           /______/
          ( ( )) ) (   ) ( ( )        /       /
          ( (__.-.___.-.__) )        /       /
           /---._.---._.---\        /       /
           \||   '/  '   ||/       /       /
            |||  (_     |||       /       /
             || ///\\\  ||\______/       /
        ___/ ||||\__/|||||/             /
       /   \   ||||||||  /             /
      /     \   ||||||  /        _____/

      '''
paper = ''' 
_ __   __ _ _ __   ___ _ __ 
| '_ \ / _` | '_ \ / _ \ '__|
| |_) | (_| | |_) |  __/ |   
| .__/ \__,_| .__/ \___|_|   
| |         | |              
|_|         |_|        
'''
scissor = '''
   ____
  / __ \
 ( (__) |___ ___
  \________,'   """""----....____
   _______<  ()          ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/
'''
userInput = int(input("Enter 0 for Rock, 1 for Paper or 2 for Scissor\n"))
sys = random.randint(0, 2)
image = [rock, paper, scissor]
if(userInput >= 0 and userInput <= 2):
 print(f'''You chose:
      {image[userInput]}''')
print(f'''Computer chose: 
      {image[sys]}''')

if(userInput >= 3 or userInput < 0):
    print("Invalid input. You lose...")
elif(userInput == 0 and sys == 2):
    print("You Win...")
elif(sys == 0 and userInput == 2):
    print("You lose...")
elif(userInput > sys):
    print("You Win...")
elif(sys > userInput):
    print("You lose")
else:
    print("Its a draw...")

