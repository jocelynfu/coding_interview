# CH 1 Arrays and Strings

#1.1
# good refence: https://codereview.stackexchange.com/questions/96630/determine-if-string-has-all-unique-characters
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

# Sort: time O(nlogn)
def isPerm_sort(strA, strB):
	if len(strA) != len(strB):
		return False
	sortedA = sorted(strA)
	sortedB = sorted(strB)
	for i in range(0,len(strA)):
		if sortedA[i] != sortedB[i]:
			return False
	return True

# dict: time O(n)
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


# list approach: time O(n)
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


#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

#1.3
# build new string from old, time: O(n)
def rep_space(string, length):
	if (" ") not in string:
		return string
	cnum = 0
	new_str = ""
	for c in string:
		if c == " ":
			new_str += "%20"
		else:
			new_str += c
		cnum += 1
		if cnum == length:
			return new_str

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

#1.4 hash approach; time: O(n)
def palindrome_perm(string):
	string = string.lower()
	dictPal = dict(zip(set(string),[0]*len(string)))
	for c in string:
		if c != " ":
			dictPal[c] += 1
	oddval = 0
	for c in string:
		if c != " ":
			if (dictPal[c] % 2) == 1:
				oddval += 1
				if oddval > 1:
					return False
	return True


test1 = "aab"
test2 = "jocelynlecoj"
test3 = "Tact Coa"
print palindrome_perm(test1)
print palindrome_perm(test2)
print palindrome_perm(test3)
