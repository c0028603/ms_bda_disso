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
    print("select your fav feature from the below options to compare")
    print("1. acousticness 2. danceability 3. energy 4. liveness 5. loudness 6. popularity 7. speechiness 8.tempo 9. valence")
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
    print("lets select the multiple (three) features to compare from the below")
    print("1. acousticness; 2. danceability; 3. energy; 4. liveness; 5. loudness; 6. popularity; 7. speechiness; 8.tempo and 9. valence")
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
    print("1. acousticness; 2. danceability; 3. energy; 4. liveness; 5. loudness; 6. popularity; 7. speechiness; 8.tempo and 9. valence\n")
    print("you can choose either of any one, any three or all features to compare")
    #print("select your option")
    print("1. One Feature 2. Multiple(Three) Features 3. All")
    a = no_of_features()
    if a == 1:        
        feature_choice = [one_feat_sel_func()] # funtion returns a numeric. converted into list so that it will be iterable
    elif a == 2:
        feature_choice = multi_feat_sel_func()
    elif a == 3:
        feature_choice = (1,2,3,4,5,6,7,8,9)
    key = [1,2,3,4,5,6,7,8,9]
    val = ['acousticness','danceability','energy','liveness','loudness','popularity','speechiness','tempo','valence'] 
    feat = dict(zip(key,val))
    features_selected = [feat[i] for i in feature_choice ]
    return features_selected
def album_sel_func(obj,choice):
    while True:    
        print("Enter ",choice,"album name:")
        usr_choice = input("")
        usr_choice_search_res = obj.get_album(usr_choice)     
        if len(usr_choice_search_res) == 0:
            print("apologies! the album was not found")
            continue
        elif len(usr_choice_search_res[usr_choice_search_res['name'] == usr_choice]) >= 1 and usr_choice_search_res[usr_choice_search_res['name'] == usr_choice].values[0] == usr_choice:
            usr_choice_search_res['name'].values[0] = usr_choice_search_res[usr_choice_search_res['name'] == usr_choice].values[0]
            print(usr_choice_search_res['name'].values[0]," is confirmed")
            break
        elif len(usr_choice_search_res) == 1 and usr_choice_search_res['name'].values[0] == usr_choice:       
                print(usr_choice_search_res['name'].values[0]," is confirmed")
                break
        elif len(usr_choice_search_res) == 1 and usr_choice_search_res['name'].values[0] != usr_choice:
            print("we have found the below match.would you like to use this?y/n: ")
            print(usr_choice_search_res['name'].values[0])
            artist_confirmation = input("")
            if artist_confirmation in ['y','Y']: 
                print(usr_choice_search_res['name'].values[0]," is confirmed")
                return usr_choice_search_res.values[0]                  
                break
            elif artist_confirmation in ['n','N']:
                print("fine! lets restart")
                continue
            else:
                print("wrong input.lets restart")
                continue
        elif len(usr_choice_search_res) >= 1 and len(usr_choice_search_res) <=20:
            print("we have the below matches of ",usr_choice,"Select an appropriate one")
            for index, row in usr_choice_search_res.iterrows():
                print(row['name'])
            continue
        elif len(usr_choice_search_res) >= 20:
            print("too many results of ",usr_choice,". please  refine the text and enter")
            continue
        else:
            print("no album found")
            continue
    return  usr_choice_search_res['name'].values[0]
def artist_sel_func(obj,choice):
    while True:
        print("Enter ",choice,"artist name:")
        usr_choice = input("")
        usr_choice_search_res = obj.get_artist(usr_choice)     
        if len(usr_choice_search_res) == 0:
            print("apologies! the artist was not found")
            continue
        elif len(usr_choice_search_res[usr_choice_search_res['artist'] == usr_choice]) >= 1 and usr_choice_search_res[usr_choice_search_res['artist'] == usr_choice].values[0] == usr_choice:
            usr_choice_search_res['artist'].values[0] = usr_choice_search_res[usr_choice_search_res['artist'] == usr_choice].values[0]
            print(usr_choice_search_res['artist'].values[0]," is confirmed")
            break
        elif len(usr_choice_search_res) == 1 and usr_choice_search_res['artist'].values[0] == usr_choice:       
                print(usr_choice_search_res['artist'].values[0]," is confirmed")
                break
        elif len(usr_choice_search_res) == 1 and usr_choice_search_res['artist'].values[0] != usr_choice:            
            print("we have found the below match.would you like to use this?y/n: ")
            print(usr_choice_search_res['artist'].values[0])
            artist_confirmation = input("")
            if artist_confirmation in ['y','Y']: 
                print(usr_choice_search_res.values[0]," is confirmed")
                return usr_choice_search_res.values[0]                     
                break
            elif artist_confirmation in ['n','N']:
                print("fine! lets restart")
                continue
            else:
                print("wrong input.lets restart")
                continue
        elif len(usr_choice_search_res) >= 1 and len(usr_choice_search_res) <=20:
            print("we have the below matches of ",usr_choice,"Select an appropriate one")
            for index, row in usr_choice_search_res.iterrows():
                print(row['artist'])
                continue
        elif len(usr_choice_search_res) >= 20:
            print("too many results of ",usr_choice,". please  refine the text and enter")
            continue
        else:
            print("no artist found")
            continue
    return  usr_choice_search_res['artist'].values[0]
def artists_album_sel_func(obj,artist,choice):
    print("Enter ",choice)      
    albums = obj.get_artists_albums(artist[0])
    print("we have",len(albums), " songs of",artist, " and here are few...\n")        
    for ind in albums.head(5).index:
        print(albums.head(5)[ind])
    while True:                        
        usr_choice = input("enter either the song or a keyword:")
        usr_choice_search_res = obj.get_artist_album(artist[0],usr_choice)     
        if len(usr_choice_search_res) == 0:
            print("apologies! the album was not found")
            continue
        elif len(usr_choice_search_res[usr_choice_search_res['name'] == usr_choice]) >= 1 and usr_choice_search_res[usr_choice_search_res['name'] == usr_choice].values[0] == usr_choice:
            usr_choice_search_res['name'].values[0] = usr_choice_search_res[usr_choice_search_res['name'] == usr_choice].values[0]
            print(usr_choice_search_res['name'].values[0]," is confirmed")
            break
        elif len(usr_choice_search_res) == 1 and usr_choice_search_res['name'].values[0] == usr_choice:       
                print(usr_choice_search_res['name'].values[0]," is confirmed")
                break
        elif len(usr_choice_search_res) == 1 and usr_choice_search_res['name'].values[0] != usr_choice:
            print("we have found the below match.would you like to use this?y/n: ")
            print(usr_choice_search_res['name'].values[0])
            artist_confirmation = input("")
            if artist_confirmation in ['y','Y']: 
                print(usr_choice_search_res['name'].values[0]," is confirmed")
                return usr_choice_search_res.values[0]                  
                break
            elif artist_confirmation in ['n','N']:
                print("fine! lets restart")
                continue
            else:
                print("wrong input.lets restart")
                continue
        elif len(usr_choice_search_res) >= 1 and len(usr_choice_search_res) <=20:
            print("we have the below matches of ",usr_choice,"Select an appropriate one")
            for index, row in usr_choice_search_res.iterrows():
                print(row['name'])
            continue
        elif len(usr_choice_search_res) >= 20:
            print("too many results of ",usr_choice,". please  refine the text and enter")
            continue
        else:
            print("no album found")
            continue
    return  usr_choice_search_res['name'].values[0]
def user_options_func():   
    print("1. two artists comparision \n2. two albums  comparision ")
    print("3. similar artists to your fav artist \n4. similar albums to your fav album")    
    print("5. similar albums to your fav artist's album \n6. Exit")
def resuts_plot(df,plt,tgt):
    fig, axes = plt.subplots(nrows=3, ncols=2 ,figsize=(20,40))
    fig.suptitle(tgt, fontsize=40,color = 'blue')
    axes[0,1].yaxis.tick_right();axes[1,1].yaxis.tick_right()
    for axis,frame in zip(axes.flat,df):
        if frame.columns[1] == 'accuracy score in %':
            cols = frame.columns.tolist()            
            #axis.set_xlabel(,fontsize = 30,fontweight = 'bold')
            axis.xaxis.set_tick_params(labelsize=30,labelrotation=45)
            axis.yaxis.set_tick_params(labelsize=30)            
            #axis.barh(frame[cols[0]],frame[cols[1]],color = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'])
            axis.bar(frame[cols[0]],frame[cols[1]],color = ['#e7969c','#7b4173','#a55194','#ce6dbd','#de9ed6'])
            axis.set_title("Metric Accuracy Score(method:NN)",color = 'blue',fontsize=30,fontweight = 'bold')
            axis.set_ylabel("accuracy score",fontsize = 30,fontweight = 'bold')
            axis.yaxis.set_label_position("right")      
        else:     
            cols = frame.columns.tolist()            
            axis.set_xlabel(frame.columns[1]+" distance",fontsize = 30,fontweight = 'bold')
            axis.xaxis.set_tick_params(labelsize=30)
            axis.yaxis.set_tick_params(labelsize=30)
            #axis.barh(frame[cols[0]],frame[cols[1]],color = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf'])
            axis.barh(frame[cols[0]],frame[cols[1]],color = ['#00ffff',	'#0df2ff',	'#1be4ff',	'#28d7ff',	'#36c9ff',	'#43bcff',	'#51aeff',	'#5ea1ff',	'#6b94ff',	'#7986ff',	'#8679ff',	'#946bff',	'#a15eff',	'#ae51ff',	'#bc43ff',	'#c936ff',	'#d728ff',	'#e41bff',	'#f20dff',	'#ff00ff'])      
    plt.subplots_adjust(top=0.96)
    plt.show()
    


    
                                     
    