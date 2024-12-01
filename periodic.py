from dolfin import *

#TODO periodic
# https://oldqa.fenicsproject.org/8682/periodic-boundary-conditions-for-dg/

class PeriodicBoundary(SubDomain):
    def inside(self, x, on_boundary):
        return bool(x[0] < DOLFIN_EPS and x[0] > -DOLFIN_EPS and on_boundary)
    def map(self, x, y):
        y[0] = x[0] - 1.0