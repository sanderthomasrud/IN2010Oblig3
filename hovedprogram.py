from funksjonerNy import IMBDGraph

graph = IMBDGraph()

# Oppgave 1

graph.makeGraph("inputs/movies.tsv", "inputs/actors.tsv")

# Oppgave 2

# graph.test("nm0000313", "nm0001745") # Jeff Bridges -> Stellan Skarsgård # tester i den lille grafen

graph.test("nm2255973", "nm0000460") # Donald Glover -> Jeremy Irons
graph.test("nm0424060", "nm0000243") # Scarlett Johansson -> Denzel Washington
graph.test("nm4689420", "nm0000365") # Carrie Coon -> Julie Delphy
graph.test("nm0000288", "nm0001401") # Christian Bale -> Angelina Jolie
graph.test("nm0031483", "nm0931324") # Atle Antonsen -> Michael K. Williams

