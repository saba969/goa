def reverse_and_add_length(s):
  
    words = s.split()
    
    result = [word + " " + str(len(word)) for word in words[::-1]]
    return result
