from multiprocessing import Process
from network.service import AsyncMessageSocket
from network.protobuf.message import PineappleFrameMessage
from zmq import PUSH


class FrameCollector(Process):
    PORT = 5557

    def __init__(self) -> None:
        Process.__init__(self, daemon=True)
        self.output_socket = AsyncMessageSocket(PineappleFrameMessage, self.PORT, PUSH)

    def run(self) -> None:
        self.output_socket.bind()

        for i in range(1000):
            pineapple_frame_msg = PineappleFrameMessage.from_data(i)
            self.output_socket.send_message(pineapple_frame_msg)

            from time import sleep

            sleep(2)
