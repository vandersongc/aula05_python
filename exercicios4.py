'''
4. Crie uma classe Animal com método falar().

'''
print('='*45)
print('\n Atividade 4\n')

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

print('='*45)