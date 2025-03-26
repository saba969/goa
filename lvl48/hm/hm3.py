def add_length(s):

    words = s.split()
    

    result = [word + str(len(word)) for word in words]
    
    return result
