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

    def saque(self,valor):
        if valor <= 0:
            flash("Valor inválido para saque.", "danger")
        else:
            if valor < self.saldo:
                self.saldo -= valor
                flash(f"Saque de  R$ {valor:.2f} realizado com sucesso!", "success")
            elif valor > self.saldo and self.especial > valor:
                self.especial -= valor
                flash(f"Saque de  R$ {valor:.2f} realizado com sucesso!(do cheque especial)", "success")
            else:
                flash("Saldo insuficiente para transferência.", "danger")
                
    def pix(self,valor,saldo_destino):
        if valor <= 0:
            flash("Valor inválido para transferência.", "danger")
        else:
            if self.saldo < valor and self.especial < valor:
                flash("Saldo insuficiente para transferência.", "danger")
            elif self.saldo > valor:
                self.saldo -= valor
                saldo_destino += valor
                flash(f"Pix de R$ {valor:.2f} enviado com sucesso!", "success")
            else:
                self.especial -= valor
                saldo_destino += valor
                flash(f"Pix de R$ {valor:.2f} enviado com sucesso!(do cheque especial)", "success")

class Conta_Poupança(Conta):
    def __init__(self, titular, numconta, saldo):
        super().__init__(titular, numconta, saldo)
        self.tipo = "corrente" #para salvar nos json 

    def deposito(self, valor):
     #valor não é atributo, definido toda vez que chamarmos a funcao
        if valor <= 0:
            flash("Valor inválido para depósito.", "danger")
        else:
            self.saldo += valor
            flash(f"Depósito de R$ {valor:.2f} realizado com sucesso!", "success")

    def saque(self, valor):
        if valor <= 0:
            flash("Saldo insuficiente ou valor inválido para saque.", "danger")
        else:
             self.saldo -= valor
             flash(f"Saque de  R$ {valor:.2f} realizado com sucesso!", "success")

    def rendimento(self):
        self.saldo += self.saldo * 0.05 #rendimento de 5% ao mês
     
    def pix(self, valor, saldo_destino):
        if valor <= 0:
            flash("Valor inválido para transferência.", "danger")
        else:
            if self.saldo < valor:
                flash("Saldo insuficiente para transferência.", "danger")
            else:
                self.saldo -= valor
                saldo_destino += valor
                flash(f"Pix de R$ {valor:.2f} enviado com sucesso!", "success")

