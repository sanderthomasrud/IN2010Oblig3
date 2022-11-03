class Actor:
    def __init__(self, nm, name):
        self.nm = nm # en unik nm-id
        self.name = name # navn
        self.movies = [] # liste over Movie-objekter skuespilleren har spilt i

    def __repr__(self): # returnerer en string som representerer objektet
        return self.name