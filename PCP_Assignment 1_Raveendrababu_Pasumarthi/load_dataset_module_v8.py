import re
music_file_raw = open("data.csv",'r',encoding="utf8")
lines = music_file_raw.readlines()
#print("no.of rows:",len(lines)-1)
def artist_music_dict():
    artist_music = {}
    i=0
    for line in lines:
        #line = next(music_file_raw).strip()
        line = str(line)
        #..........find the comma position...............
        indices = re.finditer(',',line)
        index_list = [index.start() for index in indices]
        #............... find the artist comma position..............
        artist_start_pos = line.find('[')
        artist_end_pos = line.find(']')
        artist_indices = re.finditer(',',line[artist_start_pos:artist_end_pos+1])
        artist_index_list = [index.start() for index in artist_indices]
        if len(index_list) == 18:
            artist_music[i] = {  'id' : line[index_list[5]+1:index_list[6]]
                                ,'artist(s)' : line[index_list[0]+2:index_list[1]-1]
                                ,'name' : line[index_list[11]+1:index_list[12]]
                                ,'duration_ms' : line[index_list[2]+1:index_list[3]]
                                ,'release_date' : line[index_list[13]+1:index_list[14]]
                                ,'year' : line[index_list[17]+1:len(line)]}
        elif len(index_list) > 18 and len(artist_index_list) >=1 and len(index_list) == 18 + len(artist_index_list):
            artist_music[i] = { 'id' : line[index_list[5+len(artist_index_list)]+1:index_list[6+len(artist_index_list)]] 
                                                                                                                ,'artist(s)' : line[index_list[0]+3:artist_end_pos]
                                                                                                                ,'name' : line[index_list[11+len(artist_index_list)]+1:index_list[12+len(artist_index_list)]]
                                                                                                                ,'duration_ms' : line[index_list[2+len(artist_index_list)]+1:index_list[3+len(artist_index_list)]]
                                                                                                                ,'release_date' : line[index_list[13+len(artist_index_list)]+1:index_list[14+len(artist_index_list)]]
                                                                                                                ,'year' : line[index_list[17+len(artist_index_list)]+1:len(line)]}
        elif len(index_list) > 18 and len(artist_index_list) >=1 and len(index_list) > 18 + len(artist_index_list):
            artist_music[i] = { 'id': line[index_list[5+len(artist_index_list)]+1:index_list[6+len(artist_index_list)]]
                ,'artist(s)' : line[index_list[0]+3:artist_end_pos]
                                                                                                                ,'name' : line[index_list[11+len(artist_index_list)]+1:index_list[len(index_list)-6]]
                                                                                                                ,'duration_ms' : line[index_list[2+len(artist_index_list)]+1:index_list[3+len(artist_index_list)]]
                                                                                                                ,'release_date' : line[index_list[len(index_list)-5]+1:index_list[len(index_list)-4]]
                                                                                                                ,'year' : line[index_list[len(index_list)-1]+1:len(line)]}
        else:
            artist_music[i] = { 'id' : line[index_list[5]+1:index_list[6]]
                                                                  ,'artist(s)' : line[index_list[0]+3:index_list[1]]
                                                                  ,'name' : line[index_list[11]+1:index_list[len(index_list)-6]]
                                                                  ,'duration_ms' : line[index_list[2]+1:index_list[3]]
                                                                  ,'release_date' : line[index_list[len(index_list)-5]+1:index_list[len(index_list)-4]]
                                                                  ,'year' : line[index_list[len(index_list)-1]+1:len(line)]}
        i = i+1
    return artist_music
