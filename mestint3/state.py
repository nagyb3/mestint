# hanui towers
class Hanoi:

    TOWERS = ["A", "B", "C"]

    def __init__(self, disks=None):
        if disks:
            self.towers = {"A": disks, "B": set(), "C": set()}
        else:
            self.towers = {"A": {1, 2, 3}, "B": set(), "C": set()}

    # cél állapot-e
    def is_goal_state(self):
        return self.towers["C"] == {1, 2, 3}

    def __str__(self):
        return f"Tower of Hanoi[Towers={str(self.towers)}]"


def main():
    hanoi = Hanoi()
    print(hanoi)


if __name__ == "__main__":
    main()
