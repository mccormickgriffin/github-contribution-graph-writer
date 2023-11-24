class Letter:
    def __init__(self, graph) -> None:
        if (graph.length != 7):
            raise ValueError("Invalid letter height")
        self.graph = graph

    def width(self):
        return len(self.graph[0])
