'''
Created on 2012-12-24

@author: virusyang
'''
class Matrix:
    def __init__(self,Image):
        self.image=Image
        self.matrix=[]
        
    def getMatrix(self):
        width,height=self.image.size
        for i in range(width):
            for j in range(height):
                if(self.image.getpixel((i,j))==0):
                    self.matrix.append((i,j))
        return self.matrix            

class MatrixHandler:
    def __init__(self,data):
        self.data=data
        
    def doHandler(self):
        print self.data
                        