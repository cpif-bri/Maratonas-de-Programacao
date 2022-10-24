from time import time

def maxComumDivisor(x, y):
    if(y==0):
        return x
    else:
        return maxComumDivisor(y,x%y)

n, q = (int(x) for x in input().split(" "))

jogadores = [int(x) for x in input().split(" ")]
casaZero = [-1] * len(jogadores)

st = time()

for j in range(q):
    cq, dq = (int(x) for x in input().split(" "))
    for i in range(n):
        if(jogadores[i] > 0):
            if(maxComumDivisor(i+1, cq) > 1):
                jogadores[i] -= dq
                if(jogadores[i] <= 0):
                    casaZero[i] = j+1
    
    # print(jogadores)
    # print(casaZero)

for final in casaZero:
    print(final)

    
et = time()
# get the execution time
elapsed_time = (et - st)
print('Execution time:', elapsed_time, 'seconds')




# from time import time

# def maxComumDivisor(x, y):
#     if(y==0):
#         return x
#     else:
#         return maxComumDivisor(y,x%y)

# n, q = (int(x) for x in input().split(" "))

# jogadores = [int(x) for x in input().split(" ")]
# casaZero = [-1] * len(jogadores)

# st = time()

# tam = n

# for j in range(q):
#     cq, dq = (int(x) for x in input().split(" "))
#     i = 0
#     k = 0
#     while(i < tam):
#         if(jogadores[i] > 0):
#             if(maxComumDivisor(k+1, cq) > 1):
#                 jogadores[i] -= dq
#                 if(jogadores[i] <= 0):
#                     casaZero[i] = j+1
#                     del jogadores[i]
#                     tam-=1
#                 else:
#                     i+=1
#             else:
#                 i+=1
#         else:
#             i+=1
#         k += 1

# for final in casaZero:
#     print(final)

# et = time()
# # get the execution time
# elapsed_time = (et - st)
# print('Execution time:', elapsed_time, 'seconds')