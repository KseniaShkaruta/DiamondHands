library('quantmod')
library('readr')
library('tidyverse')


mdf <- data.frame()
tickers = c('AMZN','BB','NAKD','GME','KOSS','AMC','^GSPC')
for (tkr in tickers){
    
    xts_df= getSymbols(tkr, 
                 from = as.character(Sys.Date()-(as.integer(12)*30)),
                 to = as.character(Sys.Date()),
                 env = NULL) # env null will assign to 
    
    df = fortify.zoo(xts_df)
    
    df$Index=as.character(df$Index)
    colnames(df)=c('Index','Open','High','Low','Close','Volume','Adjusted')
    
    if(tkr=='^GSPC'){
        tkr='SP500'
    }
    
    df = df %>% 
      plyr::rename(
        c("Index" = "Date")
        ) %>%
        dplyr::mutate(Stock=tkr) %>%
        dplyr::select(Stock,Date,Open,High,Low,Close,Volume,Adjusted)
    
    mdf = rbind(mdf,df)
}
write_csv(mdf, path="/tmp/stockdata_F.csv", append = FALSE, col_names = TRUE)
