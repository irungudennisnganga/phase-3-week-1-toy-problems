alpa={ "a": 1, "b":2, "c":3,"d":4,"e":5,"f":6,"g":7,"h":8,"i":9,
       "j":10, "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17,
       "r":18, "s":19, "t":20, "u":21, "v":22,"w":23,"x":24,"y":25, "z":26,
    
    }

def check_consonant(alaphabet,word):
    word.lower()
    
    sum = 0
    for i in word:
        
        if i != "a" and i != "e" and i != "i" and i != "o" and i != "u"  and i != " " :
                    
            num=alaphabet.get(i)
            sum += num
        
    print(sum)    
        
check_consonant(alpa,"zodacs")        



# if    i  == "a" :
        
    #     print(word.split(i))
       
    # elif i == "e":
       
    #     word.split(i)
    #     print(word)
    # elif i == "i":
        
    #     word.split(i)
    #     print(word)
    # elif i == "o":
        
    #     print(word.split(i))
       
    # elif i == "u":
        
    #     print(word.split(i))