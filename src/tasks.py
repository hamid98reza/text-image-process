import os
import datetime
import cv2 as cv
import settings
from src.workers import Workers



class Tasks:

    def process_english(self,no_num:bool,multi_space:bool,
                         rm_dupl_words:bool,meanless_words:bool,
                         rm_single_char:bool):
        
        wrkrs = Workers()
        with open(settings.EN_FILE, "r") as file:
            txts = file.readlines()
            txts = [txt.strip() for txt in txts]
            txts = [j for j in txts if j != ''] # drop empty strings(lines)
        file.close()
        txtlst = wrkrs.remove_sign_en(txt_list=txts)
        if no_num == True:
            txtlst = wrkrs.remove_num_en(txt_list=txtlst) # in out case we must choose the same 
        if multi_space == False:                            # name(txtlst) to prevent probable code crashes.
            txtlst = wrkrs.remove_multi_spaces(txt_list=txtlst)
        if rm_dupl_words == True:
            txtlst = wrkrs.remove_duplicated_words_preserve_order(txt_list=txtlst)
        if meanless_words == False:
            txtlst = wrkrs.remove_meanningless(txt_list=txtlst)
        if rm_single_char == True:
            txtlst = wrkrs.remove_char_single(txt_lst=txtlst)


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


    def process_farsi(self, 
                      rm_sign_num:bool,
                      rm_dupl:bool,
                      no_multispace:bool):

        wrks = Workers()
        with open(settings.FA_FILE, "r") as fafile:
            texts = fafile.readlines()
            texts = [txt.strip() for txt in texts]
            list_of_texts = [j for j in texts if j != ''] # drop empty lines
        fafile.close()

        if rm_sign_num == True:
            list_of_texts = wrks.remove_sign_num_fa(fa_txt_lst=list_of_texts)      
        if rm_dupl == True:
            list_of_texts = wrks.remove_dupl_fa(fa_txt_lst=list_of_texts)
        if no_multispace == True:
            list_of_texts = wrks.remove_multi_spaces(txt_list=list_of_texts)

        
        with open(os.path.join(settings.FA_OUT_DIR, f"{datetime.datetime.now()}.txt"), "a") as fafil:
            counter = 1
            print(f"total numeber of elements --> {len(list_of_texts)}")
            for eachstring in list_of_texts:
                written = fafil.write(eachstring+"\n")
                if written:
                    print(f"{counter} line written")
                    counter+=1
            fafil.close()
            print(f"\n\n{counter-1} line was written")  # counter-1 since \n is at the end of eachstring
            print("\nresult is available at the last file in   " + settings.FA_OUT_DIR)       




    def denoise_image(self):
        
        img_list = os.listdir(settings.IMAGEDIR)
        for image in img_list:
            path_ = os.path.join(settings.IMAGEDIR,image)
            frame = cv.imread(path_)
            rsz_frame = cv.resize(frame,(640,480))   # you can change dimension it as you desire
            dst = cv.fastNlMeansDenoisingColored(frame,
                                                 None,
                                                 int(settings.THRESH2),
                                                 int(settings.THRESH3),
                                                 int(settings.THRESH4),
                                                 int(settings.THRESH5))
            
            name = f"{datetime.datetime.now()}.jpg"
            cv.imwrite(os.path.join(settings.IMAGE_OUT_DIR, name) ,dst)
        print("Done")    
        print("your result is the last image file at  "+ settings.IMAGE_OUT_DIR)