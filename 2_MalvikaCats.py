"""
Malvika's cats, Chingam and Jimma are also bored of solving problems. Fortunately, Chingam has found n
bars of dark chocolate. They all have the same width, but differ in their lengths. In fact, no two
chocolate bars have the same length. All the n bars are kept in a row. Let's say that their lengths
are given by L[1], L[2], … , L[n] from left to right. That is, length of bar i is L[i].

Chingam decided to play a little game with Jimma. In one step,
Jimma has to choose some bar which has not been eaten yet.
Chingam hates inversions, so he will instantaneously eat that bar, along with every other Bar with
which it forms an Inversion Pair. We say that bars i and j form an Inversion Pair, if the bar to the left
is longer than the bar to the right.

That is, if Jimma selects bar i, whose length is L[i], then Chingam will eat this, as well as every bar
j such that j > i and L[j] < L[i], as well as every bar k such that k < i and L[k] > L[i]. After this,
the step ends, they proceed to the next step, where Jimma selects another bar and the whole process repeats.
The game ends when all the n chocolate bars are eaten.

Jimma doesn't like this game because she does not get any chocolate. So, she wants to finish it as soon as
possible and go back to sleep. Please help her find the minimum number of steps needed for the game to end.
---------------
Input
The first line of input contains a single integer T denoting number of test cases
The first line of each test case contains one integer: n.
The second line contains n space separated integers, which correspond to L[1], L[2], … , L[n].
---------------
Output
For each test case, output a single integer in a line corresponding to the answer of the problem.
---------------
Constraints
1 ≤ T ≤ 5
1 ≤ n ≤ 105
1 ≤ L[i] ≤ n
---------------
Example
Input:
1
4
3 1 4 2

Output:
2
---------------
Explanation
In the first step, Jimma can choose bar 4, which is of length 2. Bar 3 and bar 1 form Inversion Pairs with bar 4. So Chingam eats all these 3 bars. In the second step, Jimma chooses bar 2, and she's done. You can check that Jimma cannot get rid of all the four bars in one step.
"""
T = int(input("Enter the no of test cases:"))
for t in range(T):
	num = int(input("Enter the no of elements:"))
	list1 = []
	for i in range(num):
		list1.append(int(input("Enter element:")))
	count2 = 0
	while(len(list1) != 0):
		# Calculating total inversion pairs of each element
		list2 = []
		for i in range(len(list1)):
			count1 = 0
			for j in range(i+1, len(list1)):
				if(list1[i] > list1[j]):
					count1 += 1
			for k in range(0, i):
				if(list1[k] > list1[i]):
					count1 += 1
			list2.append(count1)
		print("Inversion Pair of each element:",list2)

		# Eating chocolates
		list3 = []
		temp_ind =  list2.index(max(list2))
		temp_ele = list1[temp_ind]
		for i in range(0,temp_ind):
			if(list1[i] > temp_ele):
				list3.append(list1[i])
		for i in range(temp_ind,len(list1)):
			if(list1[i] < temp_ele):
				list3.append(list1[i])
		list1.remove(temp_ele)
		for i in list3:
			list1.remove(i)
		print("Elements left:",list1)
		count2 += 1

	#Output
	print("Total no of steps:",count2)