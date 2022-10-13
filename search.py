# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    #print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    
    casillas_examinadas = {} #se hace dict para que el coste al hacer búsquedas sea O(1) [cord, true/false]  (HAY QUE HACER ASÍ EL DICCIONARIO !!??) --> SE PODRÍA HACER CON UN SET
    # POR QUÉ EXPANDE EL NODO 'A' 2x veces en autograder.py??!! --> ES POR EL PRINT DEL SUCCESORS DEL PRINCIPIO 
    fringe = util.Stack()
    fringe.push((problem.getStartState(), []))
    while True:
        
        if fringe.isEmpty():
            print("ERROR!!")
            return []
        
        nodo_actual = fringe.pop() #nodo_actual = ((x,y), [s, w, ...])
        
        if problem.isGoalState(nodo_actual[0]):
            # print("SE HA ALCANZADO EL OBJETIVO")
            # print("Lista recorrido: "  + str(nodo_actual[1]))
            return nodo_actual[1]

        if nodo_actual[0] not in casillas_examinadas:
            casillas_examinadas[nodo_actual[0]] = True
            # tupla_sucesor = ((5, 4), 'South', 1)
            for tupla_sucesor in problem.getSuccessors(nodo_actual[0]):
                camino = nodo_actual[1].copy()
                camino.append(tupla_sucesor[1])
                fringe.push((tupla_sucesor[0], camino))

    #util.raiseNotDefined()

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))


    casillas_examinadas = {} #se hace dict para que el coste al hacer búsquedas sea O(1) [cord, true/false]
    fringe = util.Queue()
    fringe.push((problem.getStartState(), []))
    while True:

        if fringe.isEmpty():
            print("ERROR!!")
            return []

        nodo_actual = fringe.pop() #nodo_actual = ((x,y), [s, w, ...])
        if problem.isGoalState(nodo_actual[0]):
            #print("SE HA ALCANZADO EL OBJETIVO")
            return nodo_actual[1]

        if nodo_actual[0] not in casillas_examinadas:
            print(nodo_actual[0])
            casillas_examinadas[nodo_actual[0]] = True
            # tupla_sucesor = ((5, 4), 'South', 1)
            for tupla_sucesor in problem.getSuccessors(nodo_actual[0]):
                camino = nodo_actual[1].copy()
                camino.append(tupla_sucesor[1])
                fringe.push((tupla_sucesor[0], camino))

    #util.raiseNotDefined()

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    casillas_examinadas = {} #se hace dict para que el coste al hacer búsquedas sea O(1) [cord, true/false]
    fringe = util.PriorityQueue()
    fringe.push((problem.getStartState(), [], 0), 0)
    while True:

        if fringe.isEmpty():
            print("ERROR!!")
            return []

        nodo_actual = fringe.pop() #nodo_actual = ((x,y), [s, w, ...]))
        
        if problem.isGoalState(nodo_actual[0]):
            #print("SE HA ALCANZADO EL OBJETIVO")
            return nodo_actual[1]

        if nodo_actual[0] not in casillas_examinadas:
            casillas_examinadas[nodo_actual[0]] = True
            # tupla_sucesor = ((5, 4), 'South', 1)             
            for tupla_sucesor in problem.getSuccessors(nodo_actual[0]):
                camino = nodo_actual[1].copy()
                camino.append(tupla_sucesor[1])
                coste = nodo_actual[2] + tupla_sucesor[2]
                fringe.push((tupla_sucesor[0], camino, coste), coste)

                # Actualizar orden nodos vecinos por prioridad
                fringe.update((tupla_sucesor[0], camino, coste), coste)
    #util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    casillas_examinadas = {} #se hace dict para que el coste al hacer búsquedas sea O(1) [cord, true/false]
    fringe = util.PriorityQueue()
    valor_heuristico = heuristic(problem.getStartState(), problem)
    # utilizo el valor del heurístico para ordenar los nodos, pero no lo acumulo para no pasar valor
    # del heurístico del nodo anterior a sus sucesores (SE PUEDE PONER UN EJEMPLO)
    fringe.push((problem.getStartState(), [], 0), 0 + valor_heuristico)
    while True:

        if fringe.isEmpty():
            print("ERROR!!")
            return []

        nodo_actual = fringe.pop() #nodo_actual = ((x,y), [s, w, ...]))

        if problem.isGoalState(nodo_actual[0]):
            #print("SE HA ALCANZADO EL OBJETIVO")
            return nodo_actual[1]

        if nodo_actual[0] not in casillas_examinadas:
            casillas_examinadas[nodo_actual[0]] = True
            # tupla_sucesor = ((5, 4), 'South', 1)             
            for tupla_sucesor in problem.getSuccessors(nodo_actual[0]):
                camino = nodo_actual[1].copy()
                camino.append(tupla_sucesor[1])
                valor_heuristico = heuristic(tupla_sucesor[0], problem)
                coste = nodo_actual[2] + tupla_sucesor[2]
                # utilizo el valor del heurístico para ordenar los nodos, pero no lo acumulo para no 
                # pasar valor del heurístico del nodo anterior a sus sucesores (SE PUEDE PONER UN
                # EJEMPLO)
                fringe.push((tupla_sucesor[0], camino, coste), coste + valor_heuristico)

                # Actualizar orden nodos vecinos por prioridad
                fringe.update((tupla_sucesor[0], camino, coste), coste + valor_heuristico)

    #util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
