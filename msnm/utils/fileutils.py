# -*- coding: utf-8 -*-
"""
    :mod:`File utilities`
    ===========================================================================
    :synopsis: Several methods to play with files
    :author: NESG (Network Engineering & Security Group) - https://nesg.ugr.es
    :contact: nesg@ugr.es, rmagan@ugr.es
    :organization: University of Granada
    :project: VERITAS - MSNM Sensor
    :since: 0.0.1  
"""

from msnm.modules.config.configure import Configure

import os
import logging


# types of files
# TODO

def get_generated_file(ts,type):
    '''
    This method is initially devised to get any of the files generated by the sensor under /data folder
    
    TODO: To be tested 
    
    '''
    
    # Config params
    config = Configure() 
    obs_generated_path = config.get_config()['Sensor'][type] # path where we searching for the file
    
    file_found = None
        
    for file_name in os.listdir(obs_generated_path):
        if os.path.isfile(os.path.join(obs_generated_path, file)):
            file_ts = file_name.split('.')[0][3:]
            if file_ts == ts:
                file_found = file_name
                break
    if not file_found: logging.warn("The file with ts %s was not found :(", ts)
    
    return os.path.join(obs_generated_path, file_found)

