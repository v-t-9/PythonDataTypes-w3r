from difflib import SequenceMatcher
# Write a Python program to find the longest common sub-string from two given strings.

def longest_substr(s1,s2):
   lp1 = []
   lp2 = []
   n1 = []
   r1 = ""
   n2 = []
   r2 = ""
   ls1 = []
   ls2 = []
   res1 = ""
   res2 =""

   for i in s1:
      if i in s2:
         lp1.append(s1.index(i))
         lp2.append(s2.index(i))

   for i,j in zip(lp1,lp1[1:]):
         if i + 1 == j:
            n1.append((i,j))
         else:
            n1.append(("*","*"))
         
  
   for i, j in zip(lp2,lp2[1:]):
         if i + 1 == j:
             n2.append((i,j))
         else:
            n2.append(("*","*"))

   for i in n1:
         for j in i:
             if str(j) not in r1:
                 r1 = r1 + str(j)
 
   for i in n2:
         for j in i:
             if str(j) not in r2:
                 r2 = r2 + str(j)
   
   ls1 = r1.split("*")
   len1 = [len(i) for i in ls1]
   ma1 = max(len1)
   for i in ls1:
       for j in i:
         if len(i) == ma1:
           res1 = res1 + s1[int(j)]
   
   ls2 = r2.split("*")
   len2 = [len(i) for i in ls2]
   ma2 = max(len2)
   for i in ls2:
       for j in i:
         if len(i) == ma2:
           res2 = res2 + s2[int(j)]
   
   if res1 == res2:
      return res2



if __name__ == "__main__":
    s1 = "abcdsiofmh"
    s2 = "mhzabcdnpxbd"
    print(longest_substr(s1,s2))
    
