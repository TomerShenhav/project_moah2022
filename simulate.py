from Fish import Fish

a = Fish('XY',4, 'B', 'g', 'f', 'T')
b = Fish('XX',4, 'b', 'G', 'f', 't')
for i in range(10):
    c = a.create_newborn(b)
    print(c)