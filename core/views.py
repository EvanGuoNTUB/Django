from django.shortcuts import render

def hi(request,n1,n2):
    # pass 不做事
    s = n1+n2

    return render(request,'hi.html',{
        's':s,
    })

def r(requset,start,stop,step):
    if step == 0:
        rr = range(start, stop + 1, 2)
    elif step == 1:

    else
        rr = range(start, stop + 1)

    if start > stop:
        start, stop= stop, start

    #rr=range(start,stop+1,2)
    if start >stop:
        rr=reversed(rr)

    return render(requset,'r.html',{
        'rr':rr,
    })