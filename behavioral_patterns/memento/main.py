from memento import TextEditor, History

if __name__ == "__main__":
    # Create the TextEditor (Originator) and a History (Caretaker)
    editor = TextEditor()
    history = History()

    # Write something and save the state
    editor.write("Hello, ")
    history.push(editor.save())  # Save after writing "Hello, "
    editor.show_content()        # Output: "Hello, "

    # Write more text and save state again
    editor.write("World!")
    history.push(editor.save())  # Save after writing "World!"
    editor.show_content()        # Output: "Hello, World!"

    # Undo: restore to the previous state
    previous_memento = history.pop()
    if previous_memento:
        editor.restore(previous_memento)
    editor.show_content()  # Output: "Hello, "

    # Undo again: restore to the even earlier state
    previous_memento = history.pop()
    if previous_memento:
        editor.restore(previous_memento)
    editor.show_content()  # Output: ""
