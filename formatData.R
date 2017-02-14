#COMP3121
#MA Mingyu, 14110562D
#A R program transfer original hk_films.csv data to correct format that can be used in Gephi
library(dplyr)
library(magrittr)
hk_films <- read.csv("~/GoogleDrive/_SOCIAL/2_Assignments/ass1/hk_films.csv", stringsAsFactors = FALSE)
#Create proper nodes file
nodes_movies <- data.frame(id = unique(hk_films$movies)) %>%
  mutate(label = id, type = "movie")
nodes_actors <- data.frame(id = unique(hk_films$actors)) %>%
  mutate(label = id, type = "actors")
nodes <- data.frame()
nodes <- rbind(nodes_movies, nodes_actors)
write.csv(nodes, file="~/GoogleDrive/_SOCIAL/2_Assignments/ass1/hk_films_nodes.csv")
#Create proper edges file
edges <- hk_films
colnames(edges) <- c("source","target")
edges <- edges %>% mutate(type = "undirected")
write.csv(edges, file="~/GoogleDrive/_SOCIAL/2_Assignments/ass1/hk_films_edges.csv")
