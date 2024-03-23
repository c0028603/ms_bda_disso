import nibabel as nib
#import matplotlib.pyplot as plt
#import matplotlib.image as mpimg
import pandas as pd
import os
import glob
import datetime
import warnings
warnings.filterwarnings("ignore")
class niipreprocess:
    def __init__(self,root): ##,nii_f_path,nii_lm_f_path):
        self.root = root #"C:/Drive/Dissertation/OneDrive_1_23-06-2022/BraTSReg_Training_Data_v2_csv/"
        #self.nii_f_path = filepath #"C:/Drive/Dissertation/nii2csv/BraTSReg_001/BraTSReg_001_01_0106_t1ce.nii.gz"
        #self.nii_lm_f_path = nii_lm_f_path #'C:/Drive/Dissertation/nii2csv/BraTSReg_001/BraTSReg_001_01_0106_landmarks.csv'             
    def get_nii_dir_list(self): #function to retreive nii directory
        self.nii_dir_lst = []
        for root, dirs, files in os.walk(self.root, topdown=False):
            for dir in dirs:
                self.nii_dir_lst.append(dir)
        return self.nii_dir_lst
    def get_nii_filename_list(self,pattern): #function to retrieve nii and landmark files        
        self.nii_fn_list = []     
        for root, directories, files in os.walk(self.root, topdown=False):
            nii_names= [file for file in files if pattern in file]
            for name in nii_names:
                self.nii_fn_list.append(name)
        return self.nii_fn_list
    def get_nii_object(self,nii_f_path): # to get nii object used for header and affine
        self.img_nifti = nib.load(nii_f_path)
        return self.img_nifti
    def get_nii_image_numpy(self,nii_f_path): # to get nii data into a numpy array 
        self.img_nifti =  nib.load(nii_f_path)
        self.nii_np = self.img_nifti.get_fdata()
        return self.nii_np
    def get_landmark_csv_df(self,nii_lm_f_path): # land marks file into df
        self.lm_df = pd.read_csv(nii_lm_f_path)
        #self.lm_df = pd.read_csv(nii_lm_f_path,names=['Landmark','X','Y','Z'] )
        #self.lm_df = self.lm_df.iloc[1:]
        self.lm_df['pY'] = self.lm_df['Y'] + 239
        #self.lm_df['pY'] = self.lm_df['Y'].astype(int) + 239
        #self.lm_df = self.lm_df.columns.str.replace(' ', '')
        #self.lm_df['pY'] = self.lm_df['Y'].astype(int) + 239
        return self.lm_df#.astype(int) files from folder 51 onwards has integers and whitespaces in columns 
    def get_voxel_values_df(self): # voxel values of landmarks 
        self.lm_to_VoxVal_df = self.lm_df
        self.lm_to_VoxVal_df['VoxelValue'] = ""
        for index,row  in self.lm_to_VoxVal_df.iterrows():
            voxel_in_array = self.nii_np[int(row[1]):int(row[1] + 1),int(239 + row[2] ):int(239 + row[2] + 1),int(row[3])]
            self.lm_to_VoxVal_df.at[index,'VoxelValue'] = voxel_in_array[0,0]
        return self.lm_to_VoxVal_df
    def get_nii_csv_no_istumor_df(self,nii_fn,nii_np): # this function is only to generate csv without landmarks mapping
        self.nii_df = pd.DataFrame() 
        for i in range (0,155):
            slice = nii_np[:,:,i] # one slice of nii
            slice_df = pd.DataFrame(slice)
            slice_df_melt = pd.DataFrame(slice_df).reset_index().melt('index') # transpose the x y coordinates into two columns
            slice_df_melt.columns = ['X', 'pY', 'VoxVal']
            slice_df_melt['Z'] = i
            slice_df_melt['NiiFileName'] = nii_fn
            slice_df_melt['Y'] =  slice_df_melt['pY'] - 239
            slice_df_melt = slice_df_melt.drop(slice_df_melt[slice_df_melt.VoxVal == 0].index)
            self.nii_df = self.nii_df.append(slice_df_melt)
        return self.nii_df        
    def get_nii_to_csv_df(self,nii_fn,nii_lm_fn,nii_np): # dont pass empty dataframe nii_df; function to convert nii_numpy into csv
        self.nii_df = pd.DataFrame() 
        for i in range (0,155):
            slice = nii_np[:,:,i] # one slice of nii
            slice_df = pd.DataFrame(slice)
            slice_df_melt = pd.DataFrame(slice_df).reset_index().melt('index') # transpose the x y coordinates into two columns           
            slice_df_melt.columns = ['X', 'pY', 'VoxVal']         
            slice_df_melt['Z'] = i
            slice_df_melt['NiiFileName'] = nii_fn
            slice_df_melt['LandmarksFileName'] = nii_lm_fn
            slice_df_melt = slice_df_melt.drop(slice_df_melt[slice_df_melt.VoxVal == 0].index)           
            #print(slice_df_melt.head)
            self.nii_df = self.nii_df.append(slice_df_melt)            
        return self.nii_df
    def get_nii_csv_istumor_df(self,nii_df,lm_df): # to add the istumor flag to parsed nii file
        merge_df = pd.merge(nii_df[['X','pY','Z']],lm_df[['X','pY','Z']].astype(int),how='left',indicator='istumor') # join nii csv and lm csv to get istumor flag
        nii_df['istumor'] = merge_df['istumor'].values
        return nii_df
    def get_csv_for_model(self,path): # all the nii files including base and follow-up registrations
        self.all_csv_files = glob.glob(os.path.join(path, "*values.csv"))     
        self.col_names = ['X','pY','VoxVal','Z','NiiFileName','istumor']
        self.df_from_each_csv_file = (pd.read_csv(f,usecols = self.col_names ) for f in self.all_csv_files)
        self.csv_df_for_model   = pd.concat(self.df_from_each_csv_file, ignore_index=True)
        return self.csv_df_for_model
    def get_csv_for_model_limit(self,path,limit): # all the nii files including base and follow-up registrations WITH LIMIT
        self.all_csv_files = glob.glob(os.path.join(path, "*values.csv"))    
        self.col_names = ['X','pY','VoxVal','Z','NiiFileName','istumor']
        self.df_from_each_csv_file = (pd.read_csv(f,usecols = self.col_names ) for f in self.all_csv_files[0:limit])
        self.csv_df_for_model   = pd.concat(self.df_from_each_csv_file, ignore_index=True)
        return self.csv_df_for_model
    def get_base_csv_for_model(self,path): #only base nii registrations 
        self.all_csv_files = glob.glob(os.path.join(path, "*.csv"))     
        self.col_names = ['X','pY','VoxVal','Z','NiiFileName','istumor']
        self.df_from_each_csv_file = (pd.read_csv(f,usecols = self.col_names ) for f in self.all_csv_files if "_00_" in f)
        self.base_csv_df_for_model   = pd.concat(self.df_from_each_csv_file, ignore_index=True)
        return self.base_csv_df_for_model
    def get_base_csv_for_model_limit(self,path,limit): #only base nii registrations with limited set
        self.all_csv_files = glob.glob(os.path.join(path, "*.csv"))    
        self.col_names = ['X','pY','VoxVal','Z','NiiFileName','istumor']
        self.df_from_each_csv_file = (pd.read_csv(f,usecols = self.col_names ) for f in self.all_csv_files[0:limit] if "_00_" in f)
        self.base_csv_df_for_model   = pd.concat(self.df_from_each_csv_file, ignore_index=True)
        return self.base_csv_df_for_model
    def get_fl_csv_for_model_limit(self,path,limit): # only follow-up nii registrations with limited set
        self.all_csv_files = glob.glob(os.path.join(path, "*.csv"))     
        self.col_names = ['X','pY','VoxVal','Z','NiiFileName','istumor']
        #print(self.all_csv_files[0:limit])
        self.df_from_each_csv_file = (pd.read_csv(f,usecols = self.col_names ) for f in self.all_csv_files[0:limit] if "_01_" in f)
        self.fl_csv_df_for_model   = pd.concat(self.df_from_each_csv_file, ignore_index=True)
        return self.fl_csv_df_for_model
    def get_fl_csv_for_model(self,path): #only follow-up nii registration 
        self.all_csv_files = glob.glob(os.path.join(path, "*.csv"))     
        self.col_names = ['X','pY','VoxVal','Z','NiiFileName','istumor']
        self.df_from_each_csv_file = (pd.read_csv(f,usecols = self.col_names ) for f in self.all_csv_files if "_01_" in f)
        self.fl_csv_df_for_model   = pd.concat(self.df_from_each_csv_file, ignore_index=True)
        return self.fl_csv_df_for_model
    def get_gray_matter_df_for_model(self,input_csv_path,output_csv_path):
        self.all_csv_files = glob.glob(os.path.join(input_csv_path, "*.csv"))     
        self.df = (pd.read_csv(f) for f in self.all_csv_files)
        self.df1 = self.df.query('istumor == 1')
        xyz_df_v2 = self.df1
        xy_df_v2 = pd.DataFrame()
        xyz_df_v2 = pd.DataFrame()
        for tloc in range(0,len(self.df1)):
            for i in range(1,6):
                xy_n_df = self.df[(self.df['X'].isin([self.df1.X.iloc[tloc]])) & (self.df['pY'].isin([self.df1.pY.iloc[tloc]-i])) & (self.df['Z'].isin([self.df1.Z.iloc[tloc]]))]
                xy_p_df = self.df[(self.df['X'].isin([self.df1.X.iloc[tloc]])) & (self.df['pY'].isin([self.df1.pY.iloc[tloc]+i])) & (self.df['Z'].isin([self.df1.Z.iloc[tloc]]))]
                #print([df1.X.iloc[0]],[df1.pY.iloc[0]-i],[df1.pY.iloc[0]+i])
                xy_df_v2 = pd.concat([xy_df_v2,xy_n_df,xy_p_df])
            for loc in range(0,len(xy_df_v2)):
                for j in range(1,6):
                    #print("the value of j is {}".format(j))
                    xyz_n_df = self.df[(self.df['X'].isin([xy_df_v2.X.iloc[loc]])) & (self.df.pY.isin([xy_df_v2.pY.iloc[loc]])) & (self.df['Z'].isin([xy_df_v2.Z.iloc[loc]-j]))]
                    xyz_p_df = self.df[(self.df['X'].isin([xy_df_v2.X.iloc[loc]])) & (self.df.pY.isin([xy_df_v2.pY.iloc[loc]])) & (self.df['Z'].isin([xy_df_v2.Z.iloc[loc]+j]))]       
                    xyz_df_v2 = pd.concat([xyz_df_v2,xyz_n_df,xyz_p_df])
            #print(xyz_df_v2.Z)
        #print(xy_df_v2.X,xy_df_v2.pY,xy_df_v2.Z)
        #print(df.query('istumor == 1'))
        xyz_df_v2 = pd.concat([xyz_df_v2,self.df1])
        #'C:/Drive/Dissertation/OneDrive_1_23-06-2022/BraTSReg_gray_matter_csv/'
        xyz_df_v2.drop_duplicates().to_csv(output_csv_path + xyz_df_v2.NiiFileName.iloc[0] + '_gray_matter.csv', index=False)
        return 
print(datetime.datetime.now(), 'v11.2')    


