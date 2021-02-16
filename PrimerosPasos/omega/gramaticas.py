
class Gramatica:

    # Terminales = [id class num +]
    # NO TERMINALES = [A B C D]
    # A --> idBCnum | classD
    # B --> num | +


    def __init__(self,terminals,no_terminals,begin_nterminal,**prods):
        self._terminals = terminals
        self._no_terminals = no_terminals
        self._begin_nterminal = begin_nterminal
        self._prods = prods
        self.firsts_of = {}

    def execute(self):
        self.firsts()

    def firsts(self):

        for nterm in self._no_terminals:
            #print("Primeros(%s) = { %s }" % (nterm,self.get_prod(nterm)))
            fst = set()
            self.get_prod(nterm,fst)

            self.firsts_of[nterm] = fst

        for fp in self.firsts_of.keys():
            print("Primeros(%s) -> %s" % (fp,self.firsts_of[fp]))

        print(self.firsts_of['A'] & self.firsts_of['B'])

    def follows(self):
        ...

    def get_prod(self,nt,set_array):

        for prod in self._prods[nt]:
            if prod[0] in self._no_terminals:
                self.get_prod(prod[0],set_array)
            else:
                set_array.add(prod[0])




T = ['id','class','num','+','-']
NT = ['A','B','C','D']

P = {'A': [('id','B','C','num'),('class','D'),('-',)],
     'B': [('num',),('+',),('A',)],
     'C': [('+','num','-','id'),('none',)],
     'D': [('B','C'),('A',),('none',)]}


gram = Gramatica(terminals=T,no_terminals=NT,begin_nterminal='A',**P)
gram.execute()
