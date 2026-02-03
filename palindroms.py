# s = "A man, a plane, a canal: Panama"
# palindrom, reads the same forward and backwards
# more examples
s= "Yo! Banana Boy!"
# s= "racecar"
# s= "A nut for a jar of tuna"

# Step 1: remove punctuations
# Step 2: remove spaces
# Step 3: Convert to lowercase
# Step 4: compare with the reverse
# Step 5: profit!

punctuation= "!,.?-"

for p in punctuation:
    s= s.replace(p, "")
    # removing punctuation one by one
print(s)
# now spaces
s = s.replace(" ", "")
print(s)
s = s.lower()
print(s)
if s== s[::-1]:
    print("is palindrome")
else:
    print("not palindrome")