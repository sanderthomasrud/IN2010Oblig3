
class Edge:
    def __init__(self, actor, movie):
        self.actor = actor # skuespilleren som er i enden av kanten
        self.movie = movie # filmen som kobler skuespillerene sammen

    def __lt__(self, other): # spesialmetode som gjør at Edge-objekter sammenlignes basert på rating
        return float(self.movie.rating) < float(other.movie.rating)
    
    def __repr__(self): # returnerer en string som representerer objektet
        return f"({self.actor}, {self.movie})"