class Solution:
    def isPalindrome(self, s: str) -> bool:
        i , j = 0 , len(s) - 1
        s  = s.lower()
        while 1 :
            while i < len(s) -1  and   not s[i].isalnum():
                i += 1
            while  j > 0 and not s[j].isalnum() :
                j-= 1
            if i >= j:
                return True
            if s[j] != s[i]:
                return False
            j -= 1
            i += 1