from imagehandler import ImageHandler

#paste you folder path 
dir = r"C:\Users\m_wol\OneDrive\Pulpit\pics"

imghandler = ImageHandler(dir)


imghandler.get_images()

##place for modification functions
imghandler.size_reduce()

##saving images, as copy add prefix etc.
imghandler.save_reduced_image(as_copy = False, quality=40)

#imghandler.image_resize()

##run this to rename in order, possibly add date
# imghandler.image_rename(name= "IMG", add_date_year=True)