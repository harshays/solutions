word = input()

def dimensions(word):
	word = (len(word))**0.5
	col = round(word)
	if word > col:
		row = col 
		col += 1
	else:
		row = col - 1
	assert row <= col
	return [row,col]
 
def rectangle(word):
	row,col = dimensions(word)
	new_words = ''
	for x in range(col):
		new_words += (word[x::col])
		new_words += ' '
	print (new_words[:-1])

rectangle(word)
			





