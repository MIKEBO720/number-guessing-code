#generate random number and track how many times the  user is going to  guess it
import random #module for generating random numbers

top_of_range= input("Type a number: ") #ask user for the top of the range 
#step 3 make sure the user enters a number and the number is greater than 0
guesses=0 #initialize the number of guesses to 0

if top_of_range.isdigit(): #check if the input is a digit
  top_of_range = int(top_of_range)#convert the input to an integer and thats why isdigit() is used to make sure it is a number

  if top_of_range <= 0: #if the number is less than or equal to 0
    print("please enter a number greater than 0 and try again later") #ask the user to enter a number greater than 0
    quit()  #quit the program if the number is less than or equal to 0
else:
  print("please enter a number ")
  quit( ) #quit the program if the input is not a digit
 
random_number=(random.randint( 1 ,top_of_range))#generating a random number between 1 and the top of the range and what the user entered
#notes:generate a random number between 1 and 100 but not including 101 its just python's way of doing it
#but if using randint(1,100) it will include 100 thatss just how python works

while True: #infinite loop until the user guesses the number
    #start by asking the user to guess the number
    guesses += 1 #increment the number of guesses by 1
    user_guess= input("make a guess:")      
        #ask the user to make a guess and make sure the guess is an interger meaning a number
    if user_guess.isdigit(): #check if the input is a digit
     user_guess = int(user_guess)#convert the input to an integer and thats why isdigit() is used to make sure it is a number
     
    else:
     print("please enter a number ")
    
     continue 
    
    if user_guess == random_number: #if the user guess is equal to the random number
      print("you got it!") #print you got it
      break #break the loop if the user guessed the number 
    
    else:
     if user_guess > random_number:#now we need to change the code to tell the user if the guess is too high or too low

        print("you guessed too high") #if the user guess is greater than the random number
     else:
        print("you guessed too low")
         
print("you made", guesses, "guesses") #print the number of guesses the user has made
     
     
     #notes:this is a notes for me to remember the progress of the code
#print the number of guesses the user has made
#overall whats the code does is it generates a random number between 1 and the top of the range meaning the number the user entered

#so the code will keep asking the user to guess the number until the user guesses it
#and it will keep track of how many guesses the user has made and print it out when the user guesses the number
#and if the user enters a number less than or equal to 0 it will ask the user to enter a number greater than 0 and quit the program
#and if the user enters a non-digit input it will ask the user to enter a number        