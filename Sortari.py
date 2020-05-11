from random import randint
from time import time

def bubble_sort(v, n):
    if n > 3000 :
        return -1
    else :
        ok = 1
        while ok != 0 :
            ok = 0
            for i in range(0, n - 2):
                if v[i] > v[i + 1] :
                    ok = 1
                    aux = v[i]
                    v[i] = v[i + 1]
                    v[i+1] = aux
        return v


def count_sort(v, n):
    if max(v) > 1000000 or min(v) < -1000000 :
        return -1
    else :
        if min(v) < 0 :
            frPoz = (max(v) + 1) * [0]
            frNeg = (-min(v) + 1) * [0]
            for i in v:
                if i < 0 :
                    frNeg[-i] += 1
                else: frPoz[i] += 1
            maxim = max(v)
            minim = min(v)
            j = 0
            for i in range(-minim, 0, -1) :
                while frNeg[i] != 0 :
                    frNeg[i] = frNeg[i] - 1
                    v[j] = -i
                    j = j + 1
            for i in range(0, maxim + 1) :
                while frPoz[i] != 0 :
                    frPoz[i] = frPoz[i] - 1
                    v[j] = i
                    j = j + 1

        else :
            frPoz = (max(v) + 1) * [0]
            maxim = max(v)
            minim = min(v)
            for i in v :
                frPoz[i] = frPoz[i] + 1
            j = 0
            for i in range(minim, maxim + 1) :
                while frPoz[i] != 0 :
                    frPoz[i] = frPoz[i] - 1
                    v[j] = i
                    j = j + 1
        return v

