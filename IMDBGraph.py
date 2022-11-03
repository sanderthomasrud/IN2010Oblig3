

from collections import defaultdict
import queue
from heapq import heappop, heappush
from Actor import Actor
from Edge import Edge

from Movie import Movie

class IMBDGraph:
    def __init__ (self, actors, movies):
        self.allMovies = {} # tt som key, Movie-objekt som value
        self.allActors = {} # nm som key, Actor-objekt som value
        self.graph = {} # Actor-objekt som key, liste med kanter som value
        self.totalNodes = 0 # totale antall noder
        self.totalEdges = 0 # totale antall kanter (telles dobbelt)
        self.makeGraph(actors, movies)

# OPPGAVE 1

    def readMovies(self, filename): # leser inn filmer
        file = open(filename)

        for line in file:
            parts = line.strip().split("\t") # splitter linjen og fjerner linjeskift
            self.allMovies[parts[0]] = Movie(parts[0], parts[1], parts[2]) # setter tt: Movie

    def readActors(self, filename): # leser inn skuespillere
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
        

    def makeGraph(self, movieFile, actorFile): # lager grafen
        self.readMovies(movieFile)
        self.readActors(actorFile)

        for nm in self.allActors: # går gjennom nøklene til alle skuespillere
            edgeList = [] # oppretter liste for denne skuespillerens kanter

            thisActor = self.allActors[nm] # lagrer Actor-objektet
            for movie in thisActor.movies: # går gjennom denne skuespillerens filmer
                for otherActor in movie.actors: # går gjennom denne filmens skuespillere
                    if otherActor != thisActor:
                        edge = Edge(otherActor, movie) # danner et par av skuespilleren, og filmen de har spilt sammen i
                        edgeList.append(edge) # legger paret til på listen over kanter
            
            self.graph[thisActor] = edgeList # legger til kantlisten
            self.totalEdges += len(edgeList) # legger til antall kanter til totalen
            self.totalNodes += 1 # legger til en node til totalen

        self.printGraphNumbers()
    
    def printGraphNumbers(self): # skriver ut antall noder og kanter i grafen
        print(f"Antall noder: {self.totalNodes}")
        print(f"Antall kanter: {round(self.totalEdges / 2)}\n")

# OPPGAVE 2

    def getShortestPath(self, str1, str2): # finner og skriver ut stien fra startnode til sluttnode
        startActor = self.allActors[str1]
        endActor = self.allActors[str2]

        paths = self.BFS(startActor, endActor)
        self.printPath(paths[endActor], endActor)

    def BFS(self, startActor, endActor): # bredde-først-søk som returnerer alle stier fra startnode
        visited = set() # set som inneholder alle besøkte noder

        queueueue = [startActor]

        paths = {} # dict som inneholder alle stier
        paths[startActor] = []
        visited.add(startActor)

        while queueueue: # while køen ikke er tom 
            u = queueueue.pop(0) # henter første element i køen
            for edge in self.graph[u]: # går gjennom alle kantene til noden
                if edge.actor not in visited:
                    queueueue.append(edge.actor)
                    visited.add(edge.actor)

                    lst1 = paths[u].copy() # kopierer stien til forrige node
                    paths[edge.actor] = lst1 # setter stien til denne noden lik som forrige
                    lst1.append(Edge(u, edge.movie)) # legger til siste kant
            
            if endActor in visited: # om sluttnoden er besøkt, break
                break

        return paths 

    def printPath(self, path, endActor): # skriver ut stien
        for step in path:
            print(f"{step.actor}\n=== [ {step.movie} ({step.movie.rating}) ===>", end = " ")

        print(f"{endActor}\n")

# OPPGAVE 3

    def getChillestPath(self, str1, str2): # hjelpemetode som kaller på dijkstra
        startActor = self.allActors[str1]
        endActor = self.allActors[str2]

        self.dijkstra(startActor, endActor)

    def dijkstra(self, startActor, endActor): # finner og skriver ut stien fra startnode til sluttnode  
        queue = [(0, startActor)] # kø med noder som skal gås gjennom 
        D = defaultdict(lambda: float('inf')) # dict som inneholder totalvekten til den chilleste stien til alle noder (default vekt er uendelig)

        D[startActor] = 0
        paths = {} # dict som inneholder stien til alle noder
        paths[startActor] = [] 

        while queue: # while køen ikke er tom 
            rating, actor = heappop(queue) # henter element med høyest prioritet i heapen
            if isinstance(actor, Edge): # sjekker om elementet er en Edge eller en Actor, evt gjør om til Actor
                actor = actor.actor
            
            if rating <= D[actor]: # hvis denne filmens rating er lavere enn den tidligere totalvekten, kjør
                for edge in self.graph[actor]: # går gjennom alle kantene til noden
                    weight = rating + (10.0 - float(edge.movie.rating)) # oppdaterer vekten til stien
                    if weight < D[edge.actor]: # sjekker om den nye vekten er mindre enn den forrige
                        
                        lst1 = paths[actor].copy() # kopierer stien til forrige node
                        paths[edge.actor] = lst1 # setter stien til denne noden lik som forrige
                        lst1.append(Edge(actor, edge.movie)) # legger til siste kant

                        D[edge.actor] = weight
                        heappush(queue, (weight, edge)) # cannot get heap to sort on weight              

        self.printPath(paths[endActor], endActor) # skriver ut stien
        self.printWeight(D, endActor) # skriver ut vekten

    def printWeight(self, weights, endActor): # skriver ut totalvekten av stien
        print(f"Total weight: {weights[endActor]}\n")

# OPPGAVE 4

    def countNodesInComponents(self): # teller antall forekomster av komponenter av ulik størrelse og skriver ut resultater
        componentsDict = self.DFSFull() # dict som inneholder resultater
        sortedComponents = sorted(componentsDict.items(), key=lambda x: x[0], reverse=True) # sorterer resultater

        for comp in sortedComponents: # skriver ut resultater
            print(f"There are {comp[1]} components of size {comp[0]}")
    
    def DFSFull(self): # returnerer en dict med alle komponenter
        visited = set() # set som inneholder alle besøkte noder
        components = {}

        for actor in self.graph: # går gjennom alle noder i grafen
            if actor not in visited: # hvis noden ikke er besøkt enda
                counter = 0
                counter = self.DFSVisit(actor, visited, counter) # teller antall noder i komponenten

                if counter not in components: # sjekker om det finnes noen forekomster av denne størrelsen tidligere
                    components[counter] = 1 # lager evt en ny key
                else:
                    components[counter] += 1 # legger til en forekomst av denne størrelsen

        return components # returnerer alle komponenter

    def DFSVisit(self, node, visited, counter): # rekursiv metode som returnerer antall noder i en komponent
        stack = [node] # stack som inneholder noder som skal gås gjennom 

        while stack: # while stacken ikke er tom 
            u = stack.pop() # henter elementet som sist ble lagt til 
            if u not in visited: # sjekker om noden er besøkt
                counter += 1
                visited.add(u)
                for kant in self.graph[u]: # går gjennom alle kantene til noden og legger den til på stacken
                    stack.append(kant.actor)
        
        return counter





        