def music_features_dict():
    music_features = {}
    j=0
    for line in lines:
        #line = next(music_file_raw).strip()
        line = str(line)
        #..........find the delemiter comma position...............
        indices = re.finditer(',',line)
        index_list = [index.start() for index in indices]
        #............... find the artist comma position..............
        artist_start_pos = line.find('[')
        artist_end_pos = line.find(']')
        artist_indices = re.finditer(',',line[artist_start_pos:artist_end_pos+1])
        artist_index_list = [index.start() for index in artist_indices]
        if len(index_list) == 18:
            music_features[j] = { 'id' : line[index_list[5]+1:index_list[6]]
                                                                   ,'acousticness' : line[0:index_list[0]]
                                                                  ,'danceability' : line[index_list[1]+1:index_list[2]]
                                                                  ,'energy' : line[index_list[3]+1:index_list[4]]
                                                                  ,'explicit' : line[index_list[4]+1:index_list[5]]
                                                                  ,'instrumentalness' : line[index_list[6]+1:index_list[7]] 
                                                                  ,'key' : line[index_list[7]+1:index_list[8]]
                                                                  ,'liveness' : line[index_list[8]+1:index_list[9]]
                                                                  ,'loudness' : line[index_list[9]+1:index_list[10]]
                                                                  ,'mode' : line[index_list[10]+1:index_list[11]]
                                                                  ,'popularity' : line[index_list[12]+1:index_list[13]]
                                                                  ,'speechiness' : line[index_list[14]+1:index_list[15]]
                                                                  ,'tempo' : line[index_list[15]+1:index_list[16]]
                                                                  ,'valence' : line[index_list[16]+1:index_list[17]] }
        elif len(index_list) > 18 and len(artist_index_list) >=1 and len(index_list) == 18 + len(artist_index_list):
            music_features[j] = { 'id':  line[index_list[5+len(artist_index_list)]+1:index_list[6+len(artist_index_list)]]
                                                                                                                ,'acousticness' : line[0:index_list[0]]
                                                                                                                ,'danceability' : line[artist_end_pos+3:index_list[2+len(artist_index_list)]]
                                                                                                                ,'energy' : line[index_list[3+len(artist_index_list)]+1:index_list[4+len(artist_index_list)]]
                                                                                                                ,'explicit' : line[index_list[4+len(artist_index_list)]+1:index_list[5+len(artist_index_list)]]
                                                                                                                ,'instrumentalness' : line[index_list[6+len(artist_index_list)]+1:index_list[7+len(artist_index_list)]]
                                                                                                                ,'key' : line[index_list[7+len(artist_index_list)]+1:index_list[8+len(artist_index_list)]]
                                                                                                                ,'liveness' : line[index_list[8+len(artist_index_list)]+1:index_list[9+len(artist_index_list)]]
                                                                                                                ,'loudness' : line[index_list[9+len(artist_index_list)]+1:index_list[10+len(artist_index_list)]]
                                                                                                                ,'mode' : line[index_list[10+len(artist_index_list)]+1:index_list[11+len(artist_index_list)]]
                                                                                                                ,'popularity' : line[index_list[12+len(artist_index_list)]+1:index_list[13+len(artist_index_list)]]
                                                                                                                ,'speechiness' : line[index_list[14+len(artist_index_list)]+1:index_list[15+len(artist_index_list)]]
                                                                                                                ,'tempo' : line[index_list[15+len(artist_index_list)]+1:index_list[16+len(artist_index_list)]]
                                                                                                                ,'valence' : line[index_list[16+len(artist_index_list)]+1:index_list[17+len(artist_index_list)]] }
        elif len(index_list) > 18 and len(artist_index_list) >=1 and len(index_list) > 18 + len(artist_index_list):
            music_features[j] = { 'id': line[index_list[5+len(artist_index_list)]+1:index_list[6+len(artist_index_list)]]
                                                                                                                ,'acousticness' : line[0:index_list[0]]
                                                                                                                ,'danceability' : line[artist_end_pos+3:index_list[2+len(artist_index_list)]]
                                                                                                                ,'energy' : line[index_list[3+len(artist_index_list)]+1:index_list[4+len(artist_index_list)]]
                                                                                                                ,'explicit' : line[index_list[4+len(artist_index_list)]+1:index_list[5+len(artist_index_list)]]
                                                                                                                ,'instrumentalness' : line[index_list[6+len(artist_index_list)]+1:index_list[7+len(artist_index_list)]]
                                                                                                                ,'key' : line[index_list[7+len(artist_index_list)]+1:index_list[8+len(artist_index_list)]]
                                                                                                                ,'liveness' : line[index_list[8+len(artist_index_list)]+1:index_list[9+len(artist_index_list)]]
                                                                                                                ,'loudness' : line[index_list[9+len(artist_index_list)]+1:index_list[10+len(artist_index_list)]]
                                                                                                                ,'mode' : line[index_list[10+len(artist_index_list)]+1:index_list[11+len(artist_index_list)]]
                                                                                                                ,'popularity' : line[index_list[len(index_list)-6]+1:index_list[len(index_list)-5]]
                                                                                                                ,'speechiness' : line[index_list[len(index_list)-4]+1:index_list[len(index_list)-3]]
                                                                                                                ,'tempo' : line[index_list[len(index_list)-3]+1:index_list[len(index_list)-2]]
                                                                                                                ,'valence' : line[index_list[len(index_list)-2]+1:index_list[len(index_list)-1]] }
        else:
            music_features[j] = { 'id': line[index_list[5]+1:index_list[6]]
                                                                  ,'acousticness' : line[0:index_list[0]]
                                                                  ,'danceability' : line[index_list[1]+1:index_list[2]]
                                                                  ,'energy' : line[index_list[3]+1:index_list[4]]
                                                                  ,'explicit' : line[index_list[4]+1:index_list[5]]
                                                                  ,'instrumentalness' : line[index_list[6]+1:index_list[7]]
                                                                  ,'key' : line[index_list[7]+1:index_list[8]]
                                                                  ,'liveness' : line[index_list[8]+1:index_list[9]]
                                                                  ,'loudness' : line[index_list[9]+1:index_list[10]]
                                                                  ,'mode' : line[index_list[10]+1:index_list[11]]
                                                                  ,'popularity' : line[index_list[len(index_list)-6]+1:index_list[len(index_list)-5]]
                                                                  ,'speechiness' : line[index_list[len(index_list)-4]+1:index_list[len(index_list)-3]]
                                                                  ,'tempo' : line[index_list[len(index_list)-3]+1:index_list[len(index_list)-2]]
                                                                  ,'valence' : line[index_list[len(index_list)-2]+1:index_list[len(index_list)-1]] }
        j = j+1
    return music_features
