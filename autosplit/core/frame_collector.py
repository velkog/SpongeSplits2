from multiprocessing import Process
from network.service import AsyncMessageSocket
from zmq import PUSH


class FrameCollector(Process):
    PORT = 5557

    def __init__(self) -> None:
        Process.__init__(self, daemon=True)
        self.output_socket = AsyncMessageSocket(PUSH, self.PORT)

    def run(self) -> None:
        self.output_socket.bind()

        for i in range(1000):
            self.output_socket.send_frame(i)

            from time import sleep

            sleep(2)
