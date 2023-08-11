import numpy as np
import pandas as pd
import pickle
import json

class Penguine():
    def __init__ (self,bill_length_mm,bill_depth_mm,flipper_length_mm,body_mass_g,species,island):
    

        self.bill_length_mm=bill_length_mm
        self.bill_depth_mm=bill_depth_mm
        self.flipper_length_mm=flipper_length_mm
        self.body_mass_g=body_mass_g
        self.species="species_"+species 
        self.island="island_"+island

    def load_data(self):
        with open("model.pkl","rb") as k:
            self.model = pickle.load(k)

        with open("pred_data.json","r") as l:
            self.data = json.load(l)
    def Pred_Penguine(self):
        self.load_data()

        species_index=self.data['col_names'].index(self.species)
        island_index=self.data['col_names'].index(self.island)
        array=np.zeros([1,10])
        array[0][0]=self.bill_length_mm
        array[0][1]=self.bill_depth_mm
        array[0][2]=self.flipper_length_mm
        array[0][3]=self.body_mass_g
        array[0,species_index]=1
        array[0,island_index]=1

       
        pred= self.model.predict(array)[0]
        return pred
