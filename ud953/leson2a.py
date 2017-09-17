# -*- coding: utf-8 -*-
"""
Created on Sat May 20 10:56:27 2017

@author: spiovesan
"""

import math
import lib.vector as v

if False:
    my_v11 = v.Vector([8.218,-9.341])
    my_v12 = v.Vector([-1.129,2.111])
    my_v21 = v.Vector([7.119,8.215])
    my_v22 = v.Vector([-8.223,0.878])
    my_v31 = v.Vector([1.671,-1.012,-0.318])
    print(my_v11.coordinates)
    t=tuple(map(lambda x, y: x + y, my_v11.coordinates,my_v12.coordinates))
    t=tuple(map(lambda x, y: x - y, my_v11.coordinates,my_v12.coordinates))
    print(t)
    print(my_v11+my_v12)
    print(my_v21-my_v22)
    print(my_v31*7.41)
    
    my_v34 = v.Vector([3,4])
    print(math.sqrt(sum(i**2 for i in my_v34.coordinates)))
    
    my_v32 = v.Vector([-0.221,7.437])
    print(my_v32.mag())
    my_v33 = v.Vector([5.581,-2.136])
    print(my_v33.norm())
    my_v33 = v.Vector([8.813,-1.331,-6.247])
    print(my_v33.mag())
    my_v33 = v.Vector([1.996,3.108,-4.554])
    print(my_v33.norm())

    #dot
    v_d1 = v.Vector([7.887,4.138])
    w_d1 = v.Vector([-8.802,6.776])
    print(v_d1.dot(w_d1))
    
    v_d2 = v.Vector([3.183,-7.627])
    w_d2 = v.Vector([-2.668,5.319])
    print(v_d2.angle(w_d2))
    
    v_d3 = v.Vector([-5.955,-4.904,-1.874])
    w_d3 = v.Vector([-4.496,-8.755,7.103])
    print(v_d3.dot(w_d3))
    
    v_d4 = v.Vector([7.35,0.221,5.188])
    w_d4 = v.Vector([2.751,8.259,3.985])
    print(math.degrees(v_d4.angle(w_d4)))

    v1 = v.Vector([-7.597,-7.88])
    w1 = v.Vector([22.737,23.64])
    print(v1.dot(w1))
    print(math.degrees(v1.angle(w1)))
    
    v1 = v.Vector([-2.029, 9.97,4.172])
    w1 = v.Vector([-9.231,-6.639,-7.245])
    print(v1.dot(w1))
    print(math.degrees(v1.angle(w1)))
    
    v1 = v.Vector([-2.328,-7.284,-1.214])
    w1 = v.Vector([-1.821,1.072,-2.94])
    print(v1.dot(w1))
    print(math.degrees(v1.angle(w1)))
    
    v1 = v.Vector([2.118,4.827])
    w1 = v.Vector([0,0])
    print(v1.dot(w1))
    print(math.degrees(v1.angle(w1)))
     
    a=tuple([-7.579,-7.88])
    b=tuple([22.737,23.64])
    l=map(lambda x, y: x * y, a, b)
    
    #projections
    v1 = v.Vector([3.039,1.879])
    w1 = v.Vector([0.825,2.036])
    print(v1.component_parallel_to(w1))
    
    v1 = v.Vector([-9.88,-3.264,-8.159])
    w1 = v.Vector([-2.155,-9.353,-9.473])
    print(v1.component_orthogonal_to(w1))
    
        
    v1 = v.Vector([3.009,-6.172,3.692,-2.51])
    w1 = v.Vector([6.404,-9.144,2.759,8.718])
    print(v1.component_parallel_to(w1))
    print(v1.component_orthogonal_to(w1))


    #cross product
    v1 = v.Vector([8.462,7.893,-8.187])
    w1 = v.Vector([6.984,-5.975,4.778])
    print(v1.cross_product(w1))
    v1 = v.Vector([-8.987,-9.838,5.031])
    w1 = v.Vector([-4.268,-1.861,-8.866])
    print(v1.cross_parallelogram_area(w1))
    v1 = v.Vector([1.5,9.547,3.691])
    w1 = v.Vector([-6.007,0.124,5.772])
    print(v1.cross_triangle_area(w1))
    
v_d1 = v.Vector([7.887,4.138])
w_d1 = v.Vector([-8.802,6.776])
print(v_d1.dot(w_d1))
print(v_d1.plus(w_d1))
