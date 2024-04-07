from problems.jug.state import Jug
from problems.jug.operator import Operator
from search.uninformed import BackTrack, BackTrackWithCircleMonitoring, DepthFirstSearch, BreadthSearchAlgorithm

if __name__ == "__main__":
    alg = BreadthSearchAlgorithm(delay_seconds=1)

    start_state = Jug([0, 0, 5])

    operators = [
        Operator(from_=0, to=1),
        Operator(from_=0, to=2),
        Operator(from_=1, to=2),
        Operator(from_=1, to=0),
        Operator(from_=2, to=1),
        Operator(from_=2, to=0)
    ]

    result = alg.search(start_state=start_state, operators=operators)

