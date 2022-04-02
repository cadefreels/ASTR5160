import numpy as np
from sklearn.datasets import load_iris
from sklearn import neighbors
import matplotlib.pyplot as plt

# CF From "Machine Learning Example"

iris = load_iris()

# CF Set column names for the iris data

colnames = "sepal_length sepal_width petal_length petal_width" 

# CF Plot the actual iris data and save figure

fig, ax = plt.subplots(1, 1, figsize=(8,6))
for i in range(3):
    target_class = iris.target == i
    ax.scatter(iris.data[target_class, 0], iris.data[target_class, 1], s=90, label=iris.target_names[i])
    ax.tick_params(labelsize=14)
    ax.set_xlabel("Sepal length (cm)", size=14)
    ax.set_ylabel("Sepal width (cm)", size=14)
    ax.legend(prop={'size': 14})
plt.savefig("/d/www/cade/public_html/irisdata.png")

# CF Want to use the k-nearest neighbors neighbors algorithm

knn = neighbors.KNeighborsClassifier(n_neighbors=1)
knn.fit(iris.data, iris.target)
mock_data = [5, 4, 1, 0]
mock_data = [6, 3, 4, 1]

# CF Get 2D sepal_length, sepal_width space
n = 100000
mock_data = []
for i in range(2):
    print("working on column: {}".format(colnames.split()[i]))
    col_min = np.min(iris.data[..., i])
    col_max = np.max(iris.data[..., i])
    mock_meas = np.random.random(n)*(col_max - col_min) + col_min
    mock_data.append(mock_meas)
# CF Make array into 2 columns and 2 rows.
mock_data = np.reshape(mock_data, (2, n)).T
mock_data

# CF Classify iris data using the k-nearest neighbors technique
knn = neighbors.KNeighborsClassifier(n_neighbors=1)
knn.fit(iris.data[..., :2], iris.target)
mock_target_class = knn.predict(mock_data)

# CF Plot sepal_length vs. sepal_width using the k-nearest neighbors technique to see how it classifies irises
fig, ax = plt.subplots(1, 1, figsize=(8,6))
for i in range(3):
    target_class = mock_target_class == i
    ax.scatter(mock_data[target_class, 0], mock_data[target_class, 1], s=10, label=iris.target_names[i])
    ax.tick_params(labelsize=14)
    ax.set_xlabel("Sepal length (cm)", size=14)
    ax.set_ylabel("Sepal width (cm)", size=14)
    ax.legend(prop={'size': 14})
plt.savefig("/d/www/cade/public_html/knniris.png")

# CF Find percentage of 100,000 irises that are classified as a virginica iris by the k-NN algorithm
# CF From the "Machine Learning Example", a value of 2 corresponds to the iris type 'virginica'"

ii = mock_target_class == 2

vir_perc = len(mock_target_class[ii]) / len(mock_target_class)

print(vir_perc)
