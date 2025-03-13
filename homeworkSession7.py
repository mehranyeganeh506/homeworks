#1
def max_len(s):
    c = 0
    d = {}
    for i in s :
        if isinstance(i,str):
            d[len(i)] = i
        elif isinstance(i,int):
            item = str (i)
            c = len(item)
            d[c] = i
    a = max(d.keys())
    return d.get(a)

#2
def user_speed(speed) :
    if speed <= 70 :
        print('good')
    elif speed > 70 :
        a = speed - 70
        c = a // 5 
        print(c) 
        if c > 12 :
            print ('your driver license revoked')

#3
def distance (a,b) :
    import math
    x = (b[0] - a[0]) ** 2
    y = (b[1] - a[1]) ** 2
    t = x + y 
    dist = math.sqrt(t) 
    return dist

#4
a = [1,5]
b = [8,5]
c = [8,10]
def align(a,b,c) :
    m1 = (b[1] - a[1]) / (b[0] - a[0])
    m2 = (c[1] - b[1]) / (c[0] - b[0])
    if m1 == m2 :
        return True
    elif m1 != m2 :
        return False

#5
def triangle_type(a,b,c) :
    import math
    t1 =((b[0] - a[0]) ** 2) + ((b[1] - a[1]) ** 2)
    t2 =((c[0] - b[0]) ** 2) + ((c[1] - b[1]) ** 2)
    t3 =((c[0] - a[0]) ** 2) + ((c[1] - a[1]) ** 2)
    ab = math.sqrt(t1)
    bc = math.sqrt(t2)
    ac = math.sqrt(t3)
    if ab == ac == bc :
        print('متساوی الاضلاع')
    elif (ab == math.sqrt((ac**2)+(bc**2))) or (bc == math.sqrt((ac**2)+(ab**2))) or (ac == math.sqrt((ab**2)+(bc**2))) :
        if ab == bc or ab == ac or bc == ac :
            print('قائم الزاویه متساوی الساقین')
        else:
            print('قائم الزاویه ')
    elif ab == bc or ab == ac or bc == ac :
        print(' متساوی الساقین')
    else:
        print('معمولی')

#6
def origin_distance(d):
    m = {}
    for i in a :
        p = a.get(i)
        origin = [0,0]
        b = distance(p,origin)
        m[i] = b
    z = dict(sorted(m.items(),key=lambda item:item[1]))
    return z