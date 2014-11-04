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