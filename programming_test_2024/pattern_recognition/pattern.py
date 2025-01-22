def contains_invalid_chars(s, valid_chars):
    for char in s:
        if char not in valid_chars:
            return True  # Restituisce True se c'è un carattere non valido
    return False  # Restituisce False se tutti i caratteri sono validi

def unique_characters(s):
    unique_chars = []
    for char in s:
        if char not in unique_chars:
            unique_chars.append(char)
    return unique_chars

def find_repeating_substrings(x):
    n = len(x)
    result = set()

    # Testiamo tutte le possibili lunghezze di y
    for length in range(1, n + 1):
        y = x[:length]
        valid = False
        i = 0
        #print("stringa analisi corrente:",y)
        valid = False
        '''if n % length == 0:
            if x == y * int(n / length):
                ##print (x, y * int(n / length))
                #print("validata nel modo base")
                #print()
                valid = True
        '''
        
        if x.startswith(y) and valid == False:
            x_cpy = x[len(y):]
            #print ("prima troncata: ",x_cpy)
            while x_cpy != "":
                
                iter = False
                j = 0
                #print("prima ripetizione")
                while j<len(y):
                    #print(">>",y[:j])
                    #print(">>",y[j:])
                    #print(">>", x[len(x)-len(x_cpy)-j:],x[len(x)-len(x_cpy)-j:len(x)-len(x_cpy)-1])
                    #print("--")
                    
                    if x_cpy.startswith(y[j:]) and y[:j] == x[len(x)-len(x_cpy)-j:len(x)-len(x_cpy)]:
                        ###print("V")
                        
                        x_cpy = x_cpy[len(y)-j:]
                        #print("troncate successive: ",x_cpy, y[j:])
                        iter = True
                        break
                    j += 1
                if iter == False:
                    
                    break
                    
            ##print()
            if x_cpy == "":
                
                valid = True
                    





        # Se è valida, aggiungi y ai risultati
        if valid:
            ##print(y)
            ##print()
            result.add(y)
        ##print()

    return len(result)

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    n_testcases = int(data[0])
    ###print(n_testcases)

    i = 1
    while i < n_testcases*3:
        ###print(data[i])
        
        n, m = map(int, data[i].split())
        ###print(n, m)

        alf = list(str(data[i + 1]))
        ###print(alf)

        x = str(data[i + 2])
        ##print("stringa da controllare: ", x)
        ##print()

        print(find_repeating_substrings(x))

        i += 3

        #print()
        #print("________________________________________________________")
        #print()
