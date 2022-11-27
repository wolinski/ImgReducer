# ImgReducer

## Introduction

ImgReducer is a simple script which allows to reduce size, rename, resize multiple pictures in given directory.
Script is based on Pillow library by Alex Clark and Contributors https://github.com/python-pillow/Pillow

## Features
- Reduce size
- Rename file with copy, prefix, suffix, numeration, today date
- Reduce size to given value
- Rotate


## Examples
### Reduce size of images
```
from imagehandler import ImageHandler

#paste you folder path 
dir = r"C:\Users\m_wol\OneDrive\Pulpit\pics"

imghandler = ImageHandler(dir)
imghandler.get_images()

#place for modification functions
imghandler.size_reduce()

#saving reduced images, as copy add prefix etc.
imghandler.save_reduced_image(as_copy = False, quality=80)
```
### Rename images

```
from imagehandler import ImageHandler

#paste you folder path 
dir = r"C:\Users\m_wol\OneDrive\Pulpit\pics"

imghandler = ImageHandler(dir)
imghandler.get_images()

#run this to rename in order, possibly add date
imghandler.image_rename(name="IMG", start_from=0, add_date_year=False)
```
### Resize images
```
from imagehandler import ImageHandler

#paste you folder path 
dir = r"C:\Users\m_wol\OneDrive\Pulpit\pics"

imghandler = ImageHandler(dir)
imghandler.get_images()

#resizing images to given size, but keeping the ratio
imghandler.image_resize(size=(1920,1080), as_copy=True)
```