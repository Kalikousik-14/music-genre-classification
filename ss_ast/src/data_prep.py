import os
import pandas as pd 
import glob
import json 
# import splitfolders

# splitfolders.ratio("../../Data/genres_original", # The location of dataset
#                    output="data", # The output location
#                    seed=42, # The number of seed
#                    ratio=(.7, .2, .1), # The ratio of splited dataset
#                    group_prefix=None, # If your dataset contains more than one file like ".jpg", ".pdf", etc
#                    move=False # If you choose to move, turn this into True
#                    )

genres_dir = 'data'
genres = os.listdir(genres_dir+'/train')
print(genres)

labels = pd.DataFrame({'mid':genres, 'label': genres})
labels.to_csv('labels_csv.csv')

data_val = []
data_split = ['train', 'test', 'val']
for data_type in data_split:
    data_dir_curr = os.path.join(genres_dir, data_type)
    for genre in genres:
        wavs = glob.glob(os.path.join(data_dir_curr, genre)+'/*.wav')
        for wav in wavs:
            wav_dict = {'wav':wav, 'labels':genre}
            data_val.append(wav_dict)

    data_dict = {'data':data_val}
    with open(data_type+".json", "w") as outfile:
        json.dump(data_dict, outfile)