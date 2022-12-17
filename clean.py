def cleanWord(word):
    a="" 
    wordclone=word
    if (word.find("http"))!=-1:
        return 
    if (word.find("#"))!=-1:
        return 
    if (word.find("@"))!=-1:
        return 
    for i in word:
        if i.isnumeric():
            a=a+i
        if i.isalpha():
            a=a+i
        if i=="\n" or i==" ":
            a=a+" "
    return a