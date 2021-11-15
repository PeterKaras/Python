import tensorflow as tf
import keras
import keras_preprocessing

class MyRNNCell(tf.keras.layers.Layer):
    def __init__(self, rnn_units, inputs_dim, output_dim):
        super(MyRNNCell, self).__init__()
        
        self.W_xh = self.add_weight([rnn_units, inputs_dim])
        self.W_hh = self.add_weight([rnn_units, rnn_units])
        self.W_hy = self.add_weight([rnn_units, output_dim])
        
        #Hidden state
        self.h = np.zeros([rnn_units, 1])        

    def forward_learning(self, inputs):
        
        self.h = (self.W_hh * self.h + selg.W_xh * inputs)

        output = self.W_hy * self.h
        
        return output, self.h
    
#Simple way
tf.keras.layers.SimpleRNN(rnn_units)