# config.py

class Config(object):
    embed_size = 300
    hidden_layers = 2
    hidden_size = 16
    bidirectional = True
    output_size = 4
    max_epochs = 30
    lr = 0.25
    batch_size = 5000
    max_sen_len = 20 # Sequence length for RNN
    dropout_keep = 0.5