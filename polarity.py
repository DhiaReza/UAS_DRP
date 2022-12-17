from textblob import TextBlob

def polar(sentence, dict):
    a = ""
    for i in sentence:
        a = a + i + " "
    print(a)
    sentence = TextBlob(a)
    b = sentence.sentiment[0]
    if b < 0.0:
        dict["neg"] += 1
        print("neg")
    elif b > 0.0:
        dict["pos"] += 1
        print("pos")
    else:
        dict["neut"] += 1
        print("neut")
    c = sentence.sentiment[1]
    d = str(b) + "," + str(c)
    print(sentence.sentiment)
    return d
    