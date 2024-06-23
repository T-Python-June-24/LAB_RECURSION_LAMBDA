#Q1

def letter(word, num=0):
    a=["a","e","i","o","u"]
    word=word.lower()
    if len(word) == 0:
        return num
    elif word[0] in a:
        num += 1
    return letter(word[1:], num)

word = "i love python"
print(letter(word))

#Q2

number=[40,35, 10, 15, 20]
result=list(map(lambda x:x*x , number))
print(result)
