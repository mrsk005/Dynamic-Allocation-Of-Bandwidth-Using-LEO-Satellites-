from drl.network import DRLNetwork
import numpy as np

def train_model(data, targets):
    # Initialize the DRL network
    network = DRLNetwork()
    
    # Train the network
    network.model.fit(data, targets, epochs=10, batch_size=32, validation_split=0.2)
    
    # Save the trained model
    network.model.save('drl_model.h5')

def load_model():
    # Load a pre-trained model
    return tf.keras.models.load_model('drl_model.h5')