from multiprocessing import Process
from network.service import AsyncMessageSocket
from zmq import PULL


class ResultHandler(Process):
    PORT = 5558

    def __init__(self) -> None:
        Process.__init__(self, daemon=True)

    def run(self) -> None:
        input_socket = AsyncMessageSocket(PULL, self.PORT)
        input_socket.bind()

        while True:
            result = input_socket.recv_result()
            print(result)
