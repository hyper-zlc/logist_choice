


from collections import Counter     # 用Counter的话统计不到abcd中没有的字符，自己写一个函数更适合
from time import time

def is_colse(c1,c2):
    d1={'a':'b','b':'c','c':'d','d':'e'}
    d2 = {'a': '0', 'b': 'a', 'c': 'b', 'd': 'c'}
    if d1[c1]==c2 or d2[c1]==c2:
        return True
    return False
t=time()
k=['a','b','c','d']
for i1 in k:
    for i2 in k:
        for i3 in k:
            for i4 in k:
                for i5 in k:
                    for i6 in k:
                        for i7 in k:
                            for i8 in k:
                                for i9 in k:
                                    for i10 in k:
                                        if (i4 == 'a' and i1 == i5) or (i4 == 'b' and i2 == i7) or (
                                                i4 == 'c' and i1 == i9) or (i4 == 'd' and i10 == i6):
                                            if (i2=='a' and i5=='c') or(i2=='b' and i5=='d') or(i2=='c' and i5=='a') or(i2=='d' and i5=='b') :
                                                if (i6 == 'a' and set(i2 + i4 + i8).__len__() == 1) or (
                                                        i6 == 'b' and set(i1 + i6 + i8).__len__() == 1) or (
                                                        i6 == 'c' and set(i3 + i10 + i8).__len__() == 1) or (
                                                        i6 == 'd' and set(i5 + i9 + i8).__len__() == 1):
                                                    if set(i5 + i8 + 'a').__len__() == 1 or set(
                                                        i5 + i4 + 'b').__len__() == 1 or set(
                                                        i5 + i9 + 'c').__len__() == 1 or set(
                                                        (i5, i7, 'd')).__len__() == 1:
                                                        if ('a' not in set(i6+i2+i4) and i3=='a' ) or(i3=='b' and i6 not in set('b'+i2+i4)) or \
                                                                (i3 == 'c' and i2 not in set(i3+ i6+ i4)) or (i3=='d' and i4 not in set(i3+i2+i6)):
                                                            if (i8 == 'a' and not is_colse(i7, i1)) or (
                                                                    i8 == 'b' and not is_colse(i5, i1)) or (
                                                                    i8 == 'c' and not is_colse(i2, i1)) or (
                                                                    i8 == 'd' and not is_colse(i10, i1)):
                                                                if (i9 == 'a' and ((i1 == i6) ^ (i6 == i5))) or (
                                                                        i9 == 'b' and ((i1 == i6) ^ (i10 == i5))) or (
                                                                        i9 == 'c' and ((i1 == i6) ^ (i2 == i5))) or (
                                                                        i9 == 'd' and ((i1 == i6) ^ (i9 == i5))):
                                                                    c=list(dict(Counter((i1,i2,i3,i4,i5,i6,i7,i8,i9,i10))).items())
                                                                    cm,m=min(c,key=lambda x:x[1])
                                                                    if (i7=='a' and cm=='c') or(i7=='b' and cm=='b') or(i7=='c' and cm=='a') or(i7=='d' and cm=='d') :
                                                                        ma=max(c,key=lambda x:x[1])[1]
                                                                        if (i10=='a' and ma-m==3) or(i10=='b' and ma-m==2) or(i10=='c' and ma-m==4) or(i10=='d' and ma-m==1) :
                                                                            print(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10)
                                                                            print('passed time: ',time()-t)



#
#

