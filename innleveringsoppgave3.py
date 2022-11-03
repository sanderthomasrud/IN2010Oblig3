from IMDBGraph import IMBDGraph
import time
start_time = time.time()

"""
Oppgave 1: Lager grafen
"""
print(f"\nOppgave 1\n")
graph = IMBDGraph("movies.tsv", "actors.tsv")


"""
Oppgave 2: Skriver ut raskeste vei mellom to noder, tar ikke hensyn til vekt
"""

print(f"------------------------\n\nOppgave 2\n")
graph.getShortestPath("nm2255973", "nm0000460") # Donald Glover -> Jeremy Irons
graph.getShortestPath("nm0424060", "nm0000243") # Scarlett Johansson -> Denzel Washington
graph.getShortestPath("nm4689420", "nm0000365") # Carrie Coon -> Julie Delphy
graph.getShortestPath("nm0000288", "nm0001401") # Christian Bale -> Angelina Jolie
graph.getShortestPath("nm0031483", "nm0931324") # Atle Antonsen -> Michael K. Williams

"""
Oppgave 3: Skriver ut raskeste vei mellom to noder, tar hensyn til vekt
"""

print(f"------------------------\n\nOppgave 3\n")
graph.getChillestPath("nm2255973", "nm0000460") # Donald Glover -> Jeremy Irons
graph.getChillestPath("nm0424060", "nm0000243") # Scarlett Johansson -> Denzel Washington
graph.getChillestPath("nm4689420", "nm0000365") # Carrie Coon -> Julie Delphy
graph.getChillestPath("nm0000288", "nm0001401") # Christian Bale -> Angelina Jolie
graph.getChillestPath("nm0031483", "nm0931324") # Atle Antonsen -> Michael K. Williams

"""
Oppgave 4: Skriver ut antall forekomster av størrelsen på komponenter
"""

print(f"------------------------\n\nOppgave 4\n")
graph.countNodesInComponents()

print (f"\n------------------------\n\nProgrammet bruker {int(time.time() - start_time)} sekunder på å kjøre.")
