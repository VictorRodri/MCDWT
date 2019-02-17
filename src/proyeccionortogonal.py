from numpy.linalg import lstsq 

def VecProduct(vek1, vek2): 
    return (vek1[0]*vek2[0] + vek1[1]*vek2[1] + vek1[2]*vek2[2]) 

def CalcPlane(x, y, z): 
    # x, y and z are given in lists 
    n = len(x) 
    sum_x = sum_y = sum_z = sum_xx = sum_yy = sum_xy = sum_xz = sum_yz = 0 
    for i in range(n): 
     sum_x += x[i] 
     sum_y += y[i] 
     sum_z += z[i] 
     sum_xx += x[i]*x[i] 
     sum_yy += y[i]*y[i] 
     sum_xy += x[i]*y[i] 
     sum_xz += x[i]*z[i] 
     sum_yz += y[i]*z[i] 

    M = ([sum_xx, sum_xy, sum_x], [sum_xy, sum_yy, sum_y], [sum_x, sum_y, n]) 
    b = (sum_xz, sum_yz, sum_z) 

    a,b,c = lstsq(M, b)[0] 

    ''' 
    z = a*x + b*y + c 
    a*x = z - b*y - c 
    x = -(b/a)*y + (1/a)*z - c/a 
    ''' 

    r0 = [-c/a, 
      0, 
      0] 

    u = [-b/a, 
     1, 
     0] 

    v = [1/a, 
     0, 
     1] 

    xn = [] 
    yn = [] 
    zn = [] 

    # orthogonalize u and v with Gram-Schmidt to get u and w 

    uu = VecProduct(u, u) 
    vu = VecProduct(v, u) 
    fak0 = vu/uu 
    erg0 = [val*fak0 for val in u] 
    w = [v[0]-erg0[0], 
     v[1]-erg0[1], 
     v[2]-erg0[2]] 
    ww = VecProduct(w, w) 

    # P_new = ((x*u)/(u*u))*u + ((x*w)/(w*w))*w 
    for i in range(len(x)): 
     xu = VecProduct([x[i], y[i], z[i]], u) 
     xw = VecProduct([x[i], y[i], z[i]], w) 
     fak1 = xu/uu 
     fak2 = xw/ww 
     erg1 = [val*fak1 for val in u] 
     erg2 = [val*fak2 for val in w] 
     erg = [erg1[0]+erg2[0], erg1[1]+erg2[1], erg1[2]+erg2[2]] 
     erg[0] += r0[0] 
     xn.append(erg[0]) 
     yn.append(erg[1]) 
     zn.append(erg[2]) 

    return (xn,yn,zn) 
