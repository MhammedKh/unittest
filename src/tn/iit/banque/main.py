# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from Personne import Personne
from Compte import Compte
if __name__ == "__main__":
    c=Compte(1,500)
    c2=Compte(2,700)
    p=Personne(1,"Ali","kharrat")
    p.ajouter_compte(c)
    p.ajouter_compte(c2)
    p.crediter_compte(1,100)
    p.affiche_solde_compte(1)
    p.affiche_solde_compte(1)
