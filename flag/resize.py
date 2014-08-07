from glob import glob
from os.path import splitext
from PIL import Image
imglist = glob("flag-img/*.gif")
print imglist
for imgpath in imglist:
    img = Image.open(imgpath)
    # here i use 44*28 size for the icon
    img.thumbnail((44,28))
    buildpath = imgpath.replace(".gif",".png")
    buildpath = buildpath.replace("flag-img/","flag-icon/")
    img.save(buildpath,"png")

