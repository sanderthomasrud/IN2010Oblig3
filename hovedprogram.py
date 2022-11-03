from funksjonerNy import IMBDGraph

"""
Oppgave 1: Lager grafen
"""
graph = IMBDGraph()
graph.makeGraph("input/movies.tsv", "input/actors.tsv")

"""
Oppgave 2: Skriver ut raskeste vei mellom to noder, tar ikke hensyn til vekt
"""

graph.findShortestPath("nm2255973", "nm0000460") # Donald Glover -> Jeremy Irons
graph.findShortestPath("nm0424060", "nm0000243") # Scarlett Johansson -> Denzel Washington
graph.findShortestPath("nm4689420", "nm0000365") # Carrie Coon -> Julie Delphy
graph.findShortestPath("nm0000288", "nm0001401") # Christian Bale -> Angelina Jolie
graph.findShortestPath("nm0031483", "nm0931324") # Atle Antonsen -> Michael K. Williams

"""
Oppgave 3: Skriver ut raskeste vei mellom to noder, tar hensyn til vekt
"""

graph.chillestPath("nm2255973", "nm0000460") # Donald Glover -> Jeremy Irons
graph.chillestPath("nm0424060", "nm0000243") # Scarlett Johansson -> Denzel Washington
graph.chillestPath("nm4689420", "nm0000365") # Carrie Coon -> Julie Delphy
graph.chillestPath("nm0000288", "nm0001401") # Christian Bale -> Angelina Jolie
graph.chillestPath("nm0031483", "nm0931324") # Atle Antonsen -> Michael K. Williams

"""
Oppgave 4: Skriver ut antall forekomster av størrelsen på komponenter
"""

graph.countNodesInComponents()
