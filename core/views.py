from django.shortcuts import render

def hi(request,n1,n2):
    # pass 不做事
    s = n1+n2

    return render(request,'hi.html',{
        's':s,
    })

def r(requset,start,stop,step):

    start, stop = min(stop, start), max(stop, start)
    rr = range(start, stop + 1, 2)
    return render(requset,'r.html',{
        'rr':rr,

    })
def tag_test(request):
    ll=[1,2,3,4,5,6,7,8]
    return  render(request,'tag_test.html',{
        'll':ll,

    })