# Program to count the number of each vowels
vowel = 'aeiou'
text = " how are you. where are you from"
text.casefold()
count = dict.fromkeys(vowel, 0)
for char in text:
    if char in vowel:
        count[char] += 1

print(count)


# Using dictionary and list comprehension

ip_str = 'Hello, have you tried our tutorial section yet?'
ip_str = ip_str.casefold()

count = {x: sum([1 for char in ip_str if char == x]) for x in 'aeiou'}

print(count)
