from abc import ABC, abstractmethod
from typing import Optional

from keras.engine.training import Model  # type: ignore
from learner.models import SubsetTypes
from learner.models.generic_model import GenericModel
from tensorflow.keras.utils import image_dataset_from_directory  # type: ignore
from tensorflow.python.data.ops.dataset_ops import BatchDataset  # type: ignore


class GenericImageModel(GenericModel, ABC):
    def __init__(
        self,
    ) -> None:
        GenericModel.__init__(self)
        self._train_ds: Optional[BatchDataset] = None
        self._val_ds: Optional[BatchDataset] = None

    @property
    @abstractmethod
    def IMG_HEIGHT(self) -> int:
        raise NotImplementedError

    @property
    @abstractmethod
    def IMG_WIDTH(self) -> int:
        raise NotImplementedError

    @property
    @abstractmethod
    def VALIDATION_SPLIT(self) -> float:
        raise NotImplementedError

    def _get_dataset(self, subset_type: SubsetTypes) -> BatchDataset:
        return image_dataset_from_directory(
            self.DATASET_PATH,
            validation_split=self.VALIDATION_SPLIT,
            subset=subset_type.value,
            seed=self.SEED,
            image_size=(self.IMG_HEIGHT, self.IMG_WIDTH),
            batch_size=self.BATCH_SIZE,
        )

    @property
    def TRAIN_DS(self) -> BatchDataset:
        if not self._train_ds:
            self._train_ds = self._get_dataset(SubsetTypes.TRAINING)
        return self._train_ds

    @property
    def VAL_DS(self) -> BatchDataset:
        if not self._val_ds:
            self._val_ds = self._get_dataset(SubsetTypes.VALIDATION)
        return self._val_ds
