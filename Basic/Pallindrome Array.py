Description:
Given an array arr[] of positive integers. Return true if all the array elements are palindrome otherwise, return false.

Examples:

Input: arr[] = [111, 222, 333, 444, 555]
Output: true
Explanation:
arr[0] = 111, which is a palindrome number.
arr[1] = 222, which is a palindrome number.
arr[2] = 333, which is a palindrome number.
arr[3] = 444, which is a palindrome number.
arr[4] = 555, which is a palindrome number.
As all numbers are palindrome so This will return true.
Input: arr[] = [121, 131, 20]
Output: false
Explanation: 20 is not a palindrome hence the output is false.
Expected Time Complexity: O(nlogn)
Expected Space Complexity: O(1)

Constraints:
1 <=arr.size<= 20
1 <=arr[i]<= 105


Python3:
# Function to check if all elements in the array are palindromes
def PalinArray(arr):
    def isPalindrome(num):
        # Convert the number to a string and check if it is a palindrome
        original = str(num)
        reversed_num = original[::-1]
        return original == reversed_num

    # Iterate through each element in the array and check for palindrome
    for num in arr:
        if not isPalindrome(num):
            return False
    return True
