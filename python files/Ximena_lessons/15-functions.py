# print (abs(10))
# print (bool(3))
# age = input("How old are you?: ")
# myList = [3, "Banana", 17, True]
# print (len(myList))
# myList = {"Xime":29,"Adam":13,"Simon":12}
# print (len(myList))

test_file = open('./dement.txt','w')
test_file.write('Hola Amigos')
test_file.close()

test_file = open('./text.txt')
print(test_file.read())