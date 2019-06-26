import numpy
import pylab

class Striatum():
	def __init__(self):
		pass
		
	def run(self,sim,p,file_name):		
		sim.setup(p.timestep,p.min_delay,p.max_delay,seed=0.1)
                # Define neurons and cortical input		
		st1 = sim.Population(2,'iaf_cond_alpha',cellparams={"V_reset":p.vm, "V_th": p.th, "tau_syn_ex":p.tau_synE, "tau_syn_in":p.tau_synI, "E_L":p.vm, "E_ex":p.E_ex, "E_in":p.E_in, "I_e":p.ie, "C_m":p.cm, "g_L":p.gL, "t_ref":p.tref, "V_m":p.vm})
		# Define background input
		cort0 = sim.Population(1,'poisson_generator',{'rate':p.r0*(1-p.cb)})
		corti = sim.Population(1,'poisson_generator',{'rate':p.ri*(1-p.cb)})
		p01 = sim.Projection(cort0,st1,sim.AllToAllConnector())
		p01.setWeights(p.je)
		p0i1 = sim.Projection(corti,st1,sim.AllToAllConnector())
		p0i1.setWeights(p.ji)

		cort0c = sim.Population(1,'poisson_generator',{'rate':p.r0*p.cb})
		par0 = sim.Population(1,'parrot_neuron')
		cortic = sim.Population(1,'poisson_generator',{'rate':p.ri*p.cb})
		pari = sim.Population(1,'parrot_neuron')
		p00c = sim.Projection(cort0c,par0,sim.AllToAllConnector())
		p01c = sim.Projection(par0,st1,sim.AllToAllConnector())
		p01c.setWeights(p.je)
		piic = sim.Projection(cortic,pari,sim.AllToAllConnector())
		p0i1c = sim.Projection(pari,st1,sim.AllToAllConnector())
		p0i1c.setWeights(p.ji)

		# Record and simulate
		st1.record_v()
		st1.record()
		sim.run(p.runtime)

		# Output
		st1_file = 'n1_' + file_name + '.gdf'
		st1.printSpikes(st1_file)
		vst1_file = 'vn1_' + file_name + '.gdf'
		st1.print_v(vst1_file,compatible_output=False)
		sim.end()
