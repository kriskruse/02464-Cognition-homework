I = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
# I = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]
N = len(I)
w = 0.1


def Inhibitio(I, N, w):
    Ai = []
    Ai.append(I[0])
    for j in range(1, N - 1):
        Ai.append(I[j] - w * (I[j - 1] + I[j + 1]))
    Ai.append(I[-1])
    return Ai


def Threshold(I, N, w, t):
    index = []
    Ai = []
    for j in range(1, N - 1):

        if t <= abs(I[j - 1] - I[j + 1]):
            Ai.append(I[j] - w * (I[j - 1] + I[j + 1]))
            index.append(j)
    return Inhibitio(I,N,w), Ai, index


print(Threshold(I, N, w, 1))
