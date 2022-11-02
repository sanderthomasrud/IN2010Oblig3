from funksjonerNy import IMBDGraph

graph = IMBDGraph()

graph.makeGraph("input/movies.tsv", "input/actors.tsv")

#graph.findShortestPath("nm0000313", "nm0001745") # Jeff Bridges -> Stellan Skarsgård # findShortestPather i den lille grafen

# graph.findShortestPath("nm2255973", "nm0000460") # Donald Glover -> Jeremy Irons
# graph.findShortestPath("nm0424060", "nm0000243") # Scarlett Johansson -> Denzel Washington
# graph.findShortestPath("nm4689420", "nm0000365") # Carrie Coon -> Julie Delphy
# graph.findShortestPath("nm0000288", "nm0001401") # Christian Bale -> Angelina Jolie
# graph.findShortestPath("nm0031483", "nm0931324") # Atle Antonsen -> Michael K. Williams


# graph.chillestPath("nm0000313", "nm0001745") # Jeff Bridges -> Stellan Skarsgård # chillestPather i den lille grafen

graph.chillestPath("nm2255973", "nm0000460") # Donald Glover -> Jeremy Irons
graph.chillestPath("nm0424060", "nm0000243") # Scarlett Johansson -> Denzel Washington
graph.chillestPath("nm4689420", "nm0000365") # Carrie Coon -> Julie Delphy
graph.chillestPath("nm0000288", "nm0001401") # Christian Bale -> Angelina Jolie
graph.chillestPath("nm0031483", "nm0931324") # Atle Antonsen -> Michael K. Williams


