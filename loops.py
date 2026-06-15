names = ["veeresh" , "sai" , "krsih" , "buddi"]
dname = "@desireddecors.com"
mail = []
for name in names:
    mail.append(name + dname)
print(mail)


#print name
name = "DevOps"
for text in name:
    print(text)
    print("\n")


#print 1 to 10
for i in range(11):
    print(i)

#print even 1 to 20

for even in range(20):
    if (even % 2) == 0:
        print(even)
    
#print 7 table
for num in range(11):
    num = num * 7
    print(num)
    
text = "python"
print(text[::-1])

#6. Get the first 5 characters.
text = "automation"
print(text[:5])

#Expected:

#autom
#7. Get the last 4 characters.
text = "kubernetes"
print(text[-4:])

#Expected:

#etes
#8. Print every second character.
text = "abcdefghij"
print(text[::2])

#Expected:

#acegi

#Combined (Loop + Slicing)
#9. Reverse each word in a list.
words = ["cat", "python", "cloud"]

for w in words:
    r = w[::-1]
    print(r)

#Expected:

##tac
#nohtyp
#duolc
#10. Count vowels in a string using a for loop.
text = "developer"
vowels = "aeiou"
count = 0
for t in text:
    if t in vowels:
        count = count+1
print(count)
        
    
    

#Expected:

#4
#11. Print each character and its index.
text = "azure"
for t in text:
    print(t)

#Expected:

#0 a
#1 z
#2 u
#3 r
#4 e

text = "Dev Ops Engineer"
ntext=''
for t in text:
    if t != " ":
        ntext = ntext + t
print(ntext)


text = "Dev Ops Engineer"
print(enumerate(text))

result = ""

for ch in text:
    if ch != " ":
        result += ch

print(result)
print(f"result is {result}")

length = ''
words = ["aws", "terraform", "docker", "kubernetes"]
for w in words:
    if len(w) > len(length):
        length = w
print(length)


text = "azure"

for index, ch in enumerate(text):
    print(index, ch)
