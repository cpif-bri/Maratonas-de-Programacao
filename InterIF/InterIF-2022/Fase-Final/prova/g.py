texto = input()
apagados = []
final = ''
i = 0
while(i < len(texto)):
    try:
        if(texto[i] == '<' and (texto[i+1] == 'b' or texto[i+1] == 'B') and (texto[i+2] == '>')):
            apagados.append(final[-1])
            final = final[:-1]
            i += 2
        elif(texto[i] == '<' and (texto[i+1] == 'z' or texto[i+1] == 'Z') and (texto[i+2] == '>')):
            final += apagados.pop()
            i += 2
        else:
            final += texto[i]   
        i += 1
    except:
        final += texto[i]   
        i += 1

print(final)
