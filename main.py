import os, yaml
import pandas as pd
import numpy as np
import logging
from app.utils import set_environment, get_logger


def optimimun_variable(logger: logging, df_strat: pd.DataFrame, var_name: str)-> pd.DataFrame:
    """Fonction to get the optimum over a set over strategy 

    Parameters
    ----------
    df_strat : DataFrame with strategies by id  
        if will remove the first date for all strategy's id
    var_name : name of the column to calculate the optimum variable 

    Returns
    -------
    df_opt : a dataframe with a list of id and the calculated optimum
        for var_name are rates : composed total return of each strategy
    """
    df_opt = df_strat\
        .reset_index()[['id',var_name]]\
        .groupby('id')\
        .apply(lambda x: np.mean(x[var_name]))

    return df_opt


def optimize(logger: logging, df_opt: pd.DataFrame) -> [int,float]:
    """Fonction to get the optimum over a set over strategy 

    Parameters
    ----------
    df_opt : dataFrame with index = id, value = single values 
        if will remove the first date for all strategy's id
         
    Returns
    -------
    [idxmax, value_max] : argmax and max value  

    """

    return [df_opt.idxmax(), df_opt.max()]


def split_training_test(logger: logging, df_strat: pd.DataFrame) -> [pd.DataFrame, pd.DataFrame]:
    
    """Fonction to split the training and test 

    Parameters
    ----------
    df_strat : DataFrame with all the strategy risk 
        if will remove the first date for all strategy's id
         
    Returns
    -------
    [df_test, df_train] : list of df_test and df_train 

    """

    # get all dates unique time series , drop first element and shuffle
    df_dates = pd.DataFrame(df_strat['date'].unique(),columns=['date'])\
        .sort_values(by=['date'])\
        .iloc[1:]\
        .sample(frac=1)

    # make train (0.8) and test (0.2)
    n_dates = len(df_dates)
    size_train = int(n_dates * 0.8)

    # get the training and test set
    df_index=df_strat.set_index(keys = 'date')

    df_train=df_index.loc[df_dates.iloc[0:size_train].values.flatten()]
    df_test=df_index.loc[df_dates.iloc[size_train:].values.flatten()]

    return [df_train, df_test]


if __name__ == '__main__':

#import environnement variables
    set_environment()
    logger = get_logger(__file__)

    logger.info('Start module {0}'.format("analysis"))

    #read the params variables 
    with open(os.path.join(os.environ['PATHCONF'],'params.yaml'),'r') as stream:
        params= yaml.safe_load(stream)
        logger.info('Default parameters : {0}'.format(params))

    #read strategy file_name
    inputdir = params['inputdir']
    strategy_filename = params['strategy_file']
    opt_variable = params['opt_variable']
    col_variables= params['col_variables']

    df_strategy = pd.read_csv(filepath_or_buffer=os.path.join(os.path.join(inputdir,strategy_filename)),sep='\\s+')

#split train and test
    df_strats = split_training_test(logger, df_strategy)

# get the variable to be maximized
    df_opts = list(map(lambda x: optimimun_variable(logger,x, opt_variable), df_strats))

# get the maximum in train and test it 
    id_max,value_max = optimize(logger, df_opts[0])

# get the variables corresponding to id_max
    cols_to_retrieve = ['id'] + col_variables 
    df_max = df_strategy[cols_to_retrieve].set_index(keys='id').loc[id_max].iloc[0]
        
    logger.info('col_variables max {0}'.format(df_max))
    logger.info('train id_max {0}, value_max {1}'.format(id_max, value_max))
    logger.info('test: value {0}'.format(df_opts[1].loc[id_max]))

