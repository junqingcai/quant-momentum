def initialize(context):
    g.stocks = [
        '512400.XSHG',
        '159980.XSHE',
        '161226.XSHE',
        '518880.XSHG',
        '512010.XSHG'
    ]
    
    g.lookback = 20
    
    run_monthly(rebalance, 1)


def rebalance(context):
    scores = {}
    
    for stock in g.stocks:
        df = attribute_history(stock, g.lookback, '1d', ['close'])
        
        if len(df) < g.lookback:
            continue
        
        ret = df['close'][-1] / df['close'][0] - 1
        scores[stock] = ret
    
    sorted_stocks = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    
    if sorted_stocks[0][1] < 0:
        target_stocks = ['518880.XSHG']
    else:
        target_stocks = [s[0] for s in sorted_stocks[:3]]
    
    total_value = context.portfolio.total_value
    
    weight = total_value / len(target_stocks)
    
    for stock in context.portfolio.positions:
        if stock not in target_stocks:
            order_target_value(stock, 0)
    
    for stock in target_stocks:
        order_target_value(stock, weight)