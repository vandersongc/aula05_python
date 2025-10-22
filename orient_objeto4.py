class Animal:
    def emitir_som(self):
        print('Som genérico')

class Cachorro(Animal):
    def emitir_som(self):
        print('Au Au!')

class Gato(Animal):
    def emitir_som(self):
        print('Miau!')

animais = [Cachorro(),Gato(),Animal()]

for a in animais:
    a.emitir_som()



