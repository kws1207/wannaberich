import FinanceDataReader as fdr

stocks = fdr.StockListing('NYSE')

print(stocks.columns)
