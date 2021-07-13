'''
Input Format

The first line contains n , the number of students who have subscribed to the English newspaper.
The second line contains n space separated roll numbers of those students.
The third line contains b, the number of students who have subscribed to the French newspaper.
The fourth line contains b space separated roll numbers of those students.

output: Output the total number of students who are subscribed to the English newspaper only.
'''

n = int(input())
roll_english_newspaper = set(input().split())
b = int(input())
roll_french_newspaper = set(input().split())
print(len(roll_english_newspaper.difference(roll_french_newspaper)))