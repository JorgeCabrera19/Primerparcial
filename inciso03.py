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
 



lista_original = [1, 2, 3, 4, 5]              
print("Lista:", lista_original)
suma = stack
print("Suma lista", sumapar)
