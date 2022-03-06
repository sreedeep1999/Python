y={'Jomy':10,'Sreedeep':100,'Prasanth':15,'Andrews':30,'Jomy':20} 
                                         
l=list(y.items())    
l.sort()         
print('Ascending order is',l)  

l=list(y.items())
l.sort(reverse=True)  
print('Descending order is',l)

dict=dict(l)  

print(" Sorted Dictionary :",dict)  
