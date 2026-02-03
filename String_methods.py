print(dir(""))
print(help("bob".capitalize))
print("heLLo BOBOBOB!!!".capitalize())
# prints Hello bobobob!!!

s = "Hello World"
print(s.upper())
print(s.lower())
# Useful when comparing things, words in a book, in lower and uppercase
print(help(s.center))
print(s.center(30))
print(s.center(50, "*"))

# Fake chrismtas tree
for i in range(10):
    s=("*"*(2*i+1))
    print(s.center(50))
for i in range(4):
    print("***".center(50))

# find, finds the position of substring
s = "I see thea cat. The cat is black. Cats are nice."
print(s.find("cat"))
# 8 is the first occuraence
print(s.find("dog"))
# -1 when it cant find

pos = 0
while True:
    pos = s.find("cat",pos)
    if pos == -1:  # we cannot find it
        break
    print(f"cat on position{pos}")
    # f string, you want a value in the string
    pos+=1

print(s.count("cat"))
print(s.replace("cat", "dog"))
print(s.split())
