import os, yaml
import pandas as pd

if __name__ == '__main__':

    #import environnement variables
    set_environment()
    logger = get_logger(__file__)

    logger.info('Start module {0}'.format("cover"))

    #read the params variables 
    with open(os.path.join(os.environ['PATHCONF'],'params.yaml'),'r') as stream:
        params= yaml.safe_load(stream)
        logger.info('Default parameters : {0}'.format(params))

    #read strategy file_name
    inputdir = params['inputdir']
    strategy_filename = params['strategy_filename']
	df_strategy = pd.read_csv(filepath_or_buffer=os.path.join(os.path.join(inputdir,strategy_filename)), 
			sep='\s+')

	logger.info('{0}'.format(df_strategy.head()))

	return 0