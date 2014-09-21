from nameko.dependencies import (
    EntrypointProvider, entrypoint, DependencyFactory)
from nameko.exceptions import ContainerBeingKilled


class ShutdownProvider(EntrypointProvider):

    def __init__(self, args, kwargs):
        self.args = args
        self.kwargs = kwargs

    def stop(self):

#        import pdb; pdb.set_trace()
        try:
            self.container.spawn_worker(self, self.args, self.kwargs)
        except ContainerBeingKilled:
            pass


@entrypoint
def shutdown(*args, **kwargs):
    """ Fire the decorated entrypoint once, immediately.
    """
    return DependencyFactory(ShutdownProvider, args, kwargs)
