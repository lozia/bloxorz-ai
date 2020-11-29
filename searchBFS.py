from display import Displayable, visualize
import io
from bloxorz import Board
from searchProblem import Arc, Search_problem, Path
from bloxorz_problem import BloxorzProblem

class BFSSearcher(Displayable):
    """returns a searcher for a problem.
    Paths can be found by repeatedly calling search().
    This does depth-first search unless overridden
    """

    def __init__(self, problem):
        """creates a searcher from a problem
        """
        self.problem = problem
        self.initialize_frontier()
        self.frontier_maxsize = 0
        self.num_expanded = 0
        self.add_to_frontier(Path(problem.start_node()))
        super().__init__()

    def initialize_frontier(self):
        self.frontier = []

    def empty_frontier(self):
        return self.frontier == []

    def add_to_frontier(self, path):
        self.frontier.append(path)
        self.frontier_maxsize += 1

    @visualize
    def search(self):
        """returns (next) path from the problem's start node
        to a goal node.
        Returns None if no path exists.
        """
        while not self.empty_frontier():
            path = self.frontier.pop(0)
            self.num_expanded += 1
            self.display(2, "Expanding:", path, "(cost:", path.cost, ")")
            if self.problem.is_goal(path.end()):  # solution found
                self.solution = path  # store the solution found
                self.display(1, self.num_expanded, "paths have been expanded and",
                             len(self.frontier), "paths remain in the frontier")
                return path
            else:
                neighs = self.problem.neighbors(path.end())
                self.display(3, "Neighbors are", neighs)
                for arc in reversed(neighs):
                    self.add_to_frontier(Path(path, arc))
                self.display(3, "Frontier:", self.frontier)
        self.display(1, "No (more) solutions. Total of",
                     self.num_expanded, "paths expanded.")
        return


class BFSMultiPruneSearcher(BFSSearcher):
    def __init__(self, problem):
        self.closed = {}
        self.solution = None
        super().__init__(problem)

    def initialize_frontier(self):
        self.frontier = []

    def empty_frontier(self):
        return self.frontier == []

    def add_to_frontier(self, path):
        node = path.end()
        if node not in self.closed:
            self.closed[node] = True
            self.frontier_maxsize += 1
            self.frontier.append(path)

    def search(self):
        """returns (next) path from the problem's start node
                to a goal node.
                Returns None if no path exists.
                """
        while not self.empty_frontier():
            path = self.frontier.pop(0)
            self.num_expanded += 1
            self.display(2, "Expanding:", path, "(cost:", path.cost, ")")
            if self.problem.is_goal(path.end()):  # solution found
                self.solution = path  # store the solution found
                self.display(1, self.num_expanded, "paths have been expanded and",
                             len(self.frontier), "paths remain in the frontier")
                return path
            else:
                neighs = self.problem.neighbors(path.end())
                self.display(3, "Neighbors are", neighs)
                for arc in reversed(neighs):
                    self.add_to_frontier(Path(path, arc))
                self.display(3, "Frontier:", self.frontier)
        self.display(1, "No (more) solutions. Total of",
                     self.num_expanded, "paths expanded.")
        return


import searchProblem as searchProblem


def test(SearchClass, Problem):
    print("Testing problem bp0:")
    schr1 = SearchClass(Problem)
    path1 = schr1.search()
    print("Path found:", path1)
    # assert list(path1.nodes()) == ['g', 'd', 'c', 'b', 'a'], "Shortest path not found in problem1"
    # print("Passed unit test")


if __name__ == "__main__":
    # test(BFSMultiPruneSearcher, searchProblem.problem1)
    board_string = (
        '''BLOX 1
5 3
X X X O O
S X G X O
W W W W X
''')
    fake_file = io.StringIO(board_string)
    board0 = Board.read_board(fake_file)
    bp0 = BloxorzProblem(board0)
    test(BFSMultiPruneSearcher, bp0)
