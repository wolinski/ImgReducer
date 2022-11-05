import os
import glob
from PIL import Image

# Skrypt powinien mieć możliwość zapisywania pod inną nazwą z numeracją lub możliwość zapisywania pod starą nazwą w nowym folderze, w formacie png lub jpeg.
# Docelowo stworzyc gui z inputem original path -> destination path, picture size, antialias y/n, format png/jpg
# Docelowo wybór zdjęć w gui powinien się odbywać na zasadzie zbioru wybranych zdjęć, nie z zawartości 

#funkcje do zaimplementowania
#[x]redukcja wagi z nadpisaniem pod tą samą nazwą
#[x]jak wyżej, ale z kopią
#[x]możliwość zapisania pod formatem .png
#[x]możliwość dodania prefixu/suffixu z zachowaniem starej nazwy
#[]możliwość dodania prefixu/suffixu ze zmianą nazwy
#[]możliwość zmiany rozdzielczości/wymiarów zdjecia
#[]możliwość podania samej ścieżki bez koniecznośći podawania rozszerzenia i czy sa tam tylko zdjecia, ma rozpoznac sam
#[]możliwość dodania rotate


dir = r"C:\Users\m_wol\OneDrive\Pulpit\pics\*.jpg"

class ImageHandler:
    def __init__(self, path) -> None:
        self.path = path
        self.resized_img_dict = {}
        self.imgsize = {}
        self.imgmode = {}
        self.imagelist = []
        pass

    def get_images(self): #przerobic tak zeby rozpoznawalo pliki ze zdjeciami, nawyzej trzeba podac liste formatow
        for file in glob.glob(self.path):
            img = Image.open(file)
            self.image_list.append(img)
    
    def size_reduce(self, optimized = True, quality=60):
        for img in self.image_list:
            resized_img = img.resize(img.size, Image.Resampling.LANCZOS)
            self.resized_img_dict[resized_img.tobytes()] = img.filename
            self.imgsize[img.filename] = img.size
            self.imgmode[img.filename] = img.mode


    def save_image(self, as_copy = True, prefix="", suffix="", optimized = True, quality=60, format = "jpg"):
        for img, name in self.resized_img_dict.items():
            if as_copy:
                if suffix == "":
                    suffix = "-Copy"
            img_name = prefix + os.path.splitext(name)[0] + suffix + '.' + format

            image = Image.frombytes(mode= self.imgmode[name], data = img, size=self.imgsize[name],)
            #image = Image.open(io.BytesIO(img))
            image.save(img_name, optimize=optimized, quality=quality)

    def image_rename(self, new_name = "Image"):
        pass

    def image_resize(self):
        pass

    def image_rotate(self):
        pass


imghandler = ImageHandler(dir)
imghandler.size_reduce()
imghandler.save_image(as_copy = False)
