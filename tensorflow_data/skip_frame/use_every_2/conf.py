import os
current_dir = os.path.dirname(os.path.realpath(__file__))

# tf record data location:
DATA_DIR = '/home/frederik/Documents/pushing_data/train'

# local output directory
OUT_DIR = current_dir + '/modeldata_old1'

configuration = {
'experiment_name': 'skip_frame4',
'data_dir': DATA_DIR,       # 'directory containing data.' ,
'output_dir': OUT_DIR,      #'directory for model checkpoints.' ,
'current_dir': current_dir,   #'directory for writing summary.' ,
'num_iterations': 100000,   #'number of training iterations.' ,
'pretrained_model' : '',
'sequence_length': 15,      # 'sequence length, including context frames.' ,
'skip_frame': 2,            # 'use ever ith frame to increase prediction horizon' ,
'context_frames': 2,        # of frames before predictions.' ,
'use_state': 1,             #'Whether or not to give the state+action to the model' ,
'model': 'CDNA',            #'model architecture to use - CDNA, DNA, or STP' ,
'num_masks': 10,            # 'number of masks, usually 1 for DNA, 10 for CDNA, STN.' ,
'schedsamp_k': 900.0,       # 'The k hyperparameter for scheduled sampling -1 for no scheduled sampling.' ,
'train_val_split': 0.95,    #'The percentage of files to use for the training set vs. the validation set.' ,
'batch_size': 32,           #'batch size for training' ,
'learning_rate': 0.001,     #'the base learning rate of the generator' ,
'visualize': '',            #'load model from which to generate visualizations
                            # don't modify here, pass as an argument for prediction_train
'downsize': False,          #'create downsized model'
}