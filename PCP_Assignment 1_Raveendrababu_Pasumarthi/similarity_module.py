import math
def vector_xy(d,id1,id2):
    vector_1 = [d[id1]['acousticness'],d[id1]['danceability'],d[id1]['energy'],d[id1]['liveness']
     ,d[id1]['popularity'],d[id1]['speechiness'],d[id1]['tempo'],d[id1]['valence']]
    vector_2 = [d[id2]['acousticness'],d[id2]['danceability'],d[id2]['energy'],d[id2]['liveness']
     ,d[id2]['popularity'],d[id2]['speechiness'],d[id2]['tempo'],d[id2]['valence']]
    return vector_1,vector_2
def euclidean_similarity_func(d,id1,id2):      
    x , y = vector_xy(d,id1,id2)
    x = (float(i) for i in x)
    y = (float(i) for i in y)
    euclidean_distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
    return euclidean_distance
def cosine_similarity_func(d,id1,id2):      
    x , y = vector_xy(d,id1,id2)
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(x)):
        v1 = float(x[i]); v2 = float(y[i])
        sumxx += v1*v1
        sumyy += v2*v2
        sumxy += v1*v2
    cos_sim_distnace = sumxy/math.sqrt(sumxx*sumyy)
    return cos_sim_distnace
def manhattan_similarity_func(d,id1,id2):      
    x , y = vector_xy(d,id1,id2)
    x = (float(i) for i in x)
    y = (float(i) for i in y)
    man_sim_distnace = sum(abs(a-b) for a,b in zip(x,y))
    return man_sim_distnace
def jaccard_similarity_func(d,id1,id2):      
    x , y = vector_xy(d,id1,id2)
    x = (float(i) for i in x)
    y = (float(i) for i in y)
    s1 = set(x)
    s2 = set(y)
    jaccard_sim_distnace = float(len(s1.intersection(s2)) / len(s1.union(s2)))
    return jaccard_sim_distnace
def pearson_similarity_func(d,id1,id2):      
    x , y = vector_xy(d,id1,id2)
    x = [float(i) for i in x]
    y = [float(i) for i in y]
    n = len(x)
    sum_x = float(sum(x))
    sum_y = float(sum(y))
    sum_x_sq = sum(map(lambda x: pow(x, 2), x))
    sum_y_sq = sum(map(lambda x: pow(x, 2), y))
    psum = sum(map(lambda x, y: x * y, x, y))
    num = psum - (sum_x * sum_y/n)
    den = pow((sum_x_sq - pow(sum_x, 2) / n) * (sum_y_sq - pow(sum_y, 2) / n), 0.5)
    if den == 0: pearson_sim_distnace = 0   
    pearson_sim_distnace = num / math.sqrt(den)
    return pearson_sim_distnace
def euclidean_similarity_one_func(x,y):      
    x = (float(i) for i in x)
    y = (float(i) for i in y)
    euclidean_distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
    return euclidean_distance
def cosine_similarity_one_func(x,y):      
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(x)):
        v1 = float(x[i]); v2 = float(y[i])
        sumxx += v1*v1
        sumyy += v2*v2
        sumxy += v1*v2
    cos_sim_distnace = sumxy/math.sqrt(sumxx*sumyy)
    return cos_sim_distnace
def manhattan_similarity_one_func(x,y):      
    x = (float(i) for i in x)
    y = (float(i) for i in y)
    man_sim_distnace = sum(abs(a-b) for a,b in zip(x,y))
    return man_sim_distnace
def jaccard_similarity_one_func(x,y):      
    x = (float(i) for i in x)
    y = (float(i) for i in y)
    s1 = set(x)
    s2 = set(y)
    jaccard_sim_distnace = float(len(s1.intersection(s2)) / len(s1.union(s2)))
    return jaccard_sim_distnace
def pearson_similarity_one_func(x,y):     
    n = len(x)
    x = [float(i) for i in x]
    y = [float(i) for i in y]
    sum_x = float(sum(x))
    sum_y = float(sum(y))
    sum_x_sq = sum(map(lambda x: pow(x, 2), x))
    sum_y_sq = sum(map(lambda x: pow(x, 2), y))
    psum = sum(map(lambda x, y: x * y, x, y))
    num = psum - (sum_x * sum_y/n)
    den = pow((sum_x_sq - pow(sum_x, 2) / n) * (sum_y_sq - pow(sum_y, 2) / n), 0.5)
    if den == 0: pearson_sim_distnace = 0   
    pearson_sim_distnace = num / math.sqrt(den)
    return pearson_sim_distnace
