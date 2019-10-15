"""
(Daily Coding Problem)
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

# Idea: Right away, brute force says to check each pair (nested for loop). 
def brute_force(list, k):
	for i in range(len(list)):
		for j in range(i+1, len(list)):
			if list[i]+list[j] == k:
				return True
	return False

# However this is O(n^2) and the bonus hints that O(n) is possible.

# Maybe memoization? Trying the maximum contiguous sum strategy, where you take the sum of pairs as you go. 
# If the sum is greater than k, keep the smaller number and continue; if the sum is larger, keep the larger number.
def one_pass(list, k):
	curr = list[0]
	for i in range(1,len(list)):
		sum = curr + list[i]
		if sum == k:
			return True
		elif sum > k:
			curr = min(curr, list[i])
		elif sum < k:
			curr = max(curr, list[i])
	return False

# Test
test_suite = [17, 25, 40, 30, 0]

for item in test_suite:
	print(one_pass([10,15,3,7], item))

# Expect: True, True, False, False, False


"""Answer Review
Another O(n) solution subtracted the current element from k and checked if it was in the array.
Other solutions implemented hashmaps or sorted the array first. 
- Need to study more to see if these solutions are more optimal than mine and the one below.
"""

def FindPairs(arr, k):
    for i in range(0, len(arr)):
        if k - arr[i] in arr:
            return True
    return False  


