stock_eg = getSymbols("GME", 
           from = "2020-08-14",
           to = "2021-03-17",
           env = NULL) # env null will assign to 
stock_eg = fortify.zoo(stock_eg)


sent_eg = st_data %>% dplyr::filter(stringr::str_detect(stk,"GME")) %>% dplyr::select(dt) %>% dplyr::mutate(ct=1) %>%
       group_by(dt) %>% 
       summarise(sum(ct,na.rm=TRUE)) %>%
       rename(c("CORR_ONE"="sum(ct, na.rm = TRUE)"))


stock_eg = stock_eg %>% dplyr::select(Index,ends_with("Adjusted"))
colnames(stock_eg) = c("Index","CORR_TWO") 

corr_df = sent_eg %>% dplyr::inner_join(stock_eg, by=c("dt"="Index"))

highchart() %>%
  hc_yAxis_multiples(
  list(min=0, title=list(text="input$corr_stock_var")),
  list(opposite = TRUE, title=list(text="input$corr_sent_var") )
) %>%
hc_title(text = "TITLE",
       margin = 20, align = "center")  %>%
hc_xAxis(categories = corr_df$dt, title=list(text = "Week Ending")) %>%

hc_add_series(name = "input$corr_stock_var", data = corr_df$CORR_ONE, yAxis=0) %>%
hc_add_series(name = "input$corr_sent_var", data = corr_df$CORR_TWO,  yAxis = 1) %>%
hc_tooltip(shared=TRUE) %>%
hc_colors(  brewer.pal(2, "Dark2") )





