def flattenartists(lis): # function to flatten artist data
    comma = ","
    slash = "/"
    artist__ = []
    for i in lis:
        if comma in i: # mutliple artists in a song 
            multi_artist = i.split(",") # split multiple artists 
            for single_artist in multi_artist: 
                if slash in single_artist: # some artist names are with a slash , so check for that condiction
                    slash_artists = single_artist.split("/") 
                    for slash_artist in slash_artists:
                        artist__.append(slash_artist) #artist name  from multiple artists of an album that are separated by slash  
                else:
                    artist__.append(single_artist) # artist name  from multiple artists of an album
        else:
            artist__.append(i) # artist name from album 
    cleansed_artist__ = [cleansed_artist.strip('[]') for cleansed_artist in artist__] #cleansing unwated characters like " [ ", and " ] "
    cleansed_artist__ = [cleansed_artist.strip("'") for cleansed_artist in cleansed_artist__] #cleansing unwated single quote after dedup
    cleansed_artist__ = [cleansed_artist.replace(" '",'') for cleansed_artist in cleansed_artist__] #cleansing unwated substring" '" after dedup
    dedup_artist__ = list(dict.fromkeys(cleansed_artist__))#duplicate artist removed 
    return dedup_artist__ #return distinct artists
def no_of_features():
    while True:
        try:               
            no_of_features = int(input("select your option: "))                        
            if no_of_features not in range(1,4):
                print("Not an appropriate choice.")
                continue
            else:
                break
        except ValueError:
                print("Text/decimal Not an appropriate choice.")
    return no_of_features
def one_feat_sel_func():
    print("select your fav feature from the above options to compare")
    #print("1. acousticness 2. danceability 3. energy 4. liveness 5. loudness 6. popularitiy 7. speechiness 8.tempo 9. valence")
    while True:        
        try:
            music_feature = int(input("select a feature  from the above list: "))
            if music_feature not in range(1,10):
                print("Not an appropriate choice.")
                continue
            else:
                break
        except ValueError:
            print("Text/decimal Not an appropriate choice.")
    return music_feature
def multi_feat_sel_func():    
    print("lets select the multiple (three) features to compare")
    #print("1. acousticness; 2. danceability; 3. energy; 4. liveness; 5. loudness; 6. popularitiy; 7. speechiness; 8.tempo and 9. valence")
    while True:
        try:
            music_feature_1 = int(input("select feature 1 from the above list: "))
            if music_feature_1 not in range(1,10):
                print("Not an appropriate choice.")
                continue
            else:            
                while True:
                    try:
                        music_feature_2 = int(input("select feature 2 from the above list: "))
                        if music_feature_2 == music_feature_1:                            
                            print("you chose same feature twice, select a different feature")
                            continue
                        elif  music_feature_2 not in range(1,10):
                            print("Not an appropriate choice.")
                            continue
                        while True:
                            try:
                                music_feature_3 = int(input("select feature 3 from the above list: "))
                                if music_feature_3 == music_feature_1 or music_feature_3 == music_feature_2:                            
                                   print("you chose same feature twice, select a different feature")
                                   continue
                                elif  music_feature_3 not in range(1,10):
                                      print("Not an appropriate choice.")
                                      continue
                                else:
                                      break
                            except ValueError:
                                print("Text/decimal Not an appropriate choice.")
                        break                        
                    except ValueError:
                        print("Text/decimal Not an appropriate choice.")
                break               
        except ValueError:
            print("Text/decimal Not an appropriate choice.")
    return music_feature_1,music_feature_2,music_feature_3
def allfeatfunc():    
    print("\n\nNow lets select the features to compare")
    print("we have the below features for the comparision")
    print("1. acousticness; 2. danceability; 3. energy; 4. liveness; 5. loudness; 6. popularitiy; 7. speechiness; 8.tempo and 9. valence")
    print("you can choose either of any one, any three or all features to compare")
    #print("select your option")
    print("1. One Feature 2. Multiple(Three) Features 3. All")
    a = no_of_features()
    if a == 1:        
        feature_choice = one_feat_sel_func()
    elif a == 2:
        feature_choice = multi_feat_sel_func()
    elif a == 3:
        feature_choice = (1,2,3,4,5,6,7,8,9)
    return feature_choice 
music_file_raw.close()