import glob
import sys
from PIL import Image


def relation(x,y):
    return x/y if x<y else y/x


if __name__ == '__main__':
    
    print("Start")
    
    # recursive level
    if sys.argv[1]:
        try:
            deeplevel = int(sys.argv[1])
        except: 
            print("Parameter is not an INT")
            sys.exit(0)
    else: 
        print("Parameter is missing")
        sys.exit(0)
             
    # path to my folder
    if sys.argv[2]:
        try:
            if sys.argv[2][-1:] != "\\":
                myfolder= sys.argv[2] + "\\"
            else:
                myfolder= sys.argv[2]
        except:
            print(print("Parameter is not an INT"))
            sys.exit(0)
    else: 
        print("Parameter is missing")        
        sys.exit(0)
    
    # Image file formats to resize 
    file_formats=("*.jpg","*.png")
    
    # Max Sum of pixels 
    max_size_px = 5120
    # bigest side 
    new_size_px = 3072
    
    
    # make the the recursive folder chain
    kette = '*\\'
    folders = [myfolder]
    for x in range(deeplevel):
        for i in range(x):
            kette = kette + "*\\"
        folders.append((folders[0] + kette))
    
    
    
    for single_folder in folders:   
        for ends in file_formats:
            path = single_folder + ends
            try:
                ary_images = glob.iglob(path)
                
                for single_img in ary_images:
                    print(single_img)
                    img = Image.open(single_img)
                    
                    x, y = img.size
                    
                    # resize the img if the sum of px's higher the max_size_px  
                    if  (x + y) > max_size_px: 
                        if x != new_size_px and y != new_size_px:
                            
                            re = relation(x,y)     
                            
                            if re < 0.49:
                                print(img.size,re, "Panorama Exlude")
                                continue 
                            else:
                                print(img.size,re, "RESIZE")
                                    
                                cal_size = int(new_size_px * re)
                                    
                                if x > y:
                                    img = img.resize((new_size_px, cal_size), Image.ANTIALIAS)
                                else: 
                                    img = img.resize((cal_size, new_size_px), Image.ANTIALIAS)
                                                         
                                img.save(single_img)  
    
            except Exception as e: 
                print(str(e))
    
    print("END")
