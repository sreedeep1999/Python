string = "hello world"
vowels = ['e', 'h'] 
new_string = []
for i in string:
    if i in vowels:
        new_string.append(i)

print("string :", string)
print("vowels in string ",new_string)
