import string

def clean_text(text):
    wordcl=[]
    stop_w={"the","is","a","for","was","i"}
    s=text.lower()
    d=s.split()
    for i in d:
        i=i.translate(str.maketrans("","",string.punctuation))
        word=i.split()
        for i in word:
            if i not in stop_w:
                wordcl.append(i)
    return (wordcl)
def count_words(wordc1):
    wordc={}
    for w in wordc1:
        if w in wordc:
            wordc[w]+=1
        else:
            wordc[w]=1
    return wordc 
def input_number():
    n=int(input("Enter the top value number "))
    return n
def top_words(wordc,n):
    sorted_words = sorted(wordc.items(), key=lambda x: x[1], reverse=True)
    top=sorted_words[0:n]
    return top
def sentiment(wordc1):
    positive={"good","awesome","excellent","wonderful","amazing","fabulous"}
    negative={"bad","trash","poor","slow","hate"}
    positivec=0
    negativec=0
    for word in wordc1:
        if word in positive:
            positivec+=1
        elif word in negative:
            negativec+=1
    if (positivec > negativec ):
        sentiment_l="positive"
    elif (negativec > positivec):
        sentiment_l="negative"
    else:
        sentiment_l="neutral"
    senti_sc=positivec-negativec
    return (sentiment_l,senti_sc)

def main():
    with open("data/feedback.txt" , "r") as f:
        file= f.read()
    wordc1=clean_text(file)
    wordc=(count_words(wordc1))
    n=input_number()
    result=(top_words(wordc,n))
    sent,senti=(sentiment(wordc1))
    #print(result)
    for word,count in result:
        print(word,"->",count)
    print("sentiment= ",sent,"\nsentiment score= ",senti)


if __name__=="__main__":
    main()




