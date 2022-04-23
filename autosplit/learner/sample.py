from tensorflow.data import AUTOTUNE
from tensorflow.keras import Sequential
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.layers import (
    Activation,
    Conv2D,
    Dense,
    Flatten,
    MaxPooling2D,
    Rescaling,
)
from tensorflow.keras.losses import SparseCategoricalCrossentropy
from tensorflow.keras.utils import image_dataset_from_directory

# https://www.te1nsorflow.org/tutorials/images/classification

# TODO: Do this programmicatily/move to config
BATCH_SIZE = 32
IMG_HEIGHT = 80
IMG_WIDTH = 107
DATA_DIR = "autosplit/learner/dataset/data/spatula"


# Create a dataset
train_ds = image_dataset_from_directory(
    DATA_DIR,
    validation_split=0.2,
    subset="training",
    seed=123,
    image_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=BATCH_SIZE,
)
val_ds = image_dataset_from_directory(
    DATA_DIR,
    validation_split=0.2,
    subset="validation",
    seed=123,
    image_size=(IMG_HEIGHT, IMG_WIDTH),
    batch_size=BATCH_SIZE,
)

# Configure the dataset for performance
train_ds = train_ds.cache().shuffle(1000).prefetch(buffer_size=AUTOTUNE)
val_ds = val_ds.cache().prefetch(buffer_size=AUTOTUNE)

# Standardize the data
normalization_layer = Rescaling(1.0 / 255)
normalized_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
image_batch, labels_batch = next(iter(normalized_ds))
first_image = image_batch[0]

# Create the model
num_classes = 12
model = Sequential(
    [
        Rescaling(1.0 / 255, input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)),
        Conv2D(32, 3, padding="same", activation="relu"),
        MaxPooling2D(),
        Conv2D(64, 3, padding="same", activation="relu"),
        MaxPooling2D(),
        Conv2D(128, 3, padding="same", activation="relu"),
        MaxPooling2D(),
        Flatten(),
        Dense(256, activation="relu"),
        Dense(num_classes),
        Activation("softmax"),
    ]
)

# Compile the model
model.compile(
    optimizer="adam",
    loss=SparseCategoricalCrossentropy(from_logits=True),
    metrics=["accuracy"],
)

# Train the model
EPOCHS = 1
checkpoint_path = "autosplit/learner/models/checkpoints/spatula"
cp_callback = ModelCheckpoint(
    filepath=checkpoint_path,
    save_weights_only=True,
    verbose=1,
)
# model.fit(train_ds, validation_data=val_ds, epochs=EPOCHS, callbacks=[cp_callback])

h = model.load_weights(checkpoint_path)
h.assert_existing_objects_matched()
