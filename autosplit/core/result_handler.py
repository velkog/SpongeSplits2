from multiprocessing import Process
from network.protobuf.message import PineappleResultMessage
from network.service import AsyncMessageSocket
from zmq import PULL


class ResultHandler(Process):
    PORT = 5558

    def __init__(self) -> None:
        Process.__init__(self, daemon=True)

    def run(self) -> None:
        input_socket = AsyncMessageSocket(PineappleResultMessage, self.PORT, PULL)
        input_socket.bind()

        while True:
            pineapple_result_msg = input_socket.recv_message()
            assert isinstance(pineapple_result_msg, PineappleResultMessage)
            prediction = pineapple_result_msg.prediction
            print(prediction)
