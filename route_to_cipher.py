# Load the ciphertext string.
ciphertext = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"

# Convert ciphertext into a cipherlist to split out individual words.
cipherlist = list(ciphertext.split())

# Get input for the number of columns and rows.
COLS = 4
ROWS = 5

# Get input for the key.
key = '-1 2 -3 4' # neg number means read up 

# Convert key into a list to split out individual numbers.
translation_matrix = [None] * COLS # None represents the absnse of a value
plaintext = ''
start = 0
stop = ROWS

# turn key into a list of integers split by spaces
key_int = [int(i) for i in key.split()] 

# turn columns into items in list of lists: 
for k in key_int:
    if k < 0: 
        # split list based of index if value is greater than 0
        col_items = cipherlist[start:stop] 
    elif k > 0: 
        # split list and reversed it based of index id smaller than 0
        col_items = list((reversed(cipherlist[start:stop])))
    
    # defining index based of absolute value -1
    translation_matrix[abs(k) - 1] = col_items
    start += ROWS
    stop += ROWS


print("\nciphertext = {}".format(ciphertext))
print("\ntranslation matrix =", * translation_matrix, sep="\n")
print("\nkey length = {}".format(len(key_int)))


 # loop through nested lists popping off last item to new list:
for i in range(ROWS):
    for col_items in translation_matrix:
        # removing last element on list
        word = str(col_items.pop())
        # organizing final phrase
        plaintext += word + ' '

print("\nplaintext = {}".format(plaintext))

# Create a new list for the translation matrix.
# For every number in the key:
#     Create a new list and append every n items (n = # of rows) from the cipherlist.
#     Use the sign of key number to decide whether to read the row forward or backward.
#     Using the chosen direction, add the new list to the matrix. The index of each
#     new list is based on the column number used in the key.
# Create a new string to hold translation results.
# For range of rows:
#     For the nested list in translation matrix:
#           Remove the last word in nested list
#           Add the word to the translation

