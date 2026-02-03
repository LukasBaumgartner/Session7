# + will perform string concatenation: two strings put together

s1 = "hello"
s2= "bye"
print(s1+s2)
print(s2+s1)
print(s1+ ", "+ s2+"!!")

# - is unsupported, does not work

# You can multiply a string by an integer
print(3*s2)
# you can also do
print(s1+" "+s2+"!"*10)

#We can iterate over a string using for
# 1. do the same with a while
# 2. I want the result to be hhhhheeellllooooo

for c in s1:
    print(c)

#     1. Same but proving that the for can be written as a while
i=0
while i<len(s1):
    print(s1[i])
    i=i+1

# 2.
s_new = ""
for c in s1:
    s_new =s_new+c*4
print(s_new)