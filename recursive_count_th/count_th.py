'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC

    # my first thought is this is pretty simple but theres a million ways to do this
    # we HAVE to use recursion so that limits our options abit

    
    th = 0 # setting initial value of the th variable

    if (len(word) <= 1): # check if the string is 1 or less characters, it obviously contians 0 "th"s 
        return th # so just return the variable that's set to 0
    

    if word[0] == 't' and word[1] == 'h': # look at the first index and seconed index of the string, if they match characters 't' and 'h' add one to th 
        th = th + 1

    # iterate the function recursively with a new starting index
    th = th + count_th(word[1:])


    # return the variable that should equal the number of times we found 't' and 'h' next to each other as an integer.
    return th
