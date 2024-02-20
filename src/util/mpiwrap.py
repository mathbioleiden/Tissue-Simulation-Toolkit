import os
from typing import List, Optional, TypeVar


T = TypeVar('T')


class CommWorld:
    """Wrapper for MPI_COMM_WORLD

    This provides the tiny subset of the MPI.Comm API from mpi4py that we
    actually use, either backed by the real mpi4py implementation if we're
    running under MPI, or a dummy version if we're not. In the latter case,
    mpi4py does not have to be installed.
    """
    def __init__(self) -> None:
        """Create a CommWorld."""
        try:
            from mpi4py import MPI
            self._mpi = True
            self._comm = MPI.COMM_WORLD
        except ImportError:
            self._mpi = False

    def Get_rank(self) -> int:
        """Return the rank of the current MPI process."""
        if self._mpi:
            return self._comm.Get_rank()
        return 0

    def bcast(self, data: Optional[T]) -> T:
        """Broadcast the data to all processes.

        This expects to be passed an object of type T on process 0, and
        None on all other processes. It will then return the object on
        all processes.

        Args:
            data: The data to broadcast (on the root only)

        Return:
            The passed data object
        """
        if self._mpi:
            return self._comm.bcast(data)
        assert data is not None
        return data

    def gather(self, data: T) -> Optional[List[T]]:
        """Gather the data to the process with rank 0.

        This expects to be passed an object of type T on each process,
        and returns a list of all the passed objects on the process with
        rank 0, and None on the others.

        Args:
            data: The data to be gathered (on every process)

        Return:
            A list of collected objects (on the root only)
        """
        if self._mpi:
            return self._comm.gather(data)
        return [data]

    def allgather(self, data: T) -> List[T]:
        """Gather the data to all processes.

        This expects to be passed an object of type T on each process,
        and returns a list of all the passed objects on all processes.

        Args:
            data: The data to be gathered (on every process)

        Return:
            A list of collected objects (on every process)
        """
        if self._mpi:
            return self._comm.allgather(data)
        return [data]
