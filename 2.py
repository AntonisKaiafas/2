d = open(r"C:\Users\Antonis\Documents\PYTHON\Άσκηση 2\sentence.txt").read().split()
for i in d:
    x1=0
    x2=0
    for j in range (len(i)):
        if i[j]=='f' or i[j]=='c' or i[j]=='k' or i[j]=='r':
            x1 = x1 + 1 
        else:
            x2 = x2 + 1

    if (x1 > x2):
        print("Η λέξη",i,"είναι κακή")
    else:
        print("Η λέξη",i,"είναι καλή")
    
         
