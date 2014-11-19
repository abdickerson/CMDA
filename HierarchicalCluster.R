data(iris)
names(iris)
head(iris)
summary(iris$Sepal.Length)
summary(iris$Sepal.Width)
summary(iris$Petal.Length)
summary(iris$Petal.Width)
summary(iris$Species)
features <- iris[,1:4]
scaled <- scale(features)
means <- attr(scaled,"scaled:center")
stdv <- attr(scaled, "scaled:scale")
distance <- dist(scaled, method = "euclidean")
hier_cl <- hclust(distance, method="ward.D")
plot(hier_cl, labels=iris$Species)
rect.hclust(hier_cl, k=3)
groups <- cutree(hier_cl, k = 3)
print(groups)
#Setosa occupies the first cluster
#virginica occupies the second cluster
#versicolor occupies the third cluster

#InClass10_2

kmeans_clusters <- kmeans(distance, 5 , nstart=100, iter.max=100)
kmeans_clusters
kmeans_clusters$cluster
kmeans_clusters$centers

kmeans_clusters$withinss
kmeans_clusters$tot.withinss
kmeans_clusters$betweenss

kmeans_clusters$size

compare <- cbind(groups,kmeans_clusters$cluster)
compare <- as.data.frame(compare)
compare <- cbind(iris$Species,compare)
names(compare) <- c("Species", "Hierarchical", "kmeans")
compare

compare1 <- compare[order(compare$Hierarchical),]
compare1
compare2 <- compare[order(compare$kmeans),]
compare2
#There are not any major differences in the iris plant assignments to the three different
#clusters. I wouldn't say the clusters are perfectly separated, but it is pretty
#accurate to the known Species separation.