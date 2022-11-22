# analysis
analysis of trading strategies

# Strategies tested
The optimisation is done in a training test of 80% of the yearly returns and the test results over 20% is described in the table 
| Strategy | Short | Long | Excess Return | description |
| -------- | ----- | ---- | ------------- | ----------- |
| MACD     | 40    | 90   | [-0.05,0.10]  | EMA of PRICE and log returns |
| MACD2     | 35    | 110   | [-0.05,0.09]    | EMA of (H+L)/2 and log returns constant optinum value |
| MACD3     | 45    | 100   | [-0.04,0.09]    | EMA of (H+L)/2 and price returns constant optinum value (more stable) |
| MACD4     | 30    | 100   | [-0.10,0.05]    | MA of (H+L)/2 not stable more negative returns |
| MACD5     | 15    | 70    | [-0.05,0.10]    | FirstOrder Bilinear Filter (H+L)/2 some negative returns |


 # linking notebooks
 jupyter lab --ip="*" --port=9000 --allow-root &

