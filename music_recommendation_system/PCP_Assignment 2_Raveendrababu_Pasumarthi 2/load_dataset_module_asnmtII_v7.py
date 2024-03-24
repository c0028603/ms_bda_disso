import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt
#import seaborn as sns
#define the load module class
class music_dataset:
    def __init__(self): #create costructor of dataset 
        self.filename = 'data.csv'
        self.dataset = pd.read_csv(self.filename,sep = ',')
        self.dataframe = pd.DataFrame(self.dataset)
    def get_data(self): # method to retrieve complete records in a dataframe      
        return self.dataframe
    def get_music_props_by_music_id(self,music_id):
        music_props = ['id','artists','name','duration_ms','release_date','year']
        return self.dataframe[self.dataframe['id'].isin(music_id)][music_props]          
    def get_sample_data(self): # method to see sample top 5 records of the music dataset
        return self.dataframe.head()
    def get_distinct_album_list(self): # method to retrieve album list        
        return self.dataframe.name.nunique()
    def get_album_title_by_music_id(self,music_id): #method to retrieve album by music id. music id parameter to be passed        
        return self.dataframe[self.dataframe['id'].isin(music_id)].name
    def get_artist_by_music_id(self,music_id): #method to retrieve album by music id. music id parameter to be passed        
        return self.dataframe[self.dataframe['id'].isin(music_id)].artists
    def get_music_id_by_album_name(self,music_title): #method to retrieve music id based on album title, album title parameter to be passed        
        return self.dataframe[self.dataframe['name'] == music_title].id
    def get_music_id_by_artist_name(self,artist_name):#method to retrieve music id based on artist name  
        artist_name1 = "['" + artist_name + "']" #concatenating "['" and "']" to find exact single aritist                   
        if len(self.dataframe[self.dataframe['artists'] == artist_name1]) >= 1: #use single artist data first for similarites else multi artists  data        
            return self.dataframe[self.dataframe['artists'] == artist_name1].id            
        return self.dataframe[self.dataframe['artists'].str.contains(artist_name)].id #use multi-artists data if no single artist data found               
    def get_distinct_artists_list(self): #method to retrieve distinct artists list
        self.artist = self.dataframe.artists.str.split(', ', expand=True).add_prefix('Artist')#separate artist names into diff columns
        self.artist = self.artist.stack().reset_index()#stack all columns into one column
        self.artist = self.artist.rename(columns={"level_0": "level_0", "level_1": "level_1", 0: "artist"}) #rename required column name
        self.artist = self.artist['artist'].str.split('/', expand=True).add_prefix('Artist') # again separte artists into multiple columns based on the slash(/) character
        self.artist = self.artist.stack().reset_index() #combine all columns into one column 
        self.artist = self.artist.rename(columns={"level_0": "level_0", "level_1": "level_1", 0: "artist"}) #rename required column name
        self.artist['artist'] = self.artist['artist'].str.replace('[','') # remove the character "[" from artist
        self.artist['artist'] = self.artist['artist'].str.replace(']','') # remove the character "]" from artist
        self.artist['artist'] = self.artist['artist'].str.replace("'",'')#remove unwanted single quote from artist name
        #self.artist['artist'] = self.artist['artist'].str.replace(" '",'')#remove unwated space and single quote(" '") from artistname
        i = self.artist[(self.artist['artist'] == 'n') | (self.artist['artist'] == 'a')].index
        self.artist = self.artist.drop(i) #remove the artist name "n/a"           
        return self.artist['artist'].unique() #return unique artist names list
    def get_artist(self,userchoice): #method to store the results of an user input artist
        self.artist = pd.DataFrame(self.get_distinct_artists_list())
        self.artist = self.artist.rename(columns={0: "artist"})        
        return self.artist[self.artist['artist'].str.contains(userchoice,case=False)]
    def get_album(self,userchoice): #method to retrieve albums based on user choice.        
        self.album = pd.DataFrame(self.dataframe.name)              
        return self.album[self.album['name'].str.contains(userchoice,case=False)]
    def get_artists_albums(self,artist_name):#method to retrieve all the albums of an artist  
        artist_name1 = "['" + artist_name + "']" #concatenating "['" and "']" to find exact single aritist                   
        if len(self.dataframe[self.dataframe['artists'] == artist_name1]) >= 1: #use single artist data first for similarites else multi artists  data        
            return self.dataframe[self.dataframe['artists'] == artist_name1].name            
        return self.dataframe[self.dataframe['artists'].str.contains(artist_name)].name
    def get_artist_album(self,artist,userchoice): #method to retrieve albums of a chosen artist based on user choice. 
        self.album = self.get_artists_albums(artist)
        self.album = pd.DataFrame(self.album)                           
        return self.album[self.album['name'].str.contains(userchoice,case=False)]
    def get_all_features_by_music_id(self,music_id): # method to retrieve complete records in a dataframe      
        return self.dataframe[self.dataframe['id'].isin(music_id)]
    def get_required_features_by_music_id(self,music_id,feature):# method retrieve requiered features data based on music id list        
        return self.dataframe[self.dataframe['id'].isin(music_id)][feature]
    def get_vectors_album(self,var1,var2,ftr): # function to get the two vectors of music features 
        #var1 and var2 are the arist/album 1 and 2
        m_id_1 = self.get_music_id_by_album_name(var1[0])
        m_id_2 = self.get_music_id_by_album_name(var2[0])        
        #print(self.get_music_props_by_music_id(m_id_1)) # to cross check music ids belongs to the user choice
        #print(self.get_music_props_by_music_id(m_id_2)) # to cross check music ids belongs to the user choice
        self.vector1 = self.get_required_features_by_music_id( m_id_1,ftr)
        self.vector2= self.get_required_features_by_music_id( m_id_2,ftr)  
        #print(self.vector1,self.vector2)           
        self.vector1.loc['mean']= self.vector1.mean() # calculate the mean of features in case artist have mutliple records
        self.vector2.loc['mean']= self.vector2.mean() # calculate the mean of features in case artist have mutliple records              
        return self.vector1.loc['mean'].values,self.vector2.loc['mean'].values  
    def get_vectors_artist(self,var1,var2,ftr): # function to get the two vectors of music features 
        #var1 and var2 are the arist/album 1 and 2
        m_id_1 = self.get_music_id_by_artist_name(var1[0])
        m_id_2 = self.get_music_id_by_artist_name(var2[0])
        #print(self.get_music_props_by_music_id(m_id_1)) # to cross check music ids belongs to the user choice
        #print(self.get_music_props_by_music_id(m_id_2)) # to cross check music ids belongs to the user choice
        self.vector1 = self.get_required_features_by_music_id( m_id_1,ftr)
        self.vector2 = self.get_required_features_by_music_id( m_id_2,ftr)
        self.vector1.loc['mean']= self.vector1.mean() # calculate the mean of features in case artist have mutliple records
        self.vector2.loc['mean']= self.vector2.mean() # calculate the mean of features in case artist have mutliple records              
        return self.vector1.loc['mean'].values,self.vector2.loc['mean'].values
    def get_top_n_album_rec_vectors(self,album,ftr): # method to retrieve vectors for top n albums of a target album
        if len(self.dataframe[self.dataframe['name'] == album[0]][ftr]) > 1: # in case duplicate records found for a song, just pick the very first song from the results            
            return self.dataframe[self.dataframe['name'] == album[0]][ftr].head(1),self.dataframe[self.dataframe['name'] != album[0]][ftr]     
        return self.dataframe[self.dataframe['name'] == album[0]][ftr],self.dataframe[self.dataframe['name'] != album[0]][ftr]
    def get_top_n_artist_rec_vectors(self,artist,ftr):#method to retrieve vectors for top n artists of a target artist
        artist_name1 = "['" + artist + "']" #concatenating "['" and "']" to find exact single aritist                   
        if len(self.dataframe[self.dataframe['artists'] == artist_name1]) >= 1: #use single artist data first for similarites else multi artists  data        
            return self.dataframe[self.dataframe['artists'] == artist_name1][ftr],self.dataframe[self.dataframe['artists'] != artist_name1][ftr]           
        return self.dataframe[self.dataframe['artists'].str.contains(artist)][ftr],self.dataframe[self.dataframe['artists'].str.contains(artist) == False][ftr]
    def get_top_n_artist_album_rec_vectors(self,artist,album,ftr): # method to retrieve vectors for top n albums of target artist
        artist_name1 = "['" + artist + "']" #concatenating "['" and "']" to find exact single aritist
        if len(self.dataframe[(self.dataframe['artists'] == artist_name1) & (self.dataframe['name'] == album[0])]) >= 1:            
            return self.dataframe[(self.dataframe.artists == artist_name1) & (self.dataframe.name == album[0])][ftr].head(1),self.dataframe[(self.dataframe.artists != artist_name1) & (self.dataframe.name != album[0])][ftr]
        return self.dataframe[(self.dataframe.artists.str.contains(artist)) & (self.dataframe.name == album[0])][ftr].head(1),self.dataframe[(self.dataframe.artists.str.contains(artist) == False) & (self.dataframe.name != album[0])][ftr]
    def get_required_features_by_index(self,indices,ftr): #method to retreive required features of any artist/album by its index 
        return self.dataframe[ftr].loc[indices].values
    
        
        


     

    
          
        
        
    
        

   




