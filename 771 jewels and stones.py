""" You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A". """


def hash_table(jewels, stones):
      dic = {}
      jewels_stones = 0
      
      #creating the keys of dictionary using jewels elements
      for i in jewels:
            dic[i] = 0
            
      #Checking weather stones element is in dic or not
      for j in stones:
            if j in dic:
                dic[j] += 1
                jewels_stones += 1
                
      # returning the value of stone that we have for the jewels
      return jewels_stones

jewels = "aA"
stones ='aAAbbb'

print (hash_table(jewels,stones))
