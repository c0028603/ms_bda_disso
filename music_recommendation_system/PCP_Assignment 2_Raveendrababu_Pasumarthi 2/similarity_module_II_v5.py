import math
import pandas as pd
import numpy as np
from scipy import spatial
from scipy.spatial import distance
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics import accuracy_score
class similarity_score(): # similarity score class 
    def __init__(self,var1,var2,ftr,x,y):   #constructor with required inputs to its methods            
        self.var1 = var1
        self.var2 = var2
        self.ftr = ftr
        self.x = x
        self.y = y
        self.metric = ['euclidean distance','cosine similarity','jaccard distance','manhattan distance','pearson distance']        
    def euclidean_similarity(self):  # method to returns euclidean distance
        self.euclidean_distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(self.x, self.y)]))
        return round(self.euclidean_distance,4)
    def cosine_similarity(self):   # method to calculate cosine similarity
        sumxx, sumxy, sumyy = 0, 0, 0
        for i in range(len(self.x)):
            v1 = float(self.x[i])
            v2 = float(self.y[i])
            sumxx += v1*v1
            sumyy += v2*v2
            sumxy += v1*v2
        self.cos_sim_distnace = sumxy/math.sqrt(sumxx*sumyy)
        return round(self.cos_sim_distnace,4)
    def manhattan_similarity(self): # method to calculate manhattan distance 
        self.man_sim_distnace = sum(abs(a-b) for a,b in zip(self.x,self.y))        
        return round(self.man_sim_distnace,4)    
    def jaccard_similarity(self): #method to calculate jaccard similarity      
        s1 = set(self.x)
        s2 = set(self.y)
        self.jaccard_sim_distnace = float(len(s1.intersection(s2)) / len(s1.union(s2)))       
        return round(self.jaccard_sim_distnace,4)
    def pearson_similarity(self): #method to caclulate the pearson similarity
        x = self.x
        y = self.y
        n = len(x)
        sum_x = float(sum(x))
        sum_y = float(sum(y))
        sum_x_sq = sum(map(lambda x: pow(x, 2), x))
        sum_y_sq = sum(map(lambda y: pow(y, 2), y))
        psum = sum(map(lambda x, y: x * y, x, y))
        num = psum - (sum_x * sum_y/n)
        den = pow((sum_x_sq - pow(sum_x, 2) / n) * (sum_y_sq - pow(sum_y, 2) / n), 0.5)        
        if den == 0: self.pearson_sim_distnace = 0   
        self.pearson_sim_distnace = round(num,4) / math.sqrt(round(den,4))          
        return round(self.pearson_sim_distnace,4)
    def get_score_dataframe(self):
        ed = self.euclidean_similarity();cs = self.cosine_similarity();js = self.jaccard_similarity();ms = self.manhattan_similarity();ps = self.pearson_similarity()        
        metric_df_multi_feat = pd.DataFrame(columns = self.metric,index = [self.var1[0]+' To '+self.var2[0]])                   
        metric_df_multi_feat['euclidean distance'] = float(ed)           
        metric_df_multi_feat['cosine similarity'] = float(cs)            
        metric_df_multi_feat['jaccard distance'] = float(js)           
        metric_df_multi_feat['manhattan distance'] = float(ms)             
        metric_df_multi_feat['pearson distance'] = float(ps)
        self.metric_df_multi_feat = metric_df_multi_feat                                          
        return self.metric_df_multi_feat
    def get_similarity_results_artists(self):  #method to return the result dataframe                 
        if len(self.x) == 1 and len(self.y) == 1: # if user chooses one feature , the feature values of albums/artist(s) returned as a dataframe 
            print(self.ftr[0],"results")            
            self.metric_df_one_feat = pd.DataFrame(columns = [self.ftr[0]] ,index = [self.var1[0],self.var2[0]])
            self.metric_df_one_feat.loc[self.var1[0]] = round(self.x[0],4)
            self.metric_df_one_feat.loc[self.var2[0]] = round(self.y[0],4)                       
            return self.metric_df_one_feat             
        else: #returns the dataframe of all the feature values of chosen albums/artits            
            print("Selected Artists             :",self.var1[0]," and ",self.var2[0],";")
            print("Selected Features            :",[x for x in self.ftr],"; and ")
            print("The similarity distances are :")
            self.metric_df_multi_feat = self.get_score_dataframe()
            return self.metric_df_multi_feat
    def get_similarity_results_albums(self):  #method to return the result dataframe                 
        if len(self.x) == 1 and len(self.y) == 1: # if user chooses one feature , the feature values of albums/artist(s) returned as a dataframe 
            print(self.ftr[0],"results")            
            self.metric_df_one_feat = pd.DataFrame(columns = [self.ftr[0]] ,index = [self.var1[0],self.var2[0]])
            self.metric_df_one_feat.loc[self.var1[0]] = round(self.x[0],4)
            self.metric_df_one_feat.loc[self.var2[0]] = round(self.y[0],4)                       
            return self.metric_df_one_feat             
        else: #returns the dataframe of all the feature values of chosen albums/artits            
            print("Selected Albums             :",self.var1[0]," and ",self.var2[0],";")
            print("Selected Features            :",[x for x in self.ftr],"; and ")
            print("The similarity distances are :")
            self.metric_df_multi_feat = self.get_score_dataframe()
            return self.metric_df_multi_feat
