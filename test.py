btnline_Dict = dict()

btnline_Dict[4] = list()
print(btnline_Dict)

btnline_Dict[4].append('A')
btnline_Dict[4].append('B')
btnline_Dict[4].append('C')
print(btnline_Dict)

for i in btnline_Dict[4]:
    i='Z'
btnline_Dict[4][0:2] = 'Z'
print(btnline_Dict[4][0:2])