from typing import Callable

class Callback:
    """A class that allows for the registration and triggering of callbacks."""

    def __init__(self):
        """
        Initializes an empty list to store callbacks.
        """
        self.callbacks: list[Callable] = []

    def __call__(self):
        """
        Iterates through and calls all registered callbacks.
        """
        for c in self.callbacks:
            c()

    def register(self, callback: Callable):
        """
        Register a new callback to be called when the callback object is called.
        :param callback: A callable object to be registered.
        """
        self.callbacks.append(callback)

    def unregister(self, callback: Callable):
        """
        Unregister a callback so it will no longer be called when the callback object is called.
        :param callback: The callback to be unregistered.
        """
        if callback in self.callbacks:
            self.callbacks.remove(callback)