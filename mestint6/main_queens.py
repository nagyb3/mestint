from problems.queens.state import NQueens
from problems.queens.operator import Operator
from search.uninformed import BackTrack, BackTrackWithCircleMonitoring, DepthFirstSearch, BreadthSearchAlgorithm

if __name__ == "__main__":
    alg = BreadthSearchAlgorithm(delay_seconds=1)

    start_state = NQueens(n=4)

    operators = []

    for row in range(start_state.n):
        for col in range(start_state.n):
            operators.append(Operator(row, col))

    result = alg.search(start_state=start_state, operators=operators)

