import sys
 
# Replace the value of string variable py_ext_path 
# with the actual Python extension installation path in your computer
 
py_ext_path = r"C:\Users\yusuf\AppData\Local\Programs\Python\Python38-32\Lib\site-packages"
 
if py_ext_path not in sys.path:
    sys.path.append(py_ext_path)

# bu kod origin python modullrini alablsin diyedr
#ancak işe yaramadı
