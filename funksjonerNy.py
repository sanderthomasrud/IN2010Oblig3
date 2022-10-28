

from asyncio import queues
from tracemalloc import start
from numpy import empty


class Movie:
    def __init__(self, tt, title, rating):
        self.tt = tt
        self.title = title
        self.rating = rating
        self.actors = [] # liste over Actor-objekter i filmen

    def __repr__(self):
        return self.title
  
class Actor:
    def __init__(self, nm, name):
        self.nm = nm
        self.name = name
        self.movies = [] # liste over Movie-objekter skuespilleren har spilt i

    def __repr__(self):
        return self.name

class IMBDGraph:
    def __init__ (self):
        self.allMovies = {} # tt som key, Movie-objekt som value
        self.allActors = {} # nm som key, Actor-objekt som value
        self.graph = {} # Actor-objekt som key, liste med pairs som value
        self.totalNodes = 0
        self.totalEdges = 0

    def readMovies(self, filename):
        file = open(filename)

        for line in file:
            parts = line.strip().split("\t") # splitter linjen og fjerner linjeskift
            self.allMovies[parts[0]] = Movie(parts[0], parts[1], parts[2]) # setter tt: Movie

    def readActors(self, filename):
        file = open(filename, "r")

        for line in file:
            parts = line.strip().split("\t") # splitter linjen og fjerner linjeskift

            thisActor = Actor(parts[0], parts[1])
            self.allActors[parts[0]] = thisActor

            actorsMovies = [] # liste med skuespillerens filmer, representert med Movie-objekter

            for tt in parts[2:]: # går gjennom tt-idene til filmene
                if tt in self.allMovies: # sjekker om tt-id finnes i listen over filmer
                    actorsMovies.append(self.allMovies[tt]) 
                    self.allMovies[tt].actors.append(thisActor) # legger skuespilleren til Movie-objektet, representert som Actor-objekt
            
            thisActor.movies = actorsMovies
        

    def makeGraph(self, movieFile, actorFile):
        self.readMovies(movieFile)
        self.readActors(actorFile)

        for nm in self.allActors: # går gjennom nøklene til alle skuespillere
            edgeList = [] # oppretter liste for denne skuespillerens kanter

            thisActor = self.allActors[nm] # lagrer Actor-objektet
            for movie in thisActor.movies: # går gjennom denne skuespillerens filmer
                for otherActor in movie.actors: # går gjennom denne filmens skuespillere
                    if otherActor != thisActor:
                        edge = (otherActor, movie) # danner et par av skuespilleren, og filmen de har spilt sammen i
                        edgeList.append(edge) # legger paret til på listen over kanter
            
            self.graph[thisActor] = edgeList # legger til kantlisten
            self.totalEdges += len(edgeList) # legger til antall kanter til totalen
            self.totalNodes += 1 # legger til en node til totalen

        print(f"Oppgave 1\n")
        print(f"Antall noder: {self.totalNodes}")
        print(f"Antall kanter: {round(self.totalEdges / 2)}\n")



    def test(self, str1, str2):
        self.findPath(self.allActors[str1], self.allActors[str2])


    def findPath(self, startActor, endActor):
        visited = set()

        queue = [startActor]

        paths = {}
        paths[startActor] = []
        visited.add(startActor)

        while len(queue) > 0:
            u = queue.pop(0) # henter ut det første elementet i køen
            for edge in self.graph[u]:
                if edge[0] not in visited:
                    queue.append(edge[0])
                    visited.add(edge[0])

                    lst1 = paths[u].copy()
                    paths[edge[0]] = lst1
                    lst1.append((u, edge[1])) # HVER GANG DEN ITERERER GJENNOM FOR-LOOPEN, LEGGER DEN TIL ETT ELEMENT I DEN SAMME LISTEN, SOM KOPIERES


        for step in paths[endActor]:
            print(f"{step[0]}\n=== [ {step[1]} ({step[1].rating}) ===>", end = " ")

        print(f"{endActor}\n")
            

        

