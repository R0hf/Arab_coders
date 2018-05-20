st = "alvaro fofo yentrinii alvaro yheb l incline"
print st.replace('alvaro','raouf',1)
stooges = ['Moe','Larry','Curly']
stooges.append('alvaro') # add in last 
#print stooges
word = "tanana" ;
word = word.replace("ta","ba") ;
print word ;
u = raw_input("dakhel 3afssaa madafak") ; # lire 
print u + "hahah" ;
def print_all_elements(p):
    i = 0
    while i < len(p) :
        print p[i]
        i = i + 1

def nextDay(year, month, day):
    if day == 30 :
        day = 1
        if month == 12 :
            month = 1 
            year = year + 1
        else :
            month = month + 1
    else :
        day = day + 1 
        
    return year,month,day 
#print nextDay(2018,12,30) 
#st.split() ; # str to list 
#st.join() ; #list to str        