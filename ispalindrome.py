class Solution:
    def isPalindrome( x: int) -> bool:
        
        x_str = str(x)
        return x_str == x_str[::-1]  


    
print(Solution.isPalindrome(121))