def My_Loop(li):
    iterator=iter(li)

    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break

L=[1,2,3]
tu=(10,20,30)
se={1,2,3}
dic= {1:2,2:4}

My_Loop(L)
My_Loop(tu)
My_Loop(se)
My_Loop(dic)