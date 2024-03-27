
def plusOne(digits):
        
        # num will store values from list as one number
        num = ''

        # getting numbers from list and adding it to string to get 1 number instead of list
        for i in digits:
            num+= str(i)
            


        # privously stored number is now added 1 and storing incremented number in add as string 
        add = str(int(num)+ 1)
        digits = []
        # Iterating over the new number which is in string formate
        for i in range(len(add)):
            
            digits.append(int(add[i]))

        return digits

