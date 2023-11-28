from graph_characters import character_to_graph_mapping
from graph_character import GraphCharacter

class GraphWord:
    def __init__(self, word) -> None:
        if len(word) == 0:
            raise ValueError("Cannot create a GraphWord of zero length")

        unsupported_characters = set(word) - set(character_to_graph_mapping.keys())
        if unsupported_characters:
            raise NotImplementedError(f"Character(s) [{', '.join(unsupported_characters)}] not implemented yet")
        
        self.graph_string = GraphCharacter(character_to_graph_mapping[word[0]])
        for i in range(1, len(word)):
            self.graph_string += GraphCharacter(character_to_graph_mapping[word[i]])

        self.word = word
        self.width = len(self.graph_string.graph[0])

    def get(self, row, column):
        return self.graph_string.graph[row][column]
    
    def pad_front(self, spaces):
        self.graph_string.graph = [[0] * spaces + row for row in self.graph_string.graph]

    def pad_back(self, spaces):
        self.graph_string.graph = [row + [0] * spaces for row in self.graph_string.graph]
    
    def print_graph(self):
        for row in self.graph_string.graph:
            for block in row:
                if block:
                    print("X ", end="")
                else:
                    print("  ", end="")
            print("")
    