with open("data/feedback.txt" , "r") as f:
    c= f.read()
def clean_feedback():
    s=c.lower()
    d=s.split("\n")
    positive=["good" , "awesome","excellent","amazing"]
    negative=["bad","terrible","hate"]
    pcount=0
    ncount=0
    for i in d:
        i=i.replace(".","")
        i=i.replace("?","")
        i=i.replace("!","")
        print(i)
        word=i.split()
        print(len(word))
        for i in word:
            if i in positive:
                pcount+=1
            elif i in negative:
                ncount+=1
    print("positive count =",pcount)
    print("negative count =",ncount)


clean_feedback()




