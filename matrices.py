from scipy.spatial.transform import Rotation as Rot
import numpy as np
from numpy import sin as S
from numpy import cos as C
from math import atan2, sqrt
from math import pi


def expand_rotation(rot):
    tmp = np.eye(4,4)
    tmp[:3,:3] = rot
    return tmp
    
def Rx(q):
    """
    :param q: in radians!!
    """
    return expand_rotation(Rot.from_euler('x', q).as_dcm())

def Ry(q):
    """
    :param q: in radians!!
    """
    return expand_rotation(Rot.from_euler('y', q).as_dcm())

def Rz(q):
    """
    :param q: in radians!!
    """
    return expand_rotation(Rot.from_euler('z', q).as_dcm())

def Tx(mov):
    tmp = np.eye(4,4)
    tmp[0,3] = mov
    return tmp

def Ty(mov):
    tmp = np.eye(4,4)
    tmp[1,3] = mov
    return tmp

def Tz(mov):
    tmp = np.eye(4,4)
    tmp[2,3] = mov
    return tmp


def Tr(xyz,rpy):
    [r,p,y] = rpy
    R = np.array([[C(p)*C(y), C(y)*S(p)*S(r)-S(y)*C(r), C(y)*S(p)*C(r)+S(y)*S(r)],
                  [C(p)*S(y), S(y)*S(p)*S(r)+C(y)*C(r), S(y)*S(p)*C(r)-C(y)*S(r)],
                  [-S(p), C(p)*S(r), C(p)*C(r)]
                 ])
    res = np.eye(4,4)
    res[:3,:3] = R
    [x,y,z] = xyz
    res[0,3] = x
    res[1,3] = y
    res[2,3] = z
    return res  

def dRx(q):
    R = Rot.from_euler('x', q + pi/2).as_dcm()
    tmp = np.zeros((4,4))
    tmp[:3,:3] = R
    tmp[0,0] = 0.0
    return tmp

def dRy(q):
    R = Rot.from_euler('y', q + pi/2).as_dcm()
    tmp = np.zeros((4,4))
    tmp[:3,:3] = R
    tmp[1,1] = 0.0
    return tmp

def dRz(q):
    R = Rot.from_euler('z', q + pi/2).as_dcm()
    tmp = np.zeros((4,4))
    tmp[:3,:3] = R
    tmp[2,2] = 0.0
    return tmp

def dTx(mov):
    tmp = np.zeros((4,4))
    tmp[0,3] = 1
    return tmp


def dTy(mov):
    tmp = np.zeros((4,4))
    tmp[1,3] = 1
    return tmp


def dTz(mov):
    tmp = np.zeros((4,4))
    tmp[2,3] = 1
    return tmp
