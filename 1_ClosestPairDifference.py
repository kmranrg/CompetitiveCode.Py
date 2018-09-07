"""
You have an integer array A of size N. Find closest pair of numbers in an array and print their difference.
-------------
Input
The first line of the input contains an integer T denoting the number of test cases. The description of T cases follows. Integer N and next line contains N space separated values (Ai)
-------------
Output
For each test case output a difference between closest pair
-------------
Constraints
1 ≤ T ≤ 20
2 ≤ N ≤ 105
-109 ≤ Ai ≤ 109
-------------
Example
Input:
1
5
10 4 2 7 8

Output:
1
------------- 
Explanation
Example case 1. closest pair is 7,8 and their difference is 1
"""

# Source Code

T = int(input("Enter no of test cases:"))
for t in range(0,T):
    N = int(input("Enter the no of elements:"))
    list1 = []
    for i in range(N):
        list1.append(input("Enter element:"))

    print(list1)
    c = 0
    list2 = []
    for i in list1:
        if(c < N-1):
            pre = int(i)
            post = int(list1[c+1])
            list2.append(post-pre)
            c = c + 1
    for i in range(0,N-1):  
        if(list2[i] < 0):
                list2[i] = -(list2[i])
    print(list2)
    print(min(list2))
