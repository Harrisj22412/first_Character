def Unique_char(str):
    #count the values
    letter = Counter(str)
    #starts the loop
    for i in str:
        #checks the value
        if letter[i] == 1:
            #Returns the place of the index
            return str.index(i)
    return -1

