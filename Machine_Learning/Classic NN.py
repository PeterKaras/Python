import tensorflow as tf
import keras
import keras_preprocessing

class MyDenseLayer(tf.keras.layers.Layer):
    def __init__(self, input_dim, output_dim):
        super(MyDenseLayer,self).__init__()
        
        self.W = self.add_weight([input_dim, output_dim])
        self.b = self.add_weight([1, output_dim])

    def Forward_prop(self, inputs):
        z = inputs.dot(self.W) + self.b 
        
        output = tf.math.sigmoid(z)
        
        return output
    
model = tf.keras.Sequential([
    tf.keras.layers.Dense(inputs_dim),
    tf.keras.layers.Dense(number_of_hidden_neurons), # this row can be applied multiple times
    tf.keras.layers.Dense(output_dim)
    ])

#softmax binary cross entropy loss
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(y, predicted))

#mean squared error loss
loss = tf.reduce_mean(tf.squared(tf.subtract(y, predicted)))
loss = tf.keras.losses.MSE(y, predicted)


#Gradient Descent
weights = tf.Variable([tf.random.normal()])
optimizer = tf.keras.optimizers.SGD()

while True:
    
    prediction = model(x)
    
    with tf.GradientTape() as g:
        loss = compute_loss(weights)
        
    gradient = g.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(grads,model.trainable_variables))
    
    #weights -= lr*gradient 


    
    
        