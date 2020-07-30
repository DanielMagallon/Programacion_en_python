import collections
from random import choice

Card = collections.namedtuple('Card',["rank","suit"])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = "spades diamonds clubs hearts".split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, pos):
        return self._cards[pos]

deck = FrenchDeck()
print("Size: "+str(len(deck)))

for c in deck:
    print(c)

print("Random...")
print(choice(deck))

print("Deck 12::13=",deck[12::13])

for c in reversed(deck):
    print(c)

print("Card('2','spades')? "+str(Card('2','spades') in deck))
print("Card('22','spades')? "+str(Card('22','spades') in deck))
#list2 = ["Edgar","Daniel"]+["Magallon","Villanueva"]
#print(list2)










class Storage():

    sets={}

    def __setitem__(self, key, value):
        self.sets.__setitem__(key,value)

    def __getitem__(self, key):
        return self.sets.__getitem__(key)

alamacen=Storage()
alamacen["1"]="Edgar"
print("Key 1 contains: "+alamacen["1"])


bob = ('Bob', 30, 'male')
print('Representation:', bob)

jane = ('Jane', 29, 'female')
print('\nField by index:', jane[0])

print('\nFields by index:')
for p in [bob, jane]:
    print('{} is a {} year old {}'.format(*p))