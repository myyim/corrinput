from NeuroTools.parameters import ParameterSet
from NeuroTools.parameters import ParameterRange
import corr_SDNSD as st
import pyNN.nest as sim
from NeuroTools.sandbox import make_name
from NeuroTools.sandbox import check_name
import numpy

p = ParameterSet({})
# Parameters for neuronal features
p.vm = -65.
p.th = -50.
p.tau_synE = 0.3
p.tau_synI = 2.
p.E_ex = 0.
p.E_in = -70.
p.ie = 0.
p.cm = 500.
p.gL = 25.
p.tref = 2.

# Parameters for running
p.timestep = 0.1
p.min_delay = 0.1
p.max_delay = 5.1
p.runtime = 500000.

# Parameters for number and connections
p.r0 = 1400.	# excitatory input rate
p.ri = 1647.	# inhibitory input rate
p.je = 0.015	# excitatory synaptic weight
p.ji = -0.015	# inhibitory synaptic weight
p.cb = ParameterRange(numpy.arange(1.,1.001,0.05))	# between-cell correlation of background input (NSD input)
p.N = 1000	# number of daughter cells for MIP
p.r = ParameterRange(numpy.arange(100.,101.,400.))	# MIP rate
p.c = ParameterRange(numpy.array([0.05]))	# with-pool correlation in MIP
p.q = ParameterRange(numpy.arange(0.2,0.2501,0.05))	# between-cell correlation of MIP input (SD input)
p.edge = ParameterRange(numpy.array([0.]))	# range of temporal jitter of MIP

dims,labels =  p.parameter_space_dimension_labels()
results = numpy.empty(dims)
for experiment in p.iter_inner():
	name = make_name(experiment,p.range_keys())
	print name
	model = st.Striatum()
	model.run(sim,experiment,name)
	index = p.parameter_space_index(experiment)	
	results[index] = 0
