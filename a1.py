import pandas as pd
import csv
import yaml
d=pd.read_csv('input.csv')
ans={}

j=0
for k in d:
   for i in d[k]:
      dat=i.split("-")
      
      if dat[0] not in ans:
         ans[dat[0]]=[]
         mo={}
         mo[dat[1]]=[]
         mo[dat[1]].append({d['event_type'][j]:int(d['count'][j]),'total':int(d['count'][j])})    
         ans[dat[0]].append(mo)     
      else:
            for x in ans[dat[0]]: 
                if dat[1] not in x:
                  x[dat[1]]=[]
                  x[dat[1]].append({d['event_type'][j]:int(d['count'][j]),'total':int(d['count'][j])})

                else:
                    for y in x[dat[1]]:
                        if d['event_type'][j] not in y:
                            y[d['event_type'][j]]=int(d['count'][j])
                            y['total']=y['total']+int(d['count'][j])
                            
                        else:
                           
                           y[d['event_type'][j]]=y[d['event_type'][j]]+int(d['count'][j])                        
                           y['total']=y['total']+int(d['count'][j])
      j=j+1   
   break     
print(ans)

file= open ('my_yam.yaml','w')
yam=yaml.dump(ans,file)          
