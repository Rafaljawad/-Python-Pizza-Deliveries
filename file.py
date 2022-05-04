
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")# choose the size to get your bill if you choose small ,you will pay $15, if you pick out medium , you have to pay $20. Finally if you choose larg , yoou will pay $25
add_one_topping = input("Do you want to add extra one topping? Y or N ")#if you add more one topping , you will charged extra $2 for small size and extra $3 for larg and meduim
extra_cheese = input("Do you want extra cheese? Y or N ")# if you want to add extra cheese , you will charged $1 for all sizes

# running the code steps:# I have drawn a flowchart to implement this code
# runing the small size choice
if size=="S":# if you choose small
  bill=15# the initaial bill is $15
  if add_one_topping =="Y":# if you say yes to choose one more topping
    bill+=2# then the bill will be 15+2=>$17
    if extra_cheese=="Y":# and if you add extra cheese 
      bill+=1#then the bill will be 17+1=>$18
      print(f"your total bill is ${bill}")# print the final bill after adding the two         optins above
    else:# if you choose no extra cheese so here you will be charged just 15+1 for the     cheese
      print(f"your total bill is ${bill}")# then print the bill which will be 15+2=$17
  else:# this else for choosing no more topping 
    if extra_cheese=="Y":# but extra cheese is yes
      bill+=1# then the bill will charged $1 
      print(f"your total bill is ${bill}")# and the bill will be 15+1=$16
    else:# this else for not choosing extra cheese and in this case the price will be       just $15 with no cheese and no more topping. 
      print(f"your total bill is ${bill}")# the bill will be just $15
      
 #############finishing the small size bill#########################
###starting the medium size bill same steps above with changin the price#####
elif size=="M":
  bill=20
  if add_one_topping =="Y":
    bill+=3
    if extra_cheese=="Y":
      bill+=1
      print(f"your total bill is ${bill}")
    else:
      print(f"your total bill is ${bill}")
    
  else:
    if extra_cheese=="Y":
      bill+=1
      print(f"your total bill is ${bill}")
    else:
      print(f"your total bill is ${bill}")
      

  #############finishing the meduim size bill#########################
###starting the larg size bill same steps above with changin the price#####
else:
  bill=25
  if add_one_topping =="Y":
    bill+=3
    if extra_cheese=="Y":
      bill+=1
      print(f"your total bill is ${bill}")
    else:
      print(f"your total bill is ${bill}")
    
  else:
    if extra_cheese=="Y":
      bill+=1
      print(f"your total bill is ${bill}")
    else:
      print(f"your total bill is ${bill}")




