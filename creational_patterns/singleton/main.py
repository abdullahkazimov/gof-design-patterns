import threading
from singleton import Admin

def modify_admin(name):
    # Retrieve the singleton instance
    admin = Admin(name)
    print(f"Before setting: {threading.current_thread().name} sees Admin name as {admin.name}")
    # Attempt to change the Admin's name (this would affect all threads if set here)
    admin.name = name
    print(f"After setting: {threading.current_thread().name} sees Admin name as {admin.name}")

if __name__ == "__main__":
    # Names for each thread to try setting on the Admin object
    names = ['Alice', 'Bob', 'Charlie']

    # Create threads
    threads = [threading.Thread(target=modify_admin, args=(name,), name=f"Thread-{name}") for name in names]

    # Start threads
    for thread in threads:
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()
