# install.packages("JAVA")
# install.packages("chromedriver")
# 
# if (!require("RSelenium")) install.packages("RSelenium"); library(RSelenium)
# 
# rD <- rsDriver(browser = c("chrome"), chromever = "88.0.4324.96",
#                port = 4567L)
# cliente <- rD$client

#puxando os textos dos links

library("rvest")

page <- "https://piaui.folha.uol.com.br/lupa/2021/06/14/verificamos-washington-post-motociata-bolsonaro/"

page %>%
  read_html() %>%
  html_text("p/span")
