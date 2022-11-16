import os, logging.config

def get_logger(logger_file = None): 
    """returns the default logger
    
    Paramaters
    ----------
    logger_file : None

    Returns
    -------
    logger : obj of the default logger  
    """
    if logger_file == None: 
        logger_file = __file__

    result =  logging.getLogger(os.path.basename(logger_file))

    return result

def set_environment():
    """If not set, the function will set the default environnement variable of PATHCONF to
        ./conf/dev
        and will set the logging configuration 

    Paramaters
    ----------
    None

    Returns
    -------
    0  
    """   
    pathconf = os.getenv('PATHCONF',default = './conf')

    logging.config.fileConfig(os.path.join(pathconf,'logging.conf'))

    logger = get_logger()

    logger.info('os.environ[PATHCONF] : {0}'.format(pathconf))

    os.environ['PATHCONF'] = pathconf

    return 0