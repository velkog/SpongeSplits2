from learner.models.basic_cnn_image_model import BasicCnnImageModel
from typing import Optional

class SpatulaModel(BasicCnnImageModel):
    @property
    def DATASET_PATH(self) -> str:
        return "autosplit/learner/dataset/data/spatula"

    @property
    def CHECKPOINT_PATH(self) -> Optional[str]:
        return "autosplit/learner/models/checkpoints/spatula"

    @property
    def BATCH_SIZE(self) -> int:
        return 32

    @property
    def EPOCHS(self) -> int:
        return 16

    @property
    def LEARNING_RATE(self) -> float:
        return 0.0001

    @property
    def SEED(self) -> int:
        return 123

    @property
    def IMG_HEIGHT(self) -> int:
        return 80

    @property
    def IMG_WIDTH(self) -> int:
        return 107

    @property
    def VALIDATION_SPLIT(self) -> float:
        return 0.2

    @property
    def num_classes(self) -> int:
        return 84