
import numpy
# O foco do numpy é a crialçao de arrays e operações nos mesmos
# Para criar um numpy array é possível fazer o seguinte:
python_list = [1, 2, 3]
# Utilizar o método array() em uma lista já existente
numpy_array = numpy.array(python_list)
# Utilizar o método array() no momento de criação da lista
numpy_array = numpy.array([1, 2, 3])
# Troque para True para roda o código
if False:
    print(numpy_array)
# Também é possível criar matrizes em numpy e transformá-las em array
numpy_matriz = numpy.array([[1, 2 ,3], [4, 5, 6]])

### Built-in Methods ###
if False:
    # É possível criar um array com valores uniformemente espaçados
    print(numpy.arange(0, 10)) # mesmo que numpy.arange(10)
    # Também é possível determinar intervalos com o método arrange()
    print(numpy.arange(0, 10, 2))
    # OBS: O parametro de finalização não é incluso no resultado

### Gerar Matrizes ###
if False:
    # É possível criar matrizes de zeros e ums para operações de algebra linear
    print(numpy.zeros(3))
    print(numpy.ones(3))
    print("")
    # Também é possível criar matrizes passando uma tupla como argumento
    print(numpy.zeros((3, 3)))
    print(numpy.ones((3, 3)))
    print("")
    # Também existe um método para a criação de uma matriz identidade
    print(numpy.eye(3))

### Matrizes randomicas ###
if False:
    # O numpy possui métodos imbutidos que te permitem criar vetores e matrizes randomicos
    # random.rand() cria uma amostra uniforme
    print(numpy.random.rand(3))
    # Todos valores criados randomicamente pelo random.rand() serão entre 0 e 1
    # É possível aumentar seu valor realizando uma multiplicação
    print(numpy.random.rand(3) * 100) # Retorna valores randomicos entre 0 e 100
    # Para criar uma amostra que não seja uniforme:
    not_uniform = numpy.random.randn(3)
    # Troque para True pra printar a matriz não uniforme
    if False:
        print(not_uniform)

### Reconstrução (Reshape) ###
if False:
    # Criando vetor de 10 valores
    initial_matriz = numpy.arange(10)
    # Printando vetor
    print(initial_matriz)
    # Transformando o vetor em uma matriz 5 x 2
    print(initial_matriz.reshape(5, 2))
    # É possível extrair o shape de uma matriz
    matriz = numpy.random.rand(5, 5) * 50
    print(matriz)
    # Extraindo valor
    print(matriz.shape)

### Extração de valores especificos ###
if False:
    # Extrair valor máximo de uma matriz/vetor
    array = numpy.arange(10)
    array_max = array.max()
    # Extrair posição do valor máximo
    array_max_pos = array.argmax()
    # Extrair valor minímo de uma matriz/vetores
    array_min = array.min()
    #Extrair posição de valor minimo
    array_min_pos = array.argmin()
