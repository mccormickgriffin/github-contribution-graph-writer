ROW_COUNT = 7

class GraphCharacter:
    def __init__(self, graph) -> None:
        if (len(graph) != ROW_COUNT):
            raise ValueError("Invalid graph character height")
        self.graph = graph

    def width(self):
        return len(self.graph[0])
    
    def __iadd__(self, other):
        if not isinstance(other, GraphCharacter):
            raise ValueError(f"Cannot add GraphCharacter with object of type: {type(other)}")
        
        for i in range(ROW_COUNT):
            # Add a blank space for between characters
            self.graph[i] += [0]
            # Concatinate the other letter
            self.graph[i] += other.graph[i]
        
        return self
