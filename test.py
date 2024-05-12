# list_of_lists = [['16', '12', '8', '4', '0'],['1', '5', '9', '13', '17'],
#                  ['18', '14', '10', '6', '2'],['3', '7', '11', '15', '19']]

# for i in range(len(list_of_lists)):
#     print(list_of_lists[i]) 

# print(list_of_lists[0][0])

# Load the ciphertext string.
ciphertext = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"

# Convert ciphertext into a cipherlist to split out individual words.
cipherlist = list(ciphertext.split())

print(cipherlist)

translation_matrix = []
translation_matrix_2 = [None] * 4

# print(translation_matrix)
# print(translation_matrix_2)

key = '-1 2 -3 4'

key_int = [int(i) for i in key.split()]
print(key_int)