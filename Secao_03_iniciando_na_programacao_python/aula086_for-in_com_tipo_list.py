cadastros = [
    ['Sophia Rodrigues','189.679.207-33','11/05/1993','Feminino'],
    ['Mariana Lima','756.075.763-45','20/05/1974','Feminino'],
    ['Isaac dos Santos','736.554.316-78','10/02/1988','Masculino'],
    ['Paulo Alves','039.682.683-00','03/04/1958','Masculino'],
]


for i in range(len(cadastros)):
    cadastros[i].insert(0, i+1)

    for fixa in cadastros[i]:
        print(fixa)
    
    print()