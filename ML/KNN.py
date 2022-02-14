import numpy as np 
from scipy import spatial


def init_centers(X, k = 5):
    """function takes in an np.array() of N dimensions and cluster centers k
    and returns k number of points from the array"""
    rand_index = np.random.choice(len(X),size = k, replace=False)
    return X[rand_index, : ]
  
def dist_from_cen(X, centers, order_num = 1):
    """function takes N-D array X and N-D array of centers of length k
    and returns the distance of each element in X to centers"""
    m = len(X)
    if len(centers.shape) == 1: 
        centers = centers.reshape((1,len(centers)))
       
    k = len(centers)

    dist_matrix = np.empty((m,k))  # len(X) long, len(centers) wide
    
    for i in range(m):
        dist = np.linalg.norm(X[i, :] - centers, ord=order_num, axis=1)
        # for each coordinate point find dist to all centers
        dist_matrix[i, :] = dist ** order_num
        
    return dist_matrix
  
def assign_cluster(dist_matrix):
    """ funtion takes in the distance matrix and finds the minimum distance t
        to the cluster centers"""
    return np.argmin(dist_matrix, axis = 1)
  
def new_center(X, cluster_labels):
    """Function groups all values assigned to cluster and computes the new
    cluster center from the average of all points in the N-D matrix"""
    
    m, d = X.shape
    k = max(cluster_labels) + 1
    
    updated_centers = np.empty((k, d))
    for i in range(k):
        updated_centers[i, :d] = np.mean(X[cluster_labels == i, :], axis=0)
    return updated_centers
  
def has_converged(old_centers, centers):
    return set([tuple(x) for x in old_centers]) == set([tuple(x) for x in centers])
  
def k_means(X, k, start_centers = None, max_steps = np.inf, o_num = 2):
    if start_centers is None:
        centers = init_centers(X,k)
    else:
        centers = start_centers
        
    cnt =1
    converged = False
    labels = np.zeros(len(X))
    
    while (not converged) and (cnt <= max_steps):
        old_centers = centers
        dist = dist_from_cen(X,old_centers, order_num= o_num)
        labels = assign_cluster(dist)
        centers = new_center(X, labels)
        converged = has_converged(old_centers, centers)
        cnt +=1
        
    return labels , centers
  
def k_mediod(X, k, o_num = 2,start_centers = None, max_steps = np.inf):
    
    if start_centers is None:
        centers = init_centers(X,k)
    else:
        centers = start_centers
    
    cnt = 1
    converged = False
    labels = np.zeros(len(X))
    
    while (not converged) and (cnt < max_steps):
        old_centers = centers
        dist = dist_from_cen(X, old_centers, order_num= o_num)
        labels = assign_cluster(dist)
        centers = mediod_update(X, old_centers, labels, pnum = o_num)
        converged = has_converged(old_centers, centers)
        cnt +=1
        
    return labels , centers
  
  
  
  
  
