# ANPR-KNearest
ANPR KNearest create img's from TTF font, train and recognize licence plate


##TTF TO JPEG
create font - single folder.py
(Creates jpeg's from TTF font chars 0-9 and A-Z in single folder as font-eu/0.jpg)


create font - subfolderes.py
(Creates jpeg's from TTF font in subfolders named  0-9 and A-Z with font name on every img as font/0/0-arial.jpg)


##JPEG CHAR TRAINING
training - single font (works)
training - font in subfolders (not finished, have issues, work in progress)


##RECOGNIZE
recognize.py
* reads JPEG img
* cleans img (results in temp folder)
* extracts chars (results in plate-contours folder)
* KNearest return values of nearest dists and shows result

Need asistance to finish "training - font in subfolders.py"
