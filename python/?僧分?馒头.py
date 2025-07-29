def js(msg):
    for i in range(msg):
        if i*3+(msg-i)/3==msg:
            return(i,msg-i)
assert(js(100)==(25,75))
