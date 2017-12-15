def Chi_sorted(input, output):
    
    D = {}
    for line in open(input):
        items = line.strip().split(" ")
        if len(items)==2:
	   #items2 = items[1].strip().split(".")
           D[items[0]] = items[1]
   
    #fout = open(output, 'w') 
    list=sorted(D.iteritems(), key=lambda d:d[1], reverse = True )
    k=0
    for obj in list:
	k+=1
	if k<5001:
    	    print >> fout,obj[0]+" "+obj[1]

#input='IT'
#output='IT_sorted'
Com=['Ad_media','consumer_goods','energy_environmental','IT','Machine_manufacturing','buliding','education','farm_forest_animal_fish_other','medical','transportation_logistics','car','electrocommunication','finance','life_service','professional_services','unprofitable_firm']
output='fst_Chi_sorted'
fout = open(output, 'w')
for input in Com:
    Chi_sorted(input, output)
fout.close
