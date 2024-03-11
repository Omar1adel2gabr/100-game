#FILE : CS112_A1_T2_1_20230259
# Purpose : two players start from 0 each one can choose a number from 1:10  and who reach to 100 first he is the winner 
# AUTHOR : Omar Adel Gabr
# ID : 20230259

total =0
while True:
    
    player_one=int(input("enter a number player one :"))
    if   player_one >10 or player_one<1:  # make sure that he will choose from 1 to 10 
       print ("please enter a number between 1:10")
       break 
    total+=player_one
    print("total is :",total)
 
    if total ==100 :  #check if player one win 
      print("Player one is the winner")
      break
    
    if total > 100 :  #check if player one miss the win by enter invalid number
       print ("enter another number")
       total = total -player_one
       print("total is :",total)
       player_one=int(input("enter a number player one :"))
       total+=player_one
       if   player_one >10 or player_one<1:
          print ("please enter a number between 1:10")
          break 
    
       if total ==100 :
         print("Player one is the winner")
         break
   
    player_two=int(input("enter a number player two :"))
    if   player_one >10 or player_one<1:   # make sure that he will choose from 1 to 10 
       print ("please enter a number between 1:10")
       break
    
    total+=player_two
    print("total is :",total)

    if total ==100 :     #check if player two win 
      print("Player two is the winner")
      break

    if total > 100 :       #check if player two miss the win by enter invalid number
       print ("enter another number")
       total = total -player_two
       print("total is :",total)
       player_two=int(input("enter a number player two :"))
       total+=player_two
       if   player_two >10 or player_two<1:
        print ("please enter a number between 1:10")
        break 
       if total ==100 :
        print("Player two is the winner")
        break
    