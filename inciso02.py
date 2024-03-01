class Stack:
    def __init__(self):
        self.items = []      

    def push(self, item):
        self.items.append(item)   
    
    def pop(self):
        if not self.is_empty():      
            return self.items.pop()
        else:
            return None
        
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None
        
    
    def is_empty(self):
        return len(self.items) == 0     
    
    def size(self):
        return len(self.items)


def invertir_lista(lista):
    pila = Stack()
    for elemento in lista:
        pila.push(elemento)
 
    lista_invertida = []             
    while not pila.is_empty():
        lista_invertida.append(pila.pop())

    return lista_invertida           


lista_original = [j, o, r, g, e]              
print("Lista original:", lista_original)
lista_invertida = invertir_lista(lista_original)
print("Lita invertida:", lista_invertida)

