def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1 : name = "mbox-short.txt"
   
    mbox_file = open(name)
    fromdict = {}

    for line in mbox_file: 
        line = line.strip()
        
        if line.startswith("From "):
            sender = line.split()[1]

            if sender not in fromdict:
                fromdict[sender] = 1
            else:
                fromdict[sender] += 1
    dictvals = fromdict.values()
    maxvals = max(dictvals)

    print(max(fromdict, key = fromdict.get),maxvals)

            




#need to make a dictinary 
#sort though the file
# count what we sorted thorugh 
# the program looks for From 
#takes from the 2nd word (3)

        

## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()
