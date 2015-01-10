# $N tot
# $C per choc
# +1 for every M chocs
# how many does bob get? chocs

# IO -> T \n n c m ,t lines

T = int(input())

for i in range(T):

    N,C,M = str(input()).split()
    N,C,M = map(lambda x: int(x),[N,C,M])
    choc = N//C
    wrapper = N//C
    while wrapper >= M:
        wrapper = wrapper - M + 1
        choc+=1
    answer = choc
    # Compute Answer
    print(answer)

