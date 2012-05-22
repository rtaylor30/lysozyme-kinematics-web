from scipy.integrate import odeint
import numpy as np
import pylab as pylab
import datetime

t = None
k = None

def mm_rate(z, k):
  """The Michealis-Menten reaction rate a concentration z and rate parameter k"""
  s,e,c,j = z
  k_bind,k_unbind,k_cat = k
  return np.array([-k_bind*s*e+k_unbind*c,
           -k_bind*s*e+k_unbind*c+k_cat*c,
          k_bind*s*e-k_unbind*c-k_cat*c,
                    k_cat*c])

class MichealisMenten:
  def __init__(self, s0, e0):
    self.s0 = s0
    self.e0 = e0
    self.root_url = 'static/'

  #an example of the kinetics
  def kinetics(self):
    global t, k
    s_0, e_0 = self.s0, self.e0
    z_0 = [s_0, e_0, 0.0, 0.0]
    k = [1.0,1.1,.2]

    T = 30
    N_points = 1000
    t = np.linspace(0,T,N_points).T

    # Solve the ordinary differential equations for each timepoint t.
    z = odeint(lambda zed,t: mm_rate(zed,k),z_0,t)

    pylab.plot(t,z)
    pylab.legend(['$s$','$e$','$c','$j$'])
    pylab.xlabel('time')
    pylab.ylabel('concentration')
    figure_name = 'kinetics_' + str(self.s0) + '_' + str(self.e0) + '.png'
    pylab.savefig(self.root_url + figure_name)
    pylab.clf()
    return figure_name

  #example of how turbidity depends on initial concentration

  def turbidity_time_series(self, Z_0,turbid_fun):
    global k
    return np.array([turbid_fun(odeint(lambda zed,t: mm_rate(zed,k),z_0,t)) for z_0 in Z_0]).T

  def turbidity(self):
    turbid_funs = [lambda z: 1- z[:,3]/z[0,0],
                 lambda z: 1- z[:,3]**2/z[0,0]**2,
                 lambda z: 1- np.sqrt(z[:,3]/z[0,0])]
  
    s_0 = self.s0
    E_0 = [0.5, 1.0, 2.0, 4.0, 8.0]
    Z_0 = [[s_0, e_0, 0.0, 0.0] for e_0 in E_0]

    simple_turbidity = self.turbidity_time_series(Z_0,turbid_funs[0])

    pylab.plot(t,simple_turbidity)
    pylab.xlabel('time')
    pylab.ylabel('turbidity')
    pylab.legend(['$e_0$ = '+str(e_0) for e_0 in E_0])
    figure_name_1 = 'simple_' + str(self.s0) + '_' + str(self.e0) + '.png'
    pylab.savefig(self.root_url + figure_name_1)
    pylab.clf()

  # demonstration of how the turbidity calibration function matters
    turbidities = np.array([self.turbidity_time_series(Z_0,fun)[:,3] for fun in turbid_funs]).T

    pylab.plot(t,turbidities)
    pylab.xlabel('time')
    pylab.ylabel('turbidity')
    pylab.legend(['flat','upward curved','downward curved'])
    figure_name_2 = 'turbidity_' + str(self.s0) + '_' + str(self.e0) + '.png'
    pylab.savefig(self.root_url + figure_name_2)
    pylab.clf()
    return figure_name_1, figure_name_2

