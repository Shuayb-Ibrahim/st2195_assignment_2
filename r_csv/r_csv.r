library(rvest)
library(stringr)

wiki_cars <- read_html("https://en.wikipedia.org/wiki/Comma-separated_values")
str(wiki_cars)

popnodes <- html_nodes(wiki_cars, "table")
