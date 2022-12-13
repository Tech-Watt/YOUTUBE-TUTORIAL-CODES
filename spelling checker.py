from textblob import TextBlob as tb

def textInput():
    words = input('Enter some text: ')
    words = words.split()
    return words

words = textInput()
print(words)

correction = []
for word in words:
    correction.append(tb(word))

for result in correction:
    print(result.correct(),end=' ')
