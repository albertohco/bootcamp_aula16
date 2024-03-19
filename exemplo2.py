class ContaBancaria:
    def __init__(self, saldo=0):
        self.saldo = saldo

    def depositar(self, quantia):
        if quantia > 0:
            self.saldo += quantia
            return True
        return False

    def sacar(self, quantia):
        if 0 < quantia <= self.saldo:
            self.saldo -= quantia
            return True
        return False


# Usando abstração de processos
conta = ContaBancaria(0)
conta.depositar(50)
conta.sacar(20)
print(f"Saldo atual: {conta.saldo}")
