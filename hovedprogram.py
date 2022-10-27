from funksjonerNy import IMBDGraph

graph = IMBDGraph()

graph.makeGraph("inputs/marvel_movies.tsv", "inputs/marvel_actors.tsv")

graph.test("nm0000313", "nm0001745")
# graph.BFSFull()
