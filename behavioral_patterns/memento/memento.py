class EditorMemento:
    def __init__(self, text_state):
        self._text_state = text_state
    
    def get_state(self):
        return self._text_state

class TextEditor:
    def __init__(self):
        self.content = ""
    
    def write(self, new_text: str):
        self.content += new_text
    
    def show_content(self):
        print(f"Content: {self.content}")

    def save(self):
        return EditorMemento(self.content)    
    
    def restore(self, memento: EditorMemento):
        self.content = memento.get_state()

class History:
    def __init__(self):
        self._mementos = []

    def push(self, memento):
        self._mementos.append(memento)

    def pop(self):
        if not self._mementos:
            return None
        return self._mementos.pop()
