

def longest_substring(s):
    '''
    Parameters
    ----------
    s : str
    
    Returns
    -------
    str
        Returns longest substring in alphabethical order. Picks the first 
        one if there is more than one of the same lenght.
    '''
    maxlenght=0
    i=1
    for i in range(1,len(s)):
        word=s[i-1]
        while i<len(s):
            if s[i]>s[i-1]:
                word+=s[i]
            else:
                break
            i+=1  
        if len(word)>maxlenght:
            maxlenght=len(word)
            result=word
           
    
    return "Longest substring in alphabetical order is: "+result