class top_n_recom(): # top n recommendations class 
    def __init__(self,v1,v2):#constructor with required inputs to its methods
        self.v1 = v1
        self.v2 = v2  
        self.metrics = ['euclidean','cosine','jaccard','cityblock','correlation']   #list of metrics
    def top_n_albums_distance(self,metric): #method to calculate the distance between two albums for a given metric vectors shape(1,n)
        self.dist = distance.cdist(self.v1, self.v2, metric)
        self.distance_df = pd.DataFrame(np.transpose(self.dist),columns = [metric],index = list(self.v2.index.values))
        self.distance_df = self.distance_df.sort_values(metric).head(20)
        self.distance_df_ids = self.distance_df.index.tolist()
        return self.distance_df_ids,self.distance_df
    def top_n_artists_distance(self,metric): #method to calculate the distance between two artists for a given metric. vectors shape (n,n)
        self.dist = distance.cdist(self.v1, self.v2, metric)
        self.distance_df = pd.DataFrame(np.transpose(self.dist),columns = list(self.v1.index.values),index = list(self.v2.index.values))         
        self.distance_df['index'] = self.distance_df.index  # take index as column to flatten all data        
        self.distance_df = self.distance_df.melt(id_vars=['index'], value_vars=list(self.v1.index.values)) # melt the dataframe all songs scores of an artists are flattenned/melted         
        self.distance_df = self.distance_df.drop_duplicates(subset=['index', 'value']) # remove(dedup) the same scores/distances        
        self.distance_df = self.distance_df.sort_values(by=['value']) #sort the unique scores in ascending order 
        self.distance_df = self.distance_df.drop_duplicates(subset=['index']) # remove(dedup) the repeted artists        
        self.distance_df = self.distance_df.head(20) # choose top 20 results         
        #self.distance_df_ids = self.distance_df['index'].tolist() # ids of the top 20 results into a list           
        return self.distance_df
    def get_dict_artists(self,df1,df2,simil): #method to create single dataframe from the two dataframes of top n artists results
        self.artists = df1.values.tolist()
        self.values = df2.values.tolist()
        self.d = {'artists':self.artists,simil:self.values}
        self.topnartistsdf = pd.DataFrame(self.d)
        return self.topnartistsdf
    def get_results_top_n_album(self,Obj):       # results of all the chosen metrics for the target album         
        eucledean_ids,eucledean_df = self.top_n_albums_distance(self.metrics[0])
        cosine_ids,cosine_df = self.top_n_albums_distance(self.metrics[1])
        jaccard_ids,jaccard_df = self.top_n_albums_distance(self.metrics[2])
        manhattan_ids,manhattan_df = self.top_n_albums_distance(self.metrics[3])
        correlation_ids,correlation_df = self.top_n_albums_distance(self.metrics[4])
        #df = dataset.dataframe['name'].loc[eucledean_ids] + [eucledean_df.loc[eucledean_ids]
        self.result1 = pd.concat([Obj.dataframe['name'].loc[eucledean_ids], eucledean_df.loc[eucledean_ids]], axis=1)
        self.result2 = pd.concat([Obj.dataframe['name'].loc[cosine_ids], cosine_df.loc[cosine_ids]], axis=1)
        self.result3 = pd.concat([Obj.dataframe['name'].loc[jaccard_ids], jaccard_df.loc[jaccard_ids]], axis=1)
        self.result4 = pd.concat([Obj.dataframe['name'].loc[manhattan_ids], manhattan_df.loc[manhattan_ids]], axis=1)
        self.result5 = pd.concat([Obj.dataframe['name'].loc[correlation_ids], correlation_df.loc[correlation_ids]], axis=1)
        return self.result1,self.result2,self.result3,self.result4,self.result5
    def get_results_top_n_artist(self,Obj):       # results of all the chosen metrics for the target artist         
        self.eucledean_df = self.top_n_artists_distance(self.metrics[0])                       
        self.cosine_df = self.top_n_artists_distance(self.metrics[1])       
        self.jaccard_df = self.top_n_artists_distance(self.metrics[2])        
        self.manhattan_df = self.top_n_artists_distance(self.metrics[3])        
        self.correlation_df = self.top_n_artists_distance(self.metrics[4])  
        self.result11 = Obj.dataframe['artists'].loc[self.eucledean_df['index']];self.result12 = self.eucledean_df['value'] 
        self.result21 = Obj.dataframe['artists'].loc[self.cosine_df['index']];self.result22 = self.cosine_df['value'] 
        self.result31 = Obj.dataframe['artists'].loc[self.jaccard_df['index']];self.result32 = self.jaccard_df['value'] 
        self.result41 = Obj.dataframe['artists'].loc[self.manhattan_df['index']];self.result42 = self.manhattan_df['value'] 
        self.result51 = Obj.dataframe['artists'].loc[self.correlation_df['index']];self.result52 = self.correlation_df['value']               
        return self.get_dict_artists(self.result11,self.result12,self.metrics[0]),self.get_dict_artists(self.result21,self.result22,self.metrics[1]),self.get_dict_artists(self.result31,self.result32,self.metrics[2]),self.get_dict_artists(self.result41,self.result42,self.metrics[3]),self.get_dict_artists(self.result51,self.result52,self.metrics[4])             
    def get_metrics_accuracy_album(self,Obj,metric,tgt_list,sample_list,ftr): #method to compare true score vs predicted score using nearest neibours algorithm    
        target = Obj.get_required_features_by_index(tgt_list,ftr) 
        sample = Obj.get_required_features_by_index(sample_list,ftr)  
        neigh = NearestNeighbors(n_neighbors=20,metric = metric)     
        neigh.fit(sample)
        self.pred_score = neigh.kneighbors(target,return_distance=False)
        #print("order oder oder ",self.pred_score[0]) 
        true_score = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]    
        true_score = np.array(true_score)         
        self.pred_accuracy = accuracy_score(true_score, self.pred_score[0])
        return self.pred_accuracy
    def get_results_accuracy_comparision_album(self,dataset): #method to get complete results of accuracy metrics album
        #['euclidean','cosine','jaccard','cityblock','correlation']
        ftr = ['acousticness','danceability','energy','liveness','loudness','popularity','speechiness','tempo','valence'] 
        tgt_list = self.v1.index.values.tolist()
        sample_list_1 = self.result1.index.values.tolist();sample_list_2 = self.result2.index.values.tolist()
        sample_list_3 = self.result3.index.values.tolist();sample_list_4 = self.result4.index.values.tolist()
        sample_list_5 = self.result5.index.values.tolist()#;print(sample_list_1,sample_list_2,sample_list_3,sample_list_4,sample_list_5)
        accuracy_score_metric_1 =  self.get_metrics_accuracy_album(dataset,'euclidean',tgt_list,sample_list_1,ftr)       
        accuracy_score_metric_2 =  self.get_metrics_accuracy_album(dataset,'cosine',tgt_list,sample_list_2,ftr)        
        accuracy_score_metric_3 =  self.get_metrics_accuracy_album(dataset,'jaccard',tgt_list,sample_list_3,ftr)        
        accuracy_score_metric_4 =  self.get_metrics_accuracy_album(dataset,'cityblock',tgt_list,sample_list_4,ftr)       
        accuracy_score_metric_5 =  self.get_metrics_accuracy_album(dataset,'correlation',tgt_list,sample_list_5,ftr)
        cols = ['metric','accuracy score in %']
        data = {'metric':['euclidean distance','cosine similarity','jaccard distance','manhattan distance','pearson distance'],
                'accuracy score in %': [accuracy_score_metric_1,accuracy_score_metric_2,accuracy_score_metric_3,accuracy_score_metric_4,accuracy_score_metric_5]}
        self.metrics_acc_df = pd.DataFrame(data,columns = cols)     
        return self.metrics_acc_df
    def get_results_accuracy_comparision_artist(self,dataset): #method to retreive results of accuracy metrics artist 
        #['euclidean','cosine','jaccard','cityblock','correlation']
        ftr = ['acousticness','danceability','energy','liveness','loudness','popularity','speechiness','tempo','valence'] 
        tgt_list1 = self.eucledean_df['variable'].values.tolist();sample_list_1 = self.eucledean_df['index'].values.tolist()
        tgt_list2 = self.cosine_df['variable'].values.tolist();sample_list_2 = self.cosine_df['index'].values.tolist()
        tgt_list3 = self.jaccard_df['variable'].values.tolist();sample_list_3 = self.jaccard_df['index'].values.tolist()
        tgt_list4 = self.manhattan_df['variable'].values.tolist();sample_list_4 = self.manhattan_df['index'].values.tolist()
        tgt_list5 = self.correlation_df['variable'].values.tolist();sample_list_5 = self.correlation_df['index'].values.tolist()
        accuracy_score_metric_1 =  self.get_metrics_accuracy_album(dataset,'euclidean',tgt_list1,sample_list_1,ftr)       
        accuracy_score_metric_2 =  self.get_metrics_accuracy_album(dataset,'cosine',tgt_list2,sample_list_2,ftr)        
        accuracy_score_metric_3 =  self.get_metrics_accuracy_album(dataset,'jaccard',tgt_list3,sample_list_3,ftr)        
        accuracy_score_metric_4 =  self.get_metrics_accuracy_album(dataset,'cityblock',tgt_list4,sample_list_4,ftr)       
        accuracy_score_metric_5 =  self.get_metrics_accuracy_album(dataset,'correlation',tgt_list5,sample_list_5,ftr)
        cols = ['metric','accuracy score in %']
        data = {'metric':['euclidean distance','cosine similarity','jaccard distance','manhattan distance','pearson distance'],
                'accuracy score in %': [accuracy_score_metric_1,accuracy_score_metric_2,accuracy_score_metric_3,accuracy_score_metric_4,accuracy_score_metric_5]}
        self.metrics_acc_df = pd.DataFrame(data,columns = cols)     
        return self.metrics_acc_df 

        

            
    
        