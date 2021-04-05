"""   You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:

ruleKey == "type" and ruleValue == typei.
ruleKey == "color" and ruleValue == colori.
ruleKey == "name" and ruleValue == namei.
Return the number of items that match the given rule."""

def countMatches ( items, ruleKey, ruleValue):
    
     count = 0

#         if ruleKey == "color":
#             for i in range(len(items)):
#                 if ruleValue == items[i][1]:
#                     count+=1

#         elif ruleKey == "type":
#              for i in range(len(items)):
#                 if ruleValue == items[i][0]:
#                     count+=1

#         else:
#             for i in range(len(items)):
#                 if ruleValue == items[i][2]:
#                     count+=1

     for i in range(len(items)):
            if ruleKey == "type" and ruleValue == items[i][0]:
                count += 1
            elif ruleKey == "color" and ruleValue == items[i][1]:
                count += 1
            elif ruleKey == "name" and ruleValue == items[i][2]:
                count += 1

     return count
Items= [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]   
key = "color"
value = "silver"
print(countMatches(Items,key,value))
