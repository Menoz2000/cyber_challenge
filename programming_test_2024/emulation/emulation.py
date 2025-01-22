# read input 
N = int(input())
#print (N)
program = [input() for _ in range(N)]

#initialize the six variables
variables = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0}

#map to store lable and their line number
labels = {}

#parse instructions and store labels
for i,line in enumerate(program):
    if line.startswith('lab'):
        label = line.split()[1]
        labels[label] = i

#print (labels)
#print (program)

#start execution from first instruction
i = 0
while i < N:
    instruction = program[i]

    if instruction.startswith('add'):
        _, var, num = instruction.split()
        variables[var] += int(num)
        #print (_, var, num)

    elif instruction.startswith('sub'):
        _, var, num = instruction.split()
        variables[var] -= int(num)
        #print (_, var, num)

    elif instruction.startswith('mul'):
        _, var, num = instruction.split()
        variables[var] *= int(num)
        #print (_, var, num)

    elif instruction.startswith('jmp'):
        _, var, num, name = instruction.split()
        if int(num) == int(variables[var]):
            i = labels[name]    #jump to the label, set new instruction pointer
            #print ('jump to ', name)

    #move to next instruction
    i += 1

print (sum(variables.values()))