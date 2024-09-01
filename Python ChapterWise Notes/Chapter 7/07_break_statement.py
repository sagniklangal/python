for i in range(10): # Print from 0 to 9(before 10)
    print(i)
    if i==5:
        break
else:
    print("This is inside else of for")

'''Else will be executed after complete execution of loop
But here the loop is terminated after i == 5
So, else will not be executed'''