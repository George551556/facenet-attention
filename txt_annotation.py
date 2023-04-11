#------------------------------------------------#
#   进行训练前需要利用这个文件生成cls_train.txt.
#   生成的这个文件中每一行的内容是图片的标签以及这个图片的路径
#------------------------------------------------#
import os

if __name__ == "__main__":
    #---------------------#
    #   训练集所在的路径
    #---------------------#
    datasets_path   = "datasets_masked_people_pairs"  #lkz: datasets

    types_name      = os.listdir(datasets_path)
    types_name      = sorted(types_name)

    list_file = open('cls_train.txt', 'w') #lkz: cls_train.txt
    for cls_id, type_name in enumerate(types_name):
        photos_path = os.path.join(datasets_path, type_name)
        if not os.path.isdir(photos_path):
            continue
        photos_name = os.listdir(photos_path)

        for photo_name in photos_name:
            list_file.write(str(cls_id) + ";" + '%s'%(os.path.join(os.path.abspath(datasets_path), type_name, photo_name)))
            list_file.write('\n')
    list_file.close()
