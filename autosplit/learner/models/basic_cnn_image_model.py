from typing import Optional
from abc import ABC

from keras.callbacks import History  # type: ignore
from keras.engine.training import Model  # type: ignore
from learner.models.generic_image_model import GenericImageModel
from tensorflow.keras import Sequential  # type: ignore
from tensorflow.keras.layers import (  # type: ignore
    Activation,
    Conv2D,
    Dense,
    Flatten,
    MaxPooling2D,
    Rescaling,
)
from tensorflow.keras.optimizers import Adam  # type: ignore
from tensorflow.keras.losses import SparseCategoricalCrossentropy  # type: ignore
from tensorflow import Variable  # type: ignore


class BasicCnnImageModel(GenericImageModel, ABC):
    def __init__(
        self,
    ) -> None:
        GenericImageModel.__init__(
            self,
        )

    def _get_model(self) -> Model:
        return Sequential(
            [
                Rescaling(1.0 / 255, input_shape=(self.IMG_HEIGHT, self.IMG_WIDTH, 3)),
                Conv2D(32, 3, padding="same", activation="relu"),
                MaxPooling2D(),
                Conv2D(64, 3, padding="same", activation="relu"),
                MaxPooling2D(),
                Conv2D(128, 3, padding="same", activation="relu"),
                MaxPooling2D(),
                Flatten(),
                Dense(256, activation="relu"),
                Dense(self.num_classes),
                # Activation("softmax"),
            ]
        )

    def _compile(self) -> None:
        optimizer = Adam(learning_rate=Variable(self.LEARNING_RATE), beta_1=Variable(0.9), beta_2=Variable(0.999), epsilon=Variable(1e-07))
        optimizer.iterations
        optimizer.decay = Variable(self.LEARNING_RATE / self.EPOCHS)
        self.model.compile(
            optimizer=optimizer,
            loss=SparseCategoricalCrossentropy(from_logits=True),
            metrics=["accuracy"],
        )

    def _fit(self) -> None:
        self.model.fit(
            self.TRAIN_DS,
            validation_data=self.VAL_DS,
            epochs=self.EPOCHS,
            callbacks=self._callbacks(),
        )
