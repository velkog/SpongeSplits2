from multiprocessing import Process
from network.service import AsyncMessageSocket
from zmq import PULL, PUSH


class FrameProcessor(Process):
    INPUT_PORT = 5557
    OUTPUT_PORT = 5558

    def __init__(self) -> None:
        Process.__init__(self, daemon=True)
        self.input_socket = AsyncMessageSocket(PULL, self.INPUT_PORT)
        self.output_socket = AsyncMessageSocket(PUSH, self.OUTPUT_PORT)

    def run(self) -> None:
        import random

        consumer_id = random.randint(0, 10000)

        self.input_socket.connect()
        self.output_socket.connect()

        while True:
            data = self.input_socket.recv_frame()
            result = f"Worker {consumer_id} processed data: {data}"
            self.output_socket.send_result(result)

            from time import sleep

            sleep(3)
