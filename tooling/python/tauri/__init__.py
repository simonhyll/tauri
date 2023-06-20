import asyncio
from ctypes import cdll
from typing import Callable, List, TypeVar

T = TypeVar('T', bound='Tauri')


class Tauri:
    _invoke_handler = None
    _app = None

    def __init__(self, path: str) -> None:
        self._app = cdll.LoadLibrary(path)
        self._app.init()

    def any_thread(self: T) -> T:
        print("Running any_thread")
        return self

    def invoke_handler(self: T, handler: List[Callable]) -> T:
        print("Running invoke_handler")
        self.invoke_handler = handler
        return self

    async def run(self: T, context: str) -> T:
        print("Running run")
        await self._app.run(context)
        return self

    async def __message_loop() -> None:
        await asyncio.sleep(0.001)
