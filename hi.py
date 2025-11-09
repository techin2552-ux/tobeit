word = input()
count = 0
for i in word:
    if 'a' == i.lower() or 'e' == i.lower() or 'i' == i.lower() or 'o' == i.lower() or 'u' == i.lower():
        count += 1
print(word,count)