# CH 1 Arrays and Strings

#1.1
Alphabet_size = 96
# Naive approach: time O(n^2)
def isUnique(input_str):
	for i in range(0,len(input_str)):
		for j in range(i+1,len(input_str)):
			if (input_str[i]==input_str[j]):
				return False
	return True

# Set approach: time O(n)
def isUnique_hash(input_str):
	if len(input_str) > Alphabet_size:
		return False
	char_seen = set()
	for i in input_str:
		if i in char_seen:
			return False
		char_seen.add(i)
	return True


# Sorting approach: time O(n log n)
def isUnique_sort(input_str):
	if len(input_str) > Alphabet_size:
		return False
	sorted_input = sorted(input_str)
	for i in range(0,len(input_str)-1):
		if input_str[i]==input_str[i+1]:
			return False
	return True


# Boolean list approach: time O(n)
def isUnique_list(input_str):
	if len(input_str) > Alphabet_size:
		return False
	boolist = [False] * 96
	for c in input_str:
		num = ord(c)-32
		if boolist[num] == True:
			return False
		boolist[num] = True
	return True

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

#1.2

#Sort: time O(nlogn)
def isPerm_sort(strA, strB):
	if len(strA) != len(strB):
		return False
	sortedA = sorted(strA)
	sortedB = sorted(strB)
	for i in range(0,len(strA)):
		if sortedA[i] != sortedB[i]:
			return False
	return True

def isPerm_dict(strA, strB):
	if len(strA) != len(strB):
		return False
	dictA = dict(zip(set(strA),[0]*len(strA)))
	dictB = dict(zip(set(strB),[0]*len(strB)))
	for a in strA:
		dictA[a] += 1
	for b in strB:
		dictB[b] += 1
	return dictA==dictB

def isPerm_list(strA, strB):
	if len(strA) != len(strB):
		return False
	match_list = [0] * Alphabet_size
	for a in strA:
		numA = ord(a)-32
		match_list[numA] += 1
	for b in strB:
		numB = ord(b)-32
		match_list[numB] -= 1
		if match_list[numB] < 0:
			return False
	return True

test1a = "abb"
test1b = "bab"
test1c = "aab"
print isPerm_list(test1a,test1b)
print isPerm_list(test1a,test1c)
