# reescreve o file colocando cada palavra em cada linha, elas estao separadas por virgulas

filename = "storiestest.txt"

# abrir o ficheiro
file = open(filename, 'r')
guardar = open("storiestest2.txt", 'w')

# ler o ficheiro
for line in file:
    line = line.replace("\n", "").split(", ")
    for word in line:
        guardar.write(word + "\n")
# fechar o ficheiro
file.close()
guardar.close()


