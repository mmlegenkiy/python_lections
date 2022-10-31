import pickle


file = open('lear', 'r')
str = file.read()
file.close()

# str1 = pickle.load(file)

print(str1)

# file1 = open('lear', 'w')
# file1.write(str1)
# file1.close()

# print(str1)
# print("Number of symbols")
# print(len(str1))
# print('----------------')
# print('which word ?')
# print(str1[5878:5883])
# print('----------------')
# print(str1.count('love'))
# print(str1.lower().count('love'))
# print(str1.lower().count('king'))
# print(str1.index('power'))
# print('----------------')
# print(str1.index("kingdom", 150))
# print(str1.index('the division of the kingdom'))
# print(str1.index('In three our kingdom'))
# print(str1.index('Remain this ample third of our fair kingdom'))
# print(str1.index('Upon our kingdom. '))
# word = 'son'
# print(str1.count(word))
# print(str1.lower().count(word))
#
# print(str1.rfind(word))
# print(str1[1942:1945])
# print(str1.index(word), 603)
# ind = 0
# partstr = str1
# while word in partstr:
#     indp = partstr.index(word)
#     partstr = str1[indp:]
#     ind += indp
#     print(ind)