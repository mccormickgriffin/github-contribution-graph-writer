from graph_characters import graph_characters

class GraphWord:
    def __init__(self, word) -> None:
        if len(word) == 0:
            raise ValueError("Cannot create a GraphWord of zero length")

        unsupported_characters = set(word) - set(graph_characters.keys())
        if unsupported_characters:
            raise NotImplementedError(f"Character(s) [{', '.join(unsupported_characters)}] not implemented yet")
        
        self.word = word
