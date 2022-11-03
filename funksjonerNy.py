

from asyncio import queues
from collections import defaultdict
from tracemalloc import start
from numpy import empty
from heapq import heappop, heappush


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

class Edge:
    def __init__(self, actor, movie):
        self.actor = actor
        self.movie = movie
    def __lt__(self, other):
        return float(self.movie.rating) < float(other.movie.rating)
    
    def __str__(self):
        return f"({self.actor}, {self.movie})"

class IMBDGraph:
    def __init__ (self):
        self.allMovies = {} # tt som key, Movie-objekt som value
        self.allActors = {} # nm som key, Actor-objekt som value
        self.graph = {} # Actor-objekt som key, liste med kanter som value
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
                        edge = Edge(otherActor, movie) # danner et par av skuespilleren, og filmen de har spilt sammen i
                        edgeList.append(edge) # legger paret til på listen over kanter
            
            self.graph[thisActor] = edgeList # legger til kantlisten
            self.totalEdges += len(edgeList) # legger til antall kanter til totalen
            self.totalNodes += 1 # legger til en node til totalen

        # dette må legges i en egen funksjon
        # print(f"Oppgave 1\n")
        # print(f"Antall noder: {self.totalNodes}")
        # print(f"Antall kanter: {round(self.totalEdges / 2)}\n")



    def findShortestPath(self, str1, str2):
        self.findPath(self.allActors[str1], self.allActors[str2])


    def findPath(self, startActor, endActor):
        visited = set()

        queue = [startActor]

        paths = {}
        paths[startActor] = []
        visited.add(startActor)

        while len(queue) > 0:
            u = queue.pop(0) # popping the first element in queue
            for edge in self.graph[u]:
                if edge.actor not in visited:
                    queue.append(edge.actor)
                    visited.add(edge.actor)

                    lst1 = paths[u].copy()
                    paths[edge.actor] = lst1
                    lst1.append(Edge(u, edge.movie)) 
            
            if endActor in visited:
                break

        for step in paths[endActor]:
            print(f"{step.actor}\n=== [ {step.movie} ({step.movie.rating}) ===>", end = " ")

        print(f"{endActor}\n")

    def chillestPath(self, str1, str2):
        D = self.findChillestPath(self.allActors[str1], self.allActors[str2])

    def findChillestPath(self, startActor, endActor): # legge til små optimaliseringer for å gjøre den raskere: visited-set, og if test om rating > D[actor]       
        Q = [(0, startActor)]
        D = defaultdict(lambda: float('inf'))
        D[startActor] = 0
        paths = {}
        paths[startActor] = [] 

        while Q:
            # path = []
            rating, actor = heappop(Q)
            if isinstance(actor, Edge):
                actor = actor.actor
            
            for edge in self.graph[actor]:
                # path.append(edge)
                weight = rating + (10.0 - float(edge.movie.rating))
                if weight < D[edge.actor]:
                    
                    lst1 = paths[actor].copy()
                    paths[edge.actor] = lst1
                    lst1.append(Edge(actor, edge.movie)) 

                    D[edge.actor] = weight
                    heappush(Q, (weight, edge)) # cannot get heap to sort on weight              
            # paths.append(path)

        for step in paths[endActor]:
            print(f"{step.actor}\n=== [ {step.movie} ({step.movie.rating}) ===>", end = " ")

        print(f"{endActor}")
        print(f"Total weight: {D[endActor]}\n")
        return D

    def countNodesInComponents(self):
        componentsDict = self.DFSFull()
        sortedComponents = sorted(componentsDict.items(), key=lambda x: x[0], reverse=True)

        for comp in sortedComponents:
            print(f"There are {comp[1]} components of size {comp[0]}")
    
    def DFSVisit(self, node, visited, counter):
        stack = [node]
        while stack:
            u = stack.pop()
            if u not in visited:
                counter += 1
                visited.add(u)
                for kant in self.graph[u]:
                    stack.append(kant.actor)
        
        return counter

        # visited.add(node)
        # counter += 1
        # for kant in self.graph[node]:
        #     if kant.actor not in visited: 
        #         counter = self.DFSVisit(kant.actor, visited, counter)

        # return counter

    
    def DFSFull(self):
        visited = set()
        components = {}

        for actor in self.graph:
            if actor not in visited:
                counter = 0
                counter = self.DFSVisit(actor, visited, counter)
                if counter not in components:
                    components[counter] = 1
                else:
                    components[counter] += 1
        return components




        

