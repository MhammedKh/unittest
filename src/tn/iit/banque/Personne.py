# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor


from Compte import Compte
class  Personne():
    
    def __init__(self, cin, nom, prenom):
        self.cin=cin
        self.nom = nom
        self.prenom = prenom
        self.comp = []
        
    def ajouter_compte(self, compte):
        self.comp.append(compte)
        
    def supprimer_compte(self, compte):
        self.comp.remove(compte)
        
    def affiche_nbr_compte(self):
        print str(self.cin),"a ",str(len(self.comp)),"compte"
        
    def debuter_compte(self,num,montant):
        for s in range(len(self.comp)):
            if s.num==num:
                s.debuter_solde(montant)
                
    def crediter_compte(self,num,montant):
        for s in self.comp:
            if s.num==num:
                s.crediter_solde(montant)
                
                
    def affiche_solde_compte(self,num):
        for s in self.comp:
            if() s.num==num:
                 print "le compte a contient ",str(s.solde),"dinars"
            
        
     
            
        
            
    
        
    
    
