cells = [0]*3
pointer = 0

i = 0
data = list(open('code.tt', 'r').read())

while i < len(data):
    if(data[i] == 'a'):
        cells[pointer] += 2

    elif(data[i] == 'b'):
        cells[pointer] -= 1

    elif(data[i] == 'c'):
        pointer += 1

    elif(data[i] == 'd'):
        pointer -= 2

    elif(data[i] == 'e'):
        print(chr(cells[pointer]), end='')

    elif(data[i] == 'f'):
        print(cells[pointer], end='')

    elif(data[i] == 'g'):
        print('\n', end='')

    elif(data[i] == 'h'):
        cells[pointer] = ord(input())

    elif(data[i] == 'i'):
        if(cells[pointer] <= 0):
            while(data[i] != 'j'):
                i += 1

    elif(data[i] == 'j'):
        if(cells[pointer] > 0):
            while(data[i] != 'i'):
                i -= 1

    elif(data[i] == 'k'):
        while(data[i] != 'l'):
            i += 1

    i += 1
