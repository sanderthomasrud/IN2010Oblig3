class Movie:
    def __init__(self, tt, title, rating):
        self.tt = tt # en unik tt-id
        self.title = title # tittel
        self.rating = rating # rating
        self.actors = [] # liste over Actor-objekter i filmen

    def __repr__(self): # returnerer en string som representerer objektet
        return self.title