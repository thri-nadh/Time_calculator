#python 2.7.15

# i'm eswar beginner to python, so give suggestions on comments

choose_1 = input('enter the number what you want in \n 1. hours to seconds \n 2. hours to minuites \n 3. minuites to seconds \n 4. days to minutes \n 5. days to seconds \n 6. days to hours: ') 

#converts hours to seconds
if (choose_1 == 1):
     choose_2 = input ('enter no.of hours:')
     print (choose_2*60 ) 

#converts hours to minutes     
elif (choose_1 == 2):
  choose_3 = input ('enter no.of hours:')
  print (choose_3*60) 

#converts minutes to seconds
elif (choose_1 == 3):
  choose_3 = input ('enter no.of hours:')
  print (choose_3*60)

#converts days to minutes      
elif (choose_1 == 4):
  choose_4 = input ('enter no.of days:')  
  print (choose_4*24*60)
  
#converts days to seconds
elif (choose_1 == 5):
  choose_5 = input ('enter no.of days:')
  print (choose_5*24*60*60)

#converts days to hours
elif (choose_1 == 6):
  choose_6 = input ('enter no.of days:')
  print (choose_6*24)
