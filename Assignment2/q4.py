def isAnagram(s1, s2):
    list1 = list(s1)
    list2 = list(s2)
    list1.sort()
    list2.sort()
    if list1 == list2:
        print("is an anagram")
    else:
        print("is not an anagram")

while True:
    s1 = input("Please enter the first word: ")
    s2 = input("Please enter the second word: ")
    if s1.isalpha() and s2.isalpha():
        isAnagram(s1,s2)
        break
    else:
        print("Please enter two words!")