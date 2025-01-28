def find_max_combo(s, d):
    def explore(i, A, B, minA, minB):
        
        #caso base
        if i == len(s):
            return len(A) + len(B)
        
        #prendo l'elemento corrente
        elem = s[i]
        max_dim = 0

        #provo a non usare l'elemento corrente
        max_dim = max(max_dim, explore(i+1, A, B, minA, minB))

        #provo ad aggiungere l'elemento ad A
        if abs(elem - minA) <= d or len(A) == 0:
            if elem < minA:
                #print(max_dim)
                minA = elem
            max_dim = max(max_dim, explore(i+1, A+[elem], B, minA, minB))

        #provo ad aggiungere l'elemento a B
        if abs(elem - minB) <= d or len(B) == 0:
            if elem < minB:
                #print(max_dim)
                minB = elem
            max_dim = max(max_dim, explore(i+1, A, B+[elem], minA, minB))

        

        return max_dim
    return explore(0, [], [], 2**60, 2**60)


        
        # Legge l'input
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split("\n")

    T = int(data[0])
    test_cases = []

    index = 1
    for _ in range(T):
        n, d = map(int, data[index].split())
        s = list(map(int, data[index + 1].split()))
        test_cases.append((d, s))
        index += 2

    for d, s in test_cases:
        s.sort()
        print (find_max_combo(s,d))
