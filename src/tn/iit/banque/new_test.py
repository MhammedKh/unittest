# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

import unittest


from Compte import Compte
from Personne  import Personne

class  New_TestCase(unittest.TestCase):

    

    #def tearDown(self):
    #    self.foo.dispose()
    #    self.foo = None

    def test_new_(self):
        #assert x != y;
        #self.assertEqual(x, y, "Msg");
        c=Compte(1,500)
        c2=Compte(2,700)
        p=Personne(1,"Ali","kharrat")
        p.ajouter_compte(c)
        p.ajouter_compte(c2)
        self.assertIn(c2,p.comp)
        

if __name__ == '__main__':
    unittest.main()

