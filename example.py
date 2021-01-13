from json_io import JSON2Dict,Dict2JSON
from draw import DrawDots2D,DrawDots3D
import cv2

# ch_dataset
ch_dataset_dir="example_dataset"

# en_dataset
en_dataset_dir="example_dataset"

# Get all you need
label="ymz"
data_type="3d"
pstvorngtv="pstv"
file_idx=0

json_path=ch_dataset_dir+"/"+label+"/"+data_type+"/"+pstvorngtv+"/"+str(file_idx)+".json"
dots=JSON2Dict(json_path)["dots"] # tracking

# Drawing 2d
# img_2d=DrawDots2D(dots)
# cv2.imwrite("2d.jpg",img_2d)


# Drawing 3d (not show controller)
img_3d=DrawDots3D(dots,show=False) # not show controller
cv2.imwrite("3d.jpg",img_3d)
# img_3d=DrawDots3D(dots,show=True) # show controller