# k=['a','b','c','d']
# from collections import Counter
# from time import time
# from random import  shuffle
#
# def is_colse(c1, c2):
#     d1 = {'a': 'b', 'b': 'c', 'c': 'd', 'd': 'e'}
#     d2 = {'a': '0', 'b': 'a', 'c': 'b', 'd': 'c'}
#     if d1[c1] == c2 or d2[c1] == c2:
#         return True
#     return False
#
#
# def f2():
#     if i2 + i5 in ['ac', 'ca', 'bd', 'db']:
#         return True
#
#
# def f3():
#     if ('a' not in set(i6 + i2 + i4) and i3 == 'a') or (
#             i3 == 'b' and i6 not in set('b' + i2 + i4)) or \
#             (i3 == 'c' and i2 not in set(i3 + i6 + i4)) or (
#             i3 == 'd' and i4 not in set(i3 + i2 + i6)):
#         return True
#
#
# def f4():
#     if (i4 == 'a' and i1 == i5) or (i4 == 'b' and i2 == i7) or (
#             i4 == 'c' and i1 == i9) or (i4 == 'd' and i10 == i6):
#         return True
#
#
# def f5():
#     if set(i5 + i8 + 'a').__len__() == 1 or set(
#             i5 + i4 + 'b').__len__() == 1 or set(
#         i5 + i9 + 'c').__len__() == 1 or set((i5, i7, 'd')).__len__() == 1:
#         return True
#
#
# def f6():
#     if (i6 == 'a' and set(i2 + i4 + i8).__len__() == 1) or (
#             i6 == 'b' and set(i1 + i6 + i8).__len__() == 1) or (
#             i6 == 'c' and set(i3 + i10 + i8).__len__() == 1) or (
#             i6 == 'd' and set(i5 + i9 + i8).__len__() == 1):
#         return True
#
#
# def f7():
#     if (i7 == 'a' and cm == 'c') or (i7 == 'b' and cm == 'b') or (i7 == 'c' and cm == 'a') or (
#             i7 == 'd' and cm == 'd'):
#         return True
#
#
# def f8():
#     if (i8 == 'a' and not is_colse(i7, i1)) or (i8 == 'b' and not is_colse(i5, i1)) or (
#             i8 == 'c' and not is_colse(i2, i1)) or (i8 == 'd' and not is_colse(i10, i1)):
#         return True
#
#
# def f9():
#     if (i9 == 'a' and ((i1 == i6) ^ (i6 == i5))) or (i9 == 'b' and ((i1 == i6) ^ (i10 == i5))) or (
#             i9 == 'c' and ((i1 == i6) ^ (i2 == i5))) or (i9 == 'd' and ((i1 == i6) ^ (i9 == i5))):
#         return True
#
#
# def f10():
#     if (i10 == 'a' and ma - m == 3) or (i10 == 'b' and ma - m == 2) or (i10 == 'c' and ma - m == 4) or (
#             i10 == 'd' and ma - m == 1):
#         return True
#
#
# seq = [2, 3, 4, 5, 6, 8, 9]
# shuffle(seq)
# s1, s2, s3, s4, s5, s6, s7 = [eval('f' + str(i)) for i in seq]
# print(seq)
#
#
# t=time()
# for i1 in k:
#     for i2 in k:
#         for i3 in k:
#             for i4 in k:
#                 for i5 in k:
#                     for i6 in k:
#                         for i7 in k:
#                             for i8 in k:
#                                 for i9 in k:
#                                     for i10 in k:
#                                         if s1() and s2() and s3() and s4() and s5() and s6() and s7():
#                                             # if f2() and f3() and f4() and f5() and f6() and f8() and f9():
#                                             c = list(dict(Counter((i1, i2, i3, i4, i5, i6, i7, i8, i9, i10))).items())
#                                             cm, m = min(c, key=lambda x: x[1])
#                                             ma = max(c, key=lambda x: x[1])[1]
#                                             if f7() and f10():
#                                                 # print(i1, i2, i3, i4, i5, i6, i7, i8, i9, i10)
#                                                 t1=time() - t
#                                                 if t1<0.15:
#                                                     with open('shuffle_time.txt','a') as file:
#                                                         file.write(str(seq))
#                                                         file.write('\t\t'+str(t1)+'\n')
#
#












# c=list(dict(Counter('asddsadasdsadas')).items())
# m=min(c,key=lambda x:x[1])
# print(m)

