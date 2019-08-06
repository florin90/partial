# lista_noua = []
#
# q = reduce(lambda x, y: x + y, lista[0])
# print(q)

# x0 =  map (lambda z : reduce(lambda x, y : x + y, z), lista )




from functools import reduce
lista = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]

x1 = filter( lambda x: x % 2, list( map (lambda z : reduce(lambda x, y : x + y, z), lista ) ))
print( list( x1))













