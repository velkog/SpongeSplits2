from multiprocessing import Process
from network.protobuf.message import PineappleFrameMessage, PineappleResultMessage
from network.service import AsyncMessageSocket
from zmq import PULL, PUSH


class FrameProcessor(Process):
    INPUT_PORT = 5557
    OUTPUT_PORT = 5558

    def __init__(self) -> None:
        Process.__init__(self, daemon=True)
        self.input_socket = AsyncMessageSocket(
            PineappleFrameMessage, self.INPUT_PORT, PULL
        )
        self.output_socket = AsyncMessageSocket(
            PineappleResultMessage, self.OUTPUT_PORT, PUSH
        )

    def run(self) -> None:
        import random

        consumer_id = random.randint(0, 10000)

        self.input_socket.connect()
        self.output_socket.connect()

        while True:
            pineapple_frame_msg = self.input_socket.recv_message()
            assert isinstance(pineapple_frame_msg, PineappleFrameMessage)

            frame_id = pineapple_frame_msg.frame_id
            result = f"Worker {consumer_id} processed data: {frame_id}"
            pineapple_result_msg = PineappleResultMessage.from_data(result)
            self.output_socket.send_message(pineapple_result_msg)

            from time import sleep

            sleep(3)
