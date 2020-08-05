import requests
import pandas as pd 
from yahoo_fin import stock_info as si 

'''
Inputs for the ?modules= query:

modules = [
   'assetProfile',
   'summaryProfile',
   'summaryDetail',
   'esgScores',
   'price',
   'incomeStatementHistory',
   'incomeStatementHistoryQuarterly',
   'balanceSheetHistory',
   'balanceSheetHistoryQuarterly',
   'cashflowStatementHistory',
   'cashflowStatementHistoryQuarterly',
   'defaultKeyStatistics',
   'financialData',
   'calendarEvents',
   'secFilings',
   'recommendationTrend',
   'upgradeDowngradeHistory',
   'institutionOwnership',
   'fundOwnership',
   'majorDirectHolders',
   'majorHoldersBreakdown',
   'insiderTransactions',
   'insiderHolders',
   'netSharePurchaseActivity',
   'earnings',
   'earningsHistory',
   'earningsTrend',
   'industryTrend',
   'indexTrend',
   'sectorTrend' ]

Example URL:
https://query1.finance.yahoo.com/v10/finance/quoteSummary/AAPL?modules=assetProfile%2CearningsHistory
'''

# tickers = si.tickers_sp500()
tickers = ['TSLA','AAPL']
recommendations = []

for ticker in tickers:
    lhs_url = 'https://query2.finance.yahoo.com/v10/finance/quoteSummary/'
    rhs_url = '?modules=financialData'
              
    url =  lhs_url + ticker + rhs_url
    r = requests.get(url)
    
    if not r.ok:
        recommendation = 'None'
    try:
        result = r.json()['quoteSummary']['result'][0]
        recommendation =result['financialData']['recommendationMean']['fmt']
    except:
        recommendation = 'None'
    
    recommendations.append(recommendation)
    
    # print("--------------------------------------------")
    # print ("{} has an average recommendation of: ".format(ticker), recommendation)
    # time.sleep(0.5)
    
df = pd.DataFrame(list(zip(tickers, recommendations)), columns =['Company', 'Recommendations']) 
df = df.set_index('Company')
# df.to_csv('stock_recommendations.csv')
print(df)