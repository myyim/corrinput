from NeuroTools.parameters import ParameterSet
from NeuroTools.parameters import ParameterRange
import corr_poisson as st
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
p.runtime = 100000.

# Parameters for number and connections
p.r0 = 2000.	# excitatory input rate
p.ri = 1647.	# inhibitory input rate
p.je = 0.015	# excitatory synaptic weight
p.ji = -0.015	# inhibitory synaptic weight
p.cb = ParameterRange(numpy.arange(0.,1.001,0.05))	# between-cell correlation

dims,labels =  p.parameter_space_dimension_labels()
results = numpy.empty(dims)
for experiment in p.iter_inner():
	name = make_name(experiment,p.range_keys())
	print name
	model = st.Striatum()
	model.run(sim,experiment,name)
	index = p.parameter_space_index(experiment)	
	results[index] = 0
