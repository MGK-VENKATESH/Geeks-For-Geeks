Description:
Given a sorted array arr[] and a target value, the task is to count triplets (i, j, k) of valid indices, such that arr[i] + arr[j] + arr[k] = target and i < j < k.

Examples:

Input: arr[] = [-3, -1, -1, 0, 1, 2], target = -2
Output: 4
Explanation: Two triplets that add up to -2 are:
arr[0] + arr[3] + arr[4] = (-3) + 0 + (1) = -2
arr[0] + arr[1] + arr[5] = (-3) + (-1) + (2) = -2
arr[0] + arr[2] + arr[5] = (-3) + (-1) + (2) = -2
arr[1] + arr[2] + arr[3] = (-1) + (-1) + (0) = -2
Input: arr[] = [-2, 0, 1, 1, 5], target = 1
Output: 0
Explanation: There is no triplet whose sum is equal to 1. 
Constraints:
3 ≤ arr.size() ≤ 103
-105 ≤ arr[i], target ≤ 105

Python3:
class Solution:
    def countTriplets(self, arr, target):
        # code here
        ans=0
        n=len(arr)
        for i in range(n-2):
            
            j=i+1
            k=n-1
            
            while(j<k):
                s=arr[i]+arr[j]+arr[k]
                if s==target:
                    x=arr[j]
                    c1=0
                    c2=0
                    y=arr[k]
                    while(j<k and arr[j]==x):
                       j+=1
                       c1+=1
                    
                    while(j<=k and arr[k]==y):
                        k-=1
                        c2+=1
                     
                    if x==y:
                        c=c1+c2
                        ans+=(c*(c-1))//2
                    else:
                        ans+=c1*c2
                        
                    
                    
                elif s<target:
                    j+=1
                else:
                    k-=1
        
        return ans
