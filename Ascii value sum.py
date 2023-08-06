
#My Code and my Logic 


#User function Template for python3
class Solution:
    def reciprocalString(self, S):
        a=""
        k=S.strip()
        for i in k:
            if i.islower():
                if (ord(i)+25)<=122:
                    a+=chr(ord(i)+25)
                else:
                    k=ord(i)-97
                    a+=chr(122-k)
            elif i.isupper():
                if (ord(i)+25)<=90:
                    a+=chr(ord(i)+25)
                else:
                    k=ord(i)-65
                    a+=chr(90-k)
            else:
                a+=i
        return a

#Chat Gpt Logic
    class Solution:
    def reciprocalString(self, S):
        result = ""
        for i in S:
            if i.isalpha():
                if i.islower():
                    reciprocal = chr(ord('a') + (ord('z') - ord(i)))
                else:
                    reciprocal = chr(ord('A') + (ord('Z') - ord(i)))
            else:
                reciprocal = i
            result += reciprocal
        return result

                    

