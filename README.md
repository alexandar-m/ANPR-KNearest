# ANPR Automatic number-plate recognition with Python and KNearest 
ANPR KNearest creates jpeg img's from TTF font, trains and recognizes licence plates after cleaning and separating chars


### EXTRACT TTF FONT CHAR TO JPG
create font - single folder.py
>Extract jpg img's from TTF font chars 0-9 and A-Z in dataset-single folder


create font - subfolders.py
>Extract jpg img's from TTF font in dataset folder and subfolders named 0-9 and A-Z with font name on every img as font/0/0-arial.jpg etc


### EXTRACTED JPG CHAR TRAINING
>training single font
* training font in subfolders have issues with result accuracy

<p align="center">   
  <img src="/demo/chars.jpg">
</p>

### LICENCE PLATE RECOGNIZE
recognize.py
* reads JPG img
* cleans img (results in temp folder)
* extracts chars (results in plate-contours folder)
* KNearest return values of nearest dists and shows result

<p align="center">   
  <img src="/demo/demo.jpg">
</p>

<p align="center">   
  <img src="/demo/ocr.jpg">
</p>

Need asistance to finish "training - font in subfolders.py"
