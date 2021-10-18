from models.cliente import Cliente
from models.conta import Conta

marcelo: Cliente = Cliente('Marcelo PONTES', 'marcelopontes.tele@gmail.com', '016.807.964-02', '07/04/1994')

print(marcelo)

contaf: Conta = Conta(marcelo)

print(contaf)
