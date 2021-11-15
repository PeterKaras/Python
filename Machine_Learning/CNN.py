import tensorflow as tf

def generate_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32, filter_size = 3, activation='relu'),
        tf.keras.layers.MaxPool2D(pool_size = 2, strides=2),
        
        #64 feature maps
        tf.keras.layers.Conv2D(64, filter_size = 3, activation='relu'),
        tf.keras.layers.MaxPool2D(pool_size = 2, strides=2),
        
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(1024, activation= "relu"),
        tf.keras.layers.Dense(NumberOfOutputs, activation ="softmax")
    ])
    return model


tf.keras.layers.MaxPool2D(
    pool_size = (3,3),
    strides = 2 #shifting the filter of pixels
    )

#Semantic Segmentation - upsampling
tf.keras.layers.Conv2DTranspose()