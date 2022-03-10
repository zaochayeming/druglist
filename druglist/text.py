import re

s = r'本品主要成份为多肽和核糖（从猪脾脏中提取）；辅料为<a class=bluehref="http://ypk.39.net/yaopin/xxgyy/kxk/797f4.html"target=_blank>右旋糖酐</a>'

print(re.sub('<[^>]*>', '', s))
