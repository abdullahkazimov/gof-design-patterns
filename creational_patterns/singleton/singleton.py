from threading import Lock

def singleton_thread_safe(cls):
    _instances = {}
    _lock = Lock()

    def get_instance(*args, **kwargs):
        with _lock:
            if cls not in _instances:
                _instances[cls] = cls(*args, **kwargs)
        
        return _instances[cls]

    return get_instance

@singleton_thread_safe
class Admin:
    def __init__(self, name):
        self.name = name