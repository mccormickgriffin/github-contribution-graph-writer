class GraphCharacter:
    def __init__(self, graph) -> None:
        if (len(graph) != 7):
            raise ValueError("Invalid graph character height")
        self.graph = graph

    def width(self):
        return len(self.graph[0])
