def find_max_combination(s, d):
    def esplora(i, A, B):

        #caso base, tutti gli elementi sono stati esplorati
        if i == len(s):
            return len(A)+len(B)
        
        #prendo l'elemento corrente
        elem = s[i]
        max_dim = 0

        #provo ad aggiungere l'eemento ad A
        if all(abs(elem - x) <= d for x in A):
            max_dim = max(max_dim, esplora(i + 1, A + [elem], B))
        
        #provo ad aggiungere l'eemento ad A
        if all(abs(elem - x) <= d for x in B):
            max_dim = max(max_dim, esplora(i + 1, A, B + [elem]))
        
        #provo a non usare l'elemento corrente
        max_dim = max(max_dim, esplora(i + 1, A, B))

        return max_dim

    return esplora(0, [], [])
        




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
        print (find_max_combination(s,d))
