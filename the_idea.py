# -*- coding: utf-8 -*-
"""
JobCode : F1C
JobDes  : Final Exam. 2567/1 

StudID  : 6710301025
StudName: Muhammadhasan Useng
Date    : 2024-10-03 xx:xx  
"""
import math

#*****************************
#***** class TriangleSet *****
#*****************************
class TriangleSet():
    """class for Triangle Set """
    def __init__(self, triCode, sizeA, sizeB, sizeC, area ):
        """Constructor Method to create TriangleSet instance """
        self.triCode = triCode
        self.sizeA = sizeA
        self.sizeB = sizeB
        self.sizeC = sizeC
        self.area = area

    def __str__(self):
        return f'{self.triCode}, {self.sizeA}, {self.sizeB}, {self.sizeC}, {self.area}'
        

# ***** Read Triangle File To triangle Memory *****
def triangleFile2TriMem(inFN):
    """ Read inFN(File) return trCol(Column), triMem(Memory) """    
    fin = open(inFN , 'r')
    trMem = []
    i = 0
    with fin:
        for rec in fin:
            triCode, sizeA, sizeB, sizeC, area = rec.split()
            trMem.append(TriangleSet(triCode ,sizeA ,sizeB ,sizeC, area))
            
            if i:
                triCode = float(triCode)
                sizeA = float(sizeA)
                sizeB = float(sizeB)
                sizeC = float(sizeC)
                area = float(area)
                trMem.append(TriangleSet(triCode, sizeA, sizeB, sizeC, area))
            else:
                trCol = f'{triCode:5}, {sizeA:10}, {sizeB:10}, {sizeC:10}, {area:10}'
    i += 1
    return trMem
            
            
# ***** Show All Triangle Memory *****
def showAlltriMem(trCol, trMem):
    """ Show All trMem(TriangleMem) return Total data, trQty, notrQty """
    totData = 0
    trQty = 0
    notrQty = 0
    print(trCol)
    
    for triset in trMem:
        totData += triset.area
        trQty += triset.area
        notrQty += triset.area
       
        print(triset)

    return totData, trQty, notrQty
def totAlltriMem(trMem):    
    """ trMem(TriangleMem) return Total data, trQty, notrQty """
#     totData = 0
#     trQty = 0
#     notrQty = 0
#     print(trCol)
    
#     for triset in trMem:
#         totData += triset.area
#         trQty += triset.area
#         notrQty += triset.area
        
#         print(triset)
        
        
#     return totData, trQty, notrQty


# ***** Write Triangle Memory to File *****
def trMemToTriangleFile(trCol, trMem, outFN):
    """ Write trMem to Triangle file """
    fout = open(outFN, 'w')
    with fout:
        fout.write(trCol + '\n')
        for rec in trMem:
            newrec = rec.__str__()
            fout.write( f'{newrec}\n')
    
    return


#*************************************
#***** subroutine from FlowChart *****
#*************************************
def bigAndSmall(a, b):
    """ return small, big"""
    if a < b:
        big = b 
        small = a
    else:
        big = a 
        small = b
            
    return (small, big)

def biggestOfThree(a, b, c):
    """ return s1,s2,s3 that s3 is the biggest """   
    s1, s2 = bigAndSmall(a, b)
    s2, s3 = bigAndSmall(s2, c)
    
    return (s1, s2, s3)

def isZero(a, b, c):
    """ return iz is qty of zero """   
    iz = 0 
    if a == 0:
        iz += 1
    elif b == 0:
        iz += 1 
    elif c == 0:
        iz += 1 
           
    return iz

def isNotTriangle(a, b, c):
    """ return ierr, errcode = 1,2,3,4 is not triangle """
    ierr = isZero(a, b, c)
    
    while ierr == 0:
        s1, s2, s3 = biggestOfThree(a, b, c)
        
        if s3 > (s1 + s2):
            ierr = 4
                    
    return ierr

def trueTriangleArea(a, b, c):
    """ return Cal. Triang;e Area from a, b, c """
    s = (a + b + c) / 2 
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    
    return area

def allTriangleArea(a, b, c):
    """ return Cal. Triang;e Area from a, b, c """
    ierr = isNotTriangle(a, b, c)
    
    if ierr == 0:
        area = trueTriangleArea(a, b, c)
    elif ierr == 1:
        area = -991
    elif ierr == 2:
        area = -992
    elif ierr == 3:
        area = -993
    elif ierr == 4:
            area = -994    
        
    
    return area




#********************
#*** Main Program ***
#********************
if __name__ == "__main__":
    """ read file """
    trMem = triangleFile2TriMem('InputDataA.txt')
    
    trCol, trMem = showAlltriMem(trCol, trMem, trMem) # type: ignore
    
    trMemToTriangleFile(trCol, trMem, 'OutputDataA.txt')    

    print(trMem)    
    
    
    
    
    
    
    
    
    
    
    
    
    
#**** Test def bigAndSmall(a,b) ***
    # x = 10
    # y = 2 
    # sm, bg = bigAndSmall(x, y)
    # print(f'    x,   y = {x:8.2f},{y: 8.2f}')
    # print(f'Small, Big = {sm:8.2f},{bg:8.2f}')
#**** end  Test ****

#**** Test def biggestOfThree(a, b, c) ***
    # x = 15
    # y = 10
    # z = 25
    # s1, s2, s3 = biggestOfThree(x, y, z)
    # print(f' x,  y,  z = {x:8.2f},{y: 8.2f},{z: 8.2f}')
    # print(f's1, s2, s3 = {s1:8.2f},{s2:8.2f},{s3:8.2f}')
#**** end  Test ****

#**** Test def isZero(a, b, c) ***
    # x = 20
    # y = 0.0
    # z = 0.15
    # izero = isZero(x, y, z)
    # print(f' x,  y,  z = {x:8.2f},{y: 8.2f},{z: 8.2f}')
    # print(f'There are {izero}')
#**** end  Test ****

#**** Test def isNotTriangle(a, b, c)  ***
    # a = 3
    # b = 4
    # c = 5
    # ierr = isNotTriangle(a, b, c)
    # print(f'a,  b,  c = {a:8.2f},{b: 8.2f},{c: 8.2f}')
    # if ierr == 0:
    #     print(f'This is Triangle')
    # else:
    #     print(f'This is not Triangle')
        
    # print(f'ierr = {ierr}')
#**** end  Test ****

#**** Test def allTriangleArea(a, b, c)  ***
    # a = 1
    # b = 2
    # c = 3
    # area = allTriangleArea(a, b, c)
    # print(f'a,  b,  c = {a:8.2f},{b: 8.2f},{c: 8.2f}')
    # if area > 0:
    #     print(f'\nThis is Triangle')
    # else:
    #     print(f'\nThis is not Triangle')
        
    # print(f'area = {area:8.2f}')
#**** end  Test ****

#**** Test Input, Output File from class TriangleSet:
    # inFN = 'InputDataA.txt'

    # trCol, trMem = triangleFile2TriMem(inFN)
    # totData, trQty, notrQty = showAlltriMem(trCol, trMem)
    # print(f'\nTotal Data     = {totData:6,}')
    # print(f'Total Triangle = {trQty:6,}')
    # print(f'Total not Tri. = {notrQty:6,}')
    # print(f'------ end ------')
    
    # outFN = 'OutputData.txt'
    # trMemToTriangleFile(trCol, trMem, outFN)
#**** end  Test ****