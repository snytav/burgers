from dolfin import *

def get_periodic_BC(u0,V,on_left,on_right):
    u = u0.vector().get_local()
    bc_left = DirichletBC(V, u[-2], on_left)
    bc_right = DirichletBC(V, u[1], on_right)
    bc = [bc_left, bc_right]
    return bc