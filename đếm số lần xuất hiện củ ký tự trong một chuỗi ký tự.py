def demkytu():
    text = 'hbcdcjdcd'
    tansuat = {}
    for c in text:
        tansuat[c]=tansuat.get(c,0)+1
    for f in tansuat.items():
        print (f)
if __name__=="__main__":
    demkytu()
