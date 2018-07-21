words = {
	'print': 'show in the screen',
	'dictionary': 'structure',
	'for': 'cycles',
	'if': 'judge',
	'delete': 'let it go'
}

print('print is mean: ' + words['print'])
print('dictionary is mean: ' + words['dictionary'])
print('for is mean: ' + words['for'])
print('if is mean:' + words['if'])
print('delete is mean: ' + words['delete'])

#exercise_6_4
for word,mean in words.items():
	print(word.title() + ' is mean:' + mean.title())


words['sort'] = 'order'
words['add'] = 'be more and more'
words['list'] = 'a dimesion dictionary'
words['visit'] = 'get the value'
words['create'] = 'for o to 1'

for word,mean in words.items():
	print(word.title() +" is mean: " + mean.title())
