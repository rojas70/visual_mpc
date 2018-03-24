import os

DATA_DIR = os.environ['VMPC_DATA_DIR']
from python_visual_mpc.imitation_model.imitation_model import ImitationLSTMModelState
configuration = {
    'model' : ImitationLSTMModelState,
    'data_dir':DATA_DIR  + '/cartgripper_det_grasp/train/',
    'model_dir':DATA_DIR + '/cartgripper_det_grasp/lstm_model_mdn_states/',
    'n_iters':80000,
    'n_print':100,
    'n_save':500,
    'learning_rate':5e-3,
    'train_val_split':0.95,
    'adim':5,
    'sdim':12,
    'orig_size': [48,64],
    'skip_frame' : 1,
    'sequence_length' : 15,
    'batch_size' : 64,
    'vgg19_path': DATA_DIR,
    'MDN_loss' : 20,
    'lstm_layers':[100, 100, 100]
}

