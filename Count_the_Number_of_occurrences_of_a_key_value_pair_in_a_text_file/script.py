f = open("myfile.txt", "r")
d = dict()
 
for res in f:

    res = res.strip()
 
    res = res.lower()
 
    lines = res.split()
 
    for line in lines:
 
        if line in d:
 
            d[line] = d[line]+1
        else:
 
            d[line] = 1
          
f.close()
 
for key in list(d.keys()):
    print("The count of {} is {}".format(key,d[key]))