def radix_sort(v, n):
    if n == 0 :
        v = []
        return v
    else :
        mini = 0
        if min(v) < 0:
            mini = min(v)
            for i in range(0, n):
                v[i] -= mini
        if max(v) < 10:
            x = []
            for i in range(0, 10):
                x = x + [[i]]
            for i in range(0, n):
                x[v[i]] = x[v[i]] + [v[i]]
            v = []
            for i in range(0, 10):
                if len(x[i]) > 1:
                    for j in range(1, len(x[i])):
                        v = v + [x[i][j]]
        else:
            exp = 10
            while max(v)//(exp//10) != 0:
                x = []
                for i in range(0, 10) :
                    x = x + [[i]]
                for i in range(0, n) :
                    x[v[i] % exp // (exp//10)] = x[v[i] % exp // (exp//10)] + [v[i]]
                v = []
                for i in range(0, 10) :
                    if len(x[i]) > 1 :
                        for j in range(1, len(x[i])) :
                            v = v + [x[i][j]]
                exp *= 10
        for i in range(0, n) :
            v[i] += mini
        return v

# Am luat si cazurile in care am elemente negative in vector desi acestea nu vor aparea

def merge_sort(v):
    if len(v) > 1:
        m = len(v) // 2
        S = v[: m]
        D = v[m :]
        merge_sort(S)
        merge_sort(D)
        i = j = k = 0
        while i < len(D) and j < len(S):
            if D[i] > S[j]:
                v[k] = S[j]
                j += 1
            else:
                v[k] = D[i]
                i += 1
            k += 1
        while j < len(S):
            v[k] = S[j]
            j += 1
            k += 1
        while i < len(D):
            v[k] = D[i]
            i += 1
            k += 1


def generator(n):
    x = randint(0, n)
    return x


def quick_sort(v, s, d):
    if s < d:
        poz = generator(d - s)
        poz += s
        v[poz], v[s] = v[s], v[poz]
        i = s
        j = d
        i1 = 0
        j1 = -1
        while i < j:
            if v[i] > v[j]:
                v[j], v[i] = v[i], v[j]
                c = i1
                i1 = -j1
                j1 = -c
            i = i + i1
            j = j + j1
        k = i
        quick_sort(v, s, k - 1)
        quick_sort(v, k+1, d)

def quick_sort_din_3(v, s, d):
    if s < d:
        x = v[s]
        y = v[d]
        z = v[(s + d) // 2]
        if x >= y:
            if x <= z:
                poz = s
            elif y >= z:
                    poz = d
            else: poz = (s + d) // 2
        else:
            if x >= z:
                poz = s
            elif y <= z:
                    poz = d
            else: poz = (s + d) // 2
        v[poz], v[s] = v[s], v[poz]
        i = s
        j = d
        i1 = 0
        j1 = -1
        while i < j:
            if v[i] > v[j]:
                v[j], v[i] = v[i], v[j]
                c = i1
                i1 = -j1
                j1 = -c
            i = i + i1
            j = j + j1
        k = i
        quick_sort_din_3(v, s, k - 1)
        quick_sort_din_3(v, k+1, d)

def schimbaza2(x):
    y = x % 2
    x = x // 2
    while x != 0:
        y = y * 10 + x % 2
        x = x // 2
    return y

def schimbaza10(x):
    y = 0
    lung = len(str(x))
    while x != 0:
        y += (x % 10)*(2**(lung - len(str(x))))
        x = x // 10
    return y

def generareVec(n, maxim):
    return [randint(0, maxim) for _ in range(0, n)]


def testare (n, maxim, v):
    aux = v
    g.write("~~~~~Exeplu: n = " + str(n) + ", limita maxima = " + str(maxim - 1) + "\n")

    timp0 = time()
    aux = bubble_sort(aux, n)
    timp1 = time()
    if aux == -1 :
        g.write("Bubble Sort nu a putut sorta deoarece sunt prea multe elemente in vector.\n")
    else :
        test = "A sortat."
        for i in range(0, n - 2):
            if aux[i] > aux[i + 1]:
                test = "EROARE"
        g.write("Bubble Sort: " + test + "  (Timpul in care a sortat: " + str(timp1 - timp0) + " secunde)\n")

    aux = v
    timp0 = time()
    aux = count_sort(aux, n)
    timp1 = time()
    if aux == -1 :
        g.write("Count Sort nu a putut sorta deoarece elementul maxim sau elementul minim din vectore este prea mare/mic.\n")
    else :
        test = "A sortat."
        for i in range(0, n - 2):
                if aux[i] > aux[i + 1]:
                    test = "EROARE"
        g.write("Count Sort: " + test + "  (Timpul in care a sortat: " + str(timp1 - timp0) + " secunde)\n")

    aux = v
    timp0 = time()
    aux = radix_sort(aux, n)
    timp1 = time()
    test = "A sortat."
    for i in range(0, n - 2):
        if aux[i] > aux[i + 1]:
            test = "EROARE"
    g.write("Radix Sort: " + test + "  (Timpul in care a sortat: " + str(timp1 - timp0) + " secunde) -> (cu numere in baza 10)\n")

    aux = v
    timp0 = time()
    for i in range(0, n):
        aux[i] = schimbaza2(aux[i])
    timp2 = time()
    aux = radix_sort(aux, n)
    timp3 = time()
    for i in range(0, n):
        aux[i] = schimbaza10(aux[i])
    timp1 = time()
    test = "A sortat."
    for i in range(0, n - 2):
        if aux[i] > aux[i + 1]:
            test = "EROARE"
    g.write("Radix Sort: " + test + "  (Timpul in care a sortat: " + str(timp1 - timp0) + " secunde) -> (cu numere in baza 2 si transformarea bazelor in timpul de sortare)\n")
    g.write("Radix Sort: " + test + "  (Timpul in care a sortat: " + str(timp3 - timp2) + " secunde) -> (cu numere in baza 2 si transformarea bazelor in afara timpului de sortare)\n")

    aux = v
    timp0 = time()
    merge_sort(aux)
    timp1 = time()
    test = "A sortat."
    for i in range(0, n - 2):
        if aux[i] > aux[i + 1]:
            test = "EROARE"
    g.write("Merge Sort: " + test + "  (Timpul in care a sortat: " + str(timp1 - timp0) + " secunde)\n")

    aux = v
    timp0 = time()
    quick_sort(aux, 0, n - 1)
    timp1 = time()
    test = "A sortat."
    for i in range(0, n - 2):
        if aux[i] > aux[i + 1]:
            test = "EROARE"
    g.write("Quick Sort: " + test + "  (Timpul in care a sortat: " + str(timp1 - timp0) + " secunde -> (pivot random)\n")

    aux = v
    timp0 = time()
    quick_sort_din_3(aux, 0, n - 1)
    timp1 = time()
    test = "A sortat."
    for i in range(0, n - 2):
        if aux[i] > aux[i + 1]:
            test = "EROARE"
    g.write("Quick Sort: " + test + "  (Timpul in care a sortat: " + str(timp1 - timp0) + " secunde) -> (pivot ca mediana din 3)\n")
    g.write("\n")


g = open("teste.out", "w")
f = open("teste.in", "r")
nrTeste = int(f.readline())

while nrTeste != 0 :
    citire = f.readline().split()
    citire[0], citire[1] = int(citire[0]), int(citire[1]) + 1
    v = generareVec(citire[0], citire[1])
    testare(citire[0], citire[1], v)
    nrTeste -= 1
