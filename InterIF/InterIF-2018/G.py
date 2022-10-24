X = int(input())
Y = int(input())

xHex = (hex((X-1) + (X+1)))
yHex = (hex((Y-1) + (Y+1)))

print(f'X = {xHex[2:len(xHex)].upper()}')
print(f'Y = {yHex[2:len(yHex)].upper()}')