import os
import pandas as pd
import numpy as np
import datetime
import cv2 as cv
import settings
from src.workers import Workers



class Tasks:

    def process_english(self,no_num:bool,multi_space:bool,
                         rm_dupl_words:bool,meanless_words:bool,
                         rm_single_char:bool):
        
        with open(settings.EN_FILE, "r") as file:
            txts = file.readlines()
            txts = [txt.strip() for txt in txts]
            txts = [j for j in txts if j != ''] # drop empty strings(lines)
        file.close()
        txtlst = Workers().remove_sign_en(txt_list=txts)
        if no_num == True:
            txtlst = Workers().remove_num_en(txt_list=txtlst) # in out case we must choose the same 
        if multi_space == False:                            # name(txtlst) to prevent probable code crashes.
            txtlst = Workers().remove_multi_spaces(txt_list=txtlst)
        if rm_dupl_words == True:
            txtlst = Workers().remove_duplicated_words_preserve_order(txt_list=txtlst)
        if meanless_words == False:
            txtlst = Workers().remove_meanningless(txt_list=txtlst)
        if rm_single_char == True:
            txtlst = Workers().remove_char_single(txt_lst=txtlst)


        with open(os.path.join(settings.EN_OUT_DIR, f"{datetime.datetime.now()}.txt"), "a") as f:
            counter = 1
            print(f"total numeber of elements --> {len(txtlst)}")
            for eachstring in txtlst:
                written = f.write(eachstring+"\n")
                if written:
                    print(f"{counter} line written")
                    counter+=1
            f.close()
            print(f" {counter-1} line written")  # counter-1 since \n is at the end of eachstring
            print("\nresult is available at the last file in   " + settings.EN_OUT_DIR)


    def process_farsi(self):
        pass

    def denoise_image(self):
        pass
