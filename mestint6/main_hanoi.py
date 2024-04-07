from problems.hanoi.state import Hanoi
from problems.hanoi.operator import Operator
from search.uninformed import BackTrack, BackTrackWithCircleMonitoring, DepthFirstSearch, BreadthSearchAlgorithm

if __name__ == "__main__":
    alg = BreadthSearchAlgorithm(delay_seconds=1)

    start_state = Hanoi()

    operators = [
        Operator(from_="A", to="B"),
        Operator(from_="A", to="C"),
        Operator(from_="B", to="A"),
        Operator(from_="B", to="C"),
        Operator(from_="C", to="B"),
        Operator(from_="C", to="A")
    ]

    result = alg.search(start_state=start_state, operators=operators)

