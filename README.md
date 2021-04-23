# ANPR-KNearest
ANPR KNearest create img's from TTF font, train and recognize licence plate

This is my first Github Python project.

1. TTF TO JPEG
create font - single folder.py
Creates jpeg's from TTF font in single folder

create font - subfolderes.py
Creates jpeg's from TTF font in subfolders, one char one folder

2. JPEG CHAR TRAINING
training - single font
works
training - font in subfolders
(still have issues)

3. RECOGNIZE
recognize.py
- reads JPEG img
- cleans img (results in temp folder)
- extracts chars (results in plate-contours folder)
- KNearest return values of nearest dists and shows result
