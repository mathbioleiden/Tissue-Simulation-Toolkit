import os
from typing import Any, cast, Dict, List, Literal, Optional, overload, Union

from libmuscle import Instance as M3Instance, Message
from ymmsl import Operator, SettingValue

from tissue_simulation_toolkit.util.mpiwrap import CommWorld


class Instance:
    """A helper class that mimics libmuscle.Instance

    MUSCLE3 doesn't support MPI in its Python API, because I figured if
    you do MPI then you need performance, and if you need performance you're
    not programming in Python. That's been true so far, but then I
    encountered hoomd, which is indeed written in C++ but only accessible
    from Python. So we'll add MPI support to the MUSCLE3 Python API in some
    future version, but in the mean time, this class provides a simple
    wrapper that makes it work anyway. -LV
    """
    def __init__(self, port_definition: Dict[Operator, List[str]]) -> None:
        """Create an Instance"""
        self._comm = CommWorld()

        self.instance: Optional[M3Instance] = None
        if self._is_root():
            self.instance = M3Instance(port_definition)

    def reuse_instance(self) -> bool:
        """Return whether to run the simulation again

        See libmuscle.Instance.reuse_instance().
        """
        result = False
        if self._is_root():
            result = self._instance().reuse_instance()
        result = self._comm.bcast(result)
        return result

    @overload
    def get_setting(self, name: str, typ: Literal['str']) -> str:
        ...

    @overload
    def get_setting(self, name: str, typ: Literal['int']) -> int:
        ...

    @overload
    def get_setting(self, name: str, typ: Literal['float']) -> float:
        ...

    @overload
    def get_setting(self, name: str, typ: Literal['bool']) -> bool:
        ...

    @overload
    def get_setting(self, name: str, typ: Literal['[float]']) -> List[float]:
        ...

    @overload
    def get_setting(
            self, name: str, typ: Literal['[[float]]']) -> List[List[float]]:
        ...

    @overload
    def get_setting(self, name: str, typ: None = None) -> SettingValue:
        ...

    def get_setting(self, name: str, typ: Optional[str] = None) -> SettingValue:
        """Returns the value of a model setting.

        See libmuscle.Instance.get_setting().
        """
        value = None    # type: Any
        if self._is_root():
            value = self._instance().get_setting(name, typ)     # type: ignore

        value = self._comm.bcast(value)
        return value

    def is_connected(self, port: str) -> bool:
        """Returns whether the given port is connected.

        See libmuscle.Instance.is_connected().
        """
        value = None    # type: Any
        if self._is_root():
            value = self._instance().is_connected(port)

        value = self._comm.bcast(value)
        return value

    def send(
            self, port_name: str, message: Message, slot: Optional[int] = None
            ) -> None:
        """Send a message to the outside world.

        See libmuscle.Instance.send()
        """
        if self._is_root():
            self._instance().send(port_name, message, slot)

    def receive(
            self, port_name: str, slot: Optional[int] = None,
            default: Optional[Message] = None) -> Message:
        """Receive a message from the outside world.

        See libmuscle.Instance.receive()
        """
        msg = None      # type: Any
        if self._is_root():
            msg = self._instance().receive(port_name, slot, default)

        msg = self._comm.bcast(msg)
        return msg

    def _is_root(self) -> bool:
        """Return whether the current process in the root process"""
        # 0 is the default for e.g. bcast(), saving some code
        return self._comm.Get_rank() == 0

    def _instance(self) -> M3Instance:
        """Get the instance or raise if not root

        This helps the type checker understand that self.instance is not
        None on the root process, and it guards against errors.
        """
        if not self._is_root():
            raise RuntimeError('Tried to get instance on non-root process')
        return cast(M3Instance, self.instance)
