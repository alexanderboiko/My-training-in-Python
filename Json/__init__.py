print('__init__package1')
# from .file1 import *
# from .file2 import *

__all__ = ['file2']
from . import file1, file2
# . текущий каталог
# .. каталог выше