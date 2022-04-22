from abc import ABC, abstractmethod
from typing import List, Optional

from keras.callbacks import History, ModelCheckpoint  # type: ignore
from keras.engine.training import Model  # type: ignore
from learner.models import SubsetTypes
from tensorflow.python.data.ops.dataset_ops import BatchDataset  # type: ignore
from tensorflow.python.framework.errors_impl import NotFoundError  # type: ignore


class GenericModel(ABC):
    def __init__(
        self,
    ) -> None:
        self._model: Optional[Model] = None

    @property
    @abstractmethod
    def DATASET_PATH(self) -> str:
        raise NotImplementedError

    @property
    def CHECKPOINT_PATH(self) -> Optional[str]:
        return None

    @property
    @abstractmethod
    def BATCH_SIZE(self) -> int:
        raise NotImplementedError

    @property
    @abstractmethod
    def EPOCHS(self) -> int:
        raise NotImplementedError

    @property
    @abstractmethod
    def SEED(self) -> int:
        raise NotImplementedError

    @property
    @abstractmethod
    def TRAIN_DS(self) -> BatchDataset:
        raise NotImplementedError

    @property
    @abstractmethod
    def VAL_DS(self) -> BatchDataset:
        raise NotImplementedError

    @property
    @abstractmethod
    def LEARNING_RATE(self) -> float:
        raise NotImplementedError

    @property
    def num_classes(self) -> int:
        num_classes = len(self.TRAIN_DS.class_names)
        assert num_classes == len(self.VAL_DS.class_names)
        return num_classes

    @property
    def model(self) -> Model:
        if not self._model:
            self._model = self._get_model()
        return self._model

    def _get_dataset(self, subset_type: SubsetTypes) -> BatchDataset:
        raise NotImplementedError

    @abstractmethod
    def _get_model(self) -> Model:
        raise NotImplementedError

    @abstractmethod
    def _compile(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def _fit(self) -> None:
        raise NotImplementedError

    def _load(self) -> bool:
        if self.CHECKPOINT_PATH:
            self.model.load_weights(self.CHECKPOINT_PATH).assert_existing_objects_matched()
            return True
        return False

    def _train(self) -> None:
        self._compile()
        try:
            if self._load():
                return
        except (NotFoundError, AssertionError):
            pass
        self._fit()

    def _callbacks(self) -> List[ModelCheckpoint]:
        if self.CHECKPOINT_PATH:
            return [
                ModelCheckpoint(
                    filepath=self.CHECKPOINT_PATH, save_weights_only=True, verbose=1
                )
            ]
        return []
