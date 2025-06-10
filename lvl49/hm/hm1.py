def remove_anchor(url):

    anchor_index = url.find('#')
    
    
    if anchor_index == -1:
        return url
    
   
    return url[:anchor_index]
