import argparse
from json_io import JSON2Dict
from draw import DrawDots2D,DrawDots3D
import cv2

parser=argparse.ArgumentParser()
parser.add_argument("json_path",help="Json path",type=str)
parser.add_argument("save_path",help="Img svae path",type=str)
parser.add_argument("-2d","--two_d",help="Dwaring 2d dots mode",action="store_true")
parser.add_argument("-3d","--three_d",help="Dwaring 3d dots mode",action="store_true")
parser.add_argument("-s","--show",help="Show mode(for 3d)",action="store_true")

args=parser.parse_args()
json_path=args.json_path
save_path=args.save_path
twod_bool=args.two_d
threed_bool=args.three_d
show_bool=args.show

if(threed_bool==True or twod_bool==False):draw_type="3d"
else:draw_type="2d"

dots=JSON2Dict(json_path)["dots"]
if(draw_type=="2d"):
    img=DrawDots2D(dots)
    cv2.imwrite(save_path,img)
elif(draw_type=="3d"):
    img=DrawDots3D(dots,show=show_bool)
    cv2.imwrite(save_path,img)