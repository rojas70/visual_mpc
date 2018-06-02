import os
import python_visual_mpc
current_dir = '/'.join(str.split(__file__, '/')[:-1])
bench_dir = '/'.join(str.split(__file__, '/')[:-2])

from python_visual_mpc.visual_mpc_core.algorithm.cem_controller_goalimage_sawyer import CEM_controller

ROOT_DIR = os.path.abspath(python_visual_mpc.__file__)
ROOT_DIR = '/'.join(str.split(ROOT_DIR, '/')[:-2])

from python_visual_mpc.visual_mpc_core.agent.agent_mjc import AgentMuJoCo
import numpy as np
agent = {
    'type': AgentMuJoCo,
    'T': 3,  #####################
    'substeps':200,
    'adim':5,
    'sdim':12,
    'make_final_gif':'',
    'filename': ROOT_DIR + '/mjc_models/cartgripper_grasp.xml',
    'filename_nomarkers': ROOT_DIR + '/mjc_models/cartgripper_grasp.xml',
    'gen_xml':1,   #generate xml every nth trajecotry
    'skip_first':10,
    'num_objects': 1,
    'object_mass':0.01,
    'friction':1.5,
    'viewer_image_height' : 480,
    'viewer_image_width' : 640,
    'image_height':48,
    'image_width':64,
    'sample_objectpos':'',
    'randomize_initial_pos':'',
    'const_dist':0.2,
    'data_save_dir':current_dir + '/data/train',
    'logging_dir':current_dir + '/logging',
    'posmode':"",
    'targetpos_clip':[[-0.5, -0.5, -0.08, -2 * np.pi, -1], [0.5, 0.5, 0.15, 2 * np.pi, 1]],
    'mode_rel':np.array([True, True, True, True, False]),
    'autograsp' : True,
    'cameras':['maincam', 'leftcam'],
    'verbose':"",
    'finger_sensors':''
    # 'compare_mj_planner_actions':'',
}

policy = {
    'verbose':'',
    'type' : CEM_controller,
    'low_level_ctrl': None,
    'current_dir':current_dir,
    'usenet': True,
    'nactions': 1,##############5,
    'repeat': 3,
    'initial_std': 0.02,   #std dev. in xy
    'initial_std_lift': 1.6,   #std dev. in xy
    'initial_std_rot' : np.pi / 18,
    'initial_std_grasp' : 0,
    'netconf': current_dir + '/conf.py',
    'iterations': 3,
    'action_cost_factor': 0,
    'rew_all_steps':"",
    'finalweight':10,
    # 'no_action_bound':"",
}

tag_images0 = {'name': 'images0',
             'file':'/images0/im{}.png',   # only tindex
             'shape':[agent['image_height'],agent['image_width'],3],
               }

tag_images1 = {'name': 'images1',
              'file':'/images1/im{}.png',   # only tindex
              'shape':[agent['image_height'],agent['image_width'],3],
              }

tag_qpos = {'name': 'qpos',
             'shape':[6],
             'file':'/state_action.pkl'}

tag_actions = {'name': 'actions',
            'shape':[15,5],
            'not_per_timestep':'',
            'file':'/state_action.pkl'}

tag_object_full_pose = {'name': 'object_full_pose',
                         'shape':[4,7],
                         'file':'/state_action.pkl'}
tag_object_statprop = {'name': 'obj_statprop',
                     'not_per_timestep':''}

config = {
    'current_dir':current_dir,
    'traj_per_file':16,   # needs to be equal batch size!!
    'save_data': True,
    'start_index':0,
    'end_index': 59999,
    'agent':agent,
    'policy':policy,
    'ngroup': 100,
    'sourcetags':[tag_images0, tag_images1, tag_qpos, tag_object_full_pose, tag_object_statprop, tag_actions],
    'source_basedirs':[os.environ['VMPC_DATA_DIR'] + '/cartgripper/grasping/cartgripper_startgoal_2view_lift_above_obj/train'],
    'sequence_length':2
}