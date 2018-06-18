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

# Naive approach: time O()
def isUnique_hash(input_str):
	if len(input_str) > Alphabet_size:
		return False
	char_seen = set()
	for i in input_str:
		if i in char_seen:
			return False
		char_seen.add(i)
	return True

test = "azerty"
print isUnique(test)
print isUnique_hash(test)