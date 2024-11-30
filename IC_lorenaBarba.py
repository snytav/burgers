import numpy
import sympy
def IC(nx0):
    x, nu, t = sympy.symbols('x nu t')
    phi = (sympy.exp(-(x - 4 * t)**2 / (4 * nu * (t + 1))) +
           sympy.exp(-(x - 4 * t - 2 * sympy.pi)**2 / (4 * nu * (t + 1))))
    phi

    phiprime = phi.diff(x)
    from sympy.utilities.lambdify import lambdify

    u = -2 * nu * (phiprime / phi) + 4
    ufunc = lambdify((t, x, nu), u)
    print(ufunc(1, 4, 3))
    from matplotlib import pyplot



    ###variable declarations
    nx = nx0[0]
    nt = 100
    dx = 2 * numpy.pi / (nx - 1)
    nu = .07
    dt = dx * nu

    x = numpy.linspace(0, 2 * numpy.pi, nx)
    un = numpy.empty(nx)
    t = 0

    u = numpy.asarray([ufunc(t, x0, nu) for x0 in x])
    return u

    return phiprime