# checks if the given int are positive  or negative numbers

def check_integer(data):
    # this is an empty list used to add the int greater than zero and which int is positive
    new = list([])
    
    # check if the given int are positive or negative numbers and append them to the list
    for i in data:
        if i > 0 and i == +int(i):
            new.append(i)
           
     # check if the given list contains values equal to  2  which have been appended to the list
    if len(new) == 2 :
        return(True)
    
    # return False if the given list contains values not equal to 2 which have been appended to the
    else :
        return(False)    


print(check_integer((2, 4, -3)  ))