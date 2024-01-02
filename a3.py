def ans(a):
    cl={}
    c={}
    c['id']=a['id']
    for x in a['impressions']:

        cl[x['id']]=[]
    for x in a['clicks']:
        if x['id'] in cl:
            cl[x['id']].append(x['cid'])
        else:
            c['missing_events']=[]
            c['missing_events'].append(x)
    b=a
    for x in b['impressions']:
        x['clicks']=cl[x['id']]
        if len(cl[x['id']])>0:
            bo= True
        else:
            bo= False
        x['has_click']=bo
    del b['clicks']
    print('\n')
    print(b)
    print('\n')
    print(c)
    return b
    
    
   


 


a={'id': 'id1', 'impressions': [{'id': 'id1', 'name': 'n1'}, {'id': 'id2', 'name': 'n2'}], 'clicks': [{'id': 'id1', 'cid': 'cid1'}, {'id': 'id1', 'cid': 'cid2'},  {'id': 'id3', 'cid': 'cid4'}]}
b=ans(a)
