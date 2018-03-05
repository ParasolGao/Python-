# -*- coding: utf-8 -*-

class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise 'width must be a integer!'
        if value < 0 or value > 100000:
            raise 'width must between 0~100!'
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise 'height must be a integer!'
        if value < 0 or value > 1000000:
            raise 'height must between 0~100!'
        self._height = value
    
    @property
    def resolution(self):
        return self._width * self._height
    
    
# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')