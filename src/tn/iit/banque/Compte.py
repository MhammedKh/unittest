# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class  Compte():
    
    def __init__(self,  solde,numero):
        self.num=numero
        self.s=solde
        
             
    def debuter_solde(self, montant):
        self.s+=montant
        
    def crediter_solde(self, montant):
        self.s-=montant
    def affiche_solde(self):
        print str(self.s)
