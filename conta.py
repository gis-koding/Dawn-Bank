from flask import flash
from abc import ABC, abstractmethod
from biblioteca import *


'''O que precisa de melhorias: 
-rendimento dinamico
-cheque especial dinamico
-salvamento'''

class Conta(ABC):
    def __init__(self,titular,numconta,saldo):
        self.titular = titular
        self.numconta = numconta
        self.saldo = saldo
    #possivelmente add self.agencia
    #os dados sao verificados antes de instanciar uma conta, diminuindo necessidade de verificar durante op

    @abstractmethod
    def deposito(self,valor):
        pass

    @abstractmethod
    def saque(self,valor):
        pass

    @abstractmethod
    def pix(self,valor,saldo_destino):
        pass

'''Obs: rendimento e cheque fixos por enquanto'''

class Conta_Corrente(Conta):
    def __init__(self, titular, numconta, saldo,especial=200):
        super().__init__(titular, numconta, saldo)
        self.especial = especial
        self.tipo = "corrente" #para salvar no dict json 
        #cheque especial é um saldo separado que só pode ser usado quando saldo é menor do que o valor da op

    def deposito(self, valor):
         #valor não é atributo, definido toda vez que chamarmos a funcao
            if valor <= 0:
                flash("Valor inválido para depósito.", "danger")
            else:
                self.saldo += valor
                flash(f"Depósito de R$ {valor:.2f} realizado com sucesso!", "success")

    def saque(self, valor):
        if valor <= 0:
            flash("Valor inválido para saque.", "danger")
        elif valor > (self.saldo + self.especial):
            flash("Saldo e cheque especial insuficientes.", "danger")
        else:
            self.saldo -= valor
            # Se o saldo ficou negativo, significa que usou o cheque especial
            if self.saldo < 0:
                self.especial += self.saldo # O especial paga a diferença
                self.saldo = 0
                flash(f"Saque de R$ {valor:.2f} realizado com sucesso (usou cheque especial)!", "success")
            else:
                flash(f"Saque de R$ {valor:.2f} realizado com sucesso!", "success")
    
    def pix(self, valor, conta_destino):
        if valor <= 0:
            flash("Valor inválido para transferência.", "danger")
        elif valor > (self.saldo + self.especial):
            flash("Saldo insuficiente para transferência.", "danger")
        else:
            self.saldo -= valor
            if self.saldo < 0:
                self.especial += self.saldo
                self.saldo = 0
            conta_destino.saldo += valor 
            flash(f"Pix de R$ {valor:.2f} enviado com sucesso!", "success")

class Conta_Poupança(Conta):
    def __init__(self, titular, numconta, saldo):
        super().__init__(titular, numconta, saldo)
        self.tipo = "poupança" #para salvar nos json 

    def deposito(self, valor):
     #valor não é atributo, definido toda vez que chamarmos a funcao
        if valor <= 0:
            flash("Valor inválido para depósito.", "danger")
        else:
            self.saldo += valor
            flash(f"Depósito de R$ {valor:.2f} realizado com sucesso!", "success")

    def saque(self, valor):
        if valor <= 0:
            flash("Valor inválido para saque.", "danger")
        elif valor > self.saldo: # <--- Verifica se tem saldo!
            flash("Saldo insuficiente para saque.", "danger")
        else:
             self.saldo -= valor
             flash(f"Saque de R$ {valor:.2f} realizado com sucesso!", "success")

    def rendimento(self):
        self.saldo += self.saldo * 0.05 #rendimento de 5% ao mês
     
    def pix(self, valor, conta_destino):
        if valor <= 0:
            flash("Valor inválido para transferência.", "danger")
        elif valor > self.saldo:
            flash("Saldo insuficiente para transferência.", "danger")
        else:
            self.saldo -= valor
            conta_destino.saldo += valor 
            flash(f"Pix de R$ {valor:.2f} enviado com sucesso!", "success")