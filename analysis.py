import pylab
import numpy
import netfunc
import miscfunc
import matplotlib as mpl
font_size = 20
mpl.rcParams['axes.titlesize'] = font_size+14
mpl.rcParams['xtick.labelsize'] = font_size+8
mpl.rcParams['ytick.labelsize'] = font_size+8
mpl.rcParams['axes.labelsize'] = font_size+10
mpl.rcParams['legend.fontsize'] = font_size+4
mpl.rcParams['font.size'] = font_size+14

def fig1():
	pylab.figure(figsize=(10, 7))
	pylab.subplot(211)
	data = numpy.loadtxt('./CorrMIP/CurrentInject/vn2_ie_00_.gdf')
	pylab.plot(data[:,1],data[:,2],'g',linewidth=3.)
	pylab.plot([1000,2000],[-50,-50],'k--',linewidth=2.)
	pylab.xlim(1000,2000)
	pylab.ylim(-67,-42)
	pylab.xticks([])
	pylab.yticks([-60,-50])
	pylab.subplot(212)
	d1 = numpy.loadtxt('./CorrMIP/ivn1_ie_600.0_.gdf')
	d2 = numpy.loadtxt('./CorrMIP/ivn1_ie_-800.0_.gdf')
	pylab.plot(d1[:,1],d1[:,2],'b',linewidth=3)
	pylab.plot(d2[:,1],d2[:,2],'r',linewidth=3)
	pylab.xlim(1000,2000)
	pylab.ylim(-78,-30)
	pylab.xticks([1000,1500,2000])
	pylab.yticks([-60,-40])
	pylab.xlabel('Time (ms)')
	pylab.ylabel('                      Membrane potential (mV)')
	pylab.subplots_adjust(bottom=0.12,left=0.14)
	pylab.savefig('fig1bc.eps')

def fig2():
	pylab.figure(figsize=(16,18))
	pylab.subplot(321)
	c = numpy.arange(0.,0.21,0.01)
	r = numpy.array([1000.,2000.])
	for n in range(r.size):
		out = numpy.zeros(c.size)
		for m in range(c.size):
			for l in range(1,6):
				filename = './CorrMIP/Trial'+str(l)+'/n1_c_'+str(c[m])+'_edge_0.0_r_'+str(r[n])+'_rho_1.0_tau_0.0_.gdf'
				f = open(filename,'r')
				f.readline()
				f.readline()
				f.readline()
				f.readline()
				f.readline()
				if f.readline() != '':
					out[m] += netfunc.rate(filename, start=100.0, dur=20000., num=1)
		if n == 0:
			pylab.plot(c,out/5.,'0.5',label='$r$='+str(int(r[n])),linewidth=3.)
		if n == 1:
			pylab.plot(c,out/5.,'k',label='$r$='+str(int(r[n])),linewidth=3.)
	pylab.xlim(0,0.2)
	pylab.ylim(0,22)
	pylab.ylabel('Output firing rate (Hz)')
	pylab.xticks([])
	pylab.legend(loc=8)
	pylab.subplot(322)
	c = numpy.arange(0.,0.21,0.01)
	t = numpy.array([-2.,0.,2.])
	for n in range(t.size):
		out = numpy.zeros(c.size)
		for m in range(1,c.size):
			for l in range(1,6):
				filename = './CorrMIP/Trial'+str(l)+'/n1_c_'+str(c[m])+'_edge_0.0_r_2000.0_rho_1.0_tau_'+str(t[n])+'_.gdf'
				f = open(filename,'r')
				f.readline()
				f.readline()
				f.readline()
				f.readline()
				f.readline()
				if f.readline() != '':
					out[m] += netfunc.rate(filename, start=100.0, dur=20000., num=1)
		if n == 0:
			pylab.plot(c,out/5.,'r',label='$t_{E} < t_{I}$',linewidth=3.)
		if n == 1:
			pylab.plot(c,out/5.,'k',label='$t_{E} = t_{I}$',linewidth=3.)
		if n == 2:
			pylab.plot(c,out/5.,'b',label='$t_{E} > t_{I}$',linewidth=3.)
	pylab.ylim(0,22)
	pylab.xlim(0,0.2)
	pylab.xticks([])
	pylab.legend(bbox_to_anchor = (0.64, 0.6))
	pylab.subplot(324)
	c = numpy.arange(0.,0.21,0.01)
	rho = numpy.arange(0.,1.1,0.5)
	for n in range(rho.size):
		out = numpy.zeros(c.size)
		for m in range(1,c.size):
			for l in range(1,6):
				filename = './CorrMIP/Trial'+str(l)+'/n1_c_'+str(c[m])+'_edge_0.0_r_2000.0_rho_'+str(rho[n])+'_tau_2.0_.gdf'
				f = open(filename,'r')
				f.readline()
				f.readline()
				f.readline()
				f.readline()
				f.readline()
				if f.readline() != '':
					out[m] += netfunc.rate(filename, start=100.0, dur=20000., num=1)
		if n == 0:
			pylab.plot(c,out/5.,'k',label='$c_{EI}=0$',linewidth=3.)
		if n == 1:
			pylab.plot(c,out/5.,'0.4',label='$c_{EI}=0.5$',linewidth=3.)
		if n == 2:
			pylab.plot(c,out/5.,'0.7',label='$c_{EI}=1$',linewidth=3.)
	pylab.text(0.15,18,'$t_{E} > t_{I}$')
	pylab.xlim(0,0.2)
	pylab.xticks([])
	pylab.ylim(0,22)
	pylab.subplot(323)
	c = numpy.arange(0.,0.21,0.01)
	rho = numpy.arange(0.,1.1,0.5)
	for n in range(rho.size):
		out = numpy.zeros(c.size)
		for m in range(1,c.size):
			for l in range(1,6):
				filename = './CorrMIP/Trial'+str(l)+'/n1_c_'+str(c[m])+'_edge_0.0_r_2000.0_rho_'+str(rho[n])+'_tau_-2.0_.gdf'
				f = open(filename,'r')
				f.readline()
				f.readline()
				f.readline()
				f.readline()
				f.readline()
				if f.readline() != '':
					out[m] += netfunc.rate(filename, start=100.0, dur=20000., num=1)
		if n == 0:
			pylab.plot(c,out/5.,'k',label='$c_{EI}=0$',linewidth=3.)
		if n == 1:
			pylab.plot(c,out/5.,'0.4',label='$c_{EI}=0.5$',linewidth=3.)
		if n == 2:
			pylab.plot(c,out/5.,'0.7',label='$c_{EI}=1$',linewidth=3.)
	pylab.text(0.15,18,'$t_{E} < t_{I}$')
	pylab.ylabel('Output firing rate (Hz)')
	pylab.xlim(0,0.2)
	pylab.xticks([])
	pylab.ylim(0,22)
	pylab.legend(loc=8)
	pylab.subplot(325)
	c = numpy.arange(0.,0.21,0.01)
	edge = numpy.arange(0.,3.1,1.)
	for n in range(edge.size):
		out = numpy.zeros(c.size)
		for m in range(1,c.size):
			for l in range(1,6):
				filename = './CorrMIP/Trial'+str(l)+'/n1_c_'+str(c[m])+'_edge_'+str(edge[n])+'_r_2000.0_rho_0.0_tau_0.0_.gdf'
				f = open(filename,'r')
				f.readline()
				f.readline()
				f.readline()
				f.readline()
				f.readline()
				if f.readline() != '':
					out[m] += netfunc.rate(filename, start=100.0, dur=20000., num=1)
		if n == 0:
			pylab.plot(c,out/5.,'k',label='$w=0$',linewidth=3.)
		if n == 1:
			pylab.plot(c,out/5.,'g',label='$w=2$',linewidth=3.)
		if n == 2:
			pylab.plot(c,out/5.,'c',label='$w=4$',linewidth=3.)
		if n == 3:
			pylab.plot(c,out/5.,'y',label='$w=6$',linewidth=3.)
	pylab.text(0.14,18,'$c_{EI}$ = 0')
	pylab.xlabel('Input correlation $c$')
	pylab.ylabel('Output firing rate (Hz)')
	pylab.xlim(0,0.2)
	pylab.xticks(numpy.arange(0.,0.21,0.1),('  0','0.1','0.2'))
	pylab.ylim(0,22)
	pylab.legend(loc=8)
	pylab.subplot(326)
	c = numpy.arange(0.,0.21,0.01)
	edge = numpy.arange(0.,3.1,1.)
	for n in range(edge.size):
		out = numpy.zeros(c.size)
		for m in range(1,c.size):
			for l in range(1,6):
				filename = './CorrMIP/Trial'+str(l)+'/n1_c_'+str(c[m])+'_edge_'+str(edge[n])+'_r_2000.0_rho_1.0_tau_0.0_.gdf'
				f = open(filename,'r')
				f.readline()
				f.readline()
				f.readline()
				f.readline()
				f.readline()
				if f.readline() != '':
					out[m] += netfunc.rate(filename, start=100.0, dur=20000., num=1)
		if n == 0:
			pylab.plot(c,out/5.,'k',label='$w=0$',linewidth=3.)
		if n == 1:
			pylab.plot(c,out/5.,'g',label='$w=2$',linewidth=3.)
		if n == 2:
			pylab.plot(c,out/5.,'c',label='$w=4$',linewidth=3.)
		if n == 3:
			pylab.plot(c,out/5.,'y',label='$w=6$',linewidth=3.)
	pylab.text(0.14,18,'$c_{EI}$ = 1')
	pylab.xlabel('Input correlation $c$')
	pylab.xlim(0,0.2)
	pylab.xticks(numpy.arange(0.,0.21,0.1),('  0','0.1','0.2'))
	pylab.ylim(0,22)
	pylab.subplots_adjust(bottom=0.07,left=0.07,right=0.94)
	pylab.savefig('fig2.eps')

def fig3():
	pylab.figure(figsize=(16, 12))
	pylab.subplot(222)
	filename = './CorrSpikes/Poisson/vn1_cb_0.72_.gdf'
	filesp = './CorrSpikes/Poisson/n1_cb_0.72_.gdf'
	data = numpy.loadtxt(filename)
	spk = numpy.loadtxt(filesp)
	data = data[data[:,1]<=2000.]
	d1 = data[data[:,0]==1.,1:]
	d2 = data[data[:,0]==2.,1:]
	sp1 = spk[spk[:,1]==0.,0]
	sp2 = spk[spk[:,1]==1.,0]
	for j in sp1:
		k = numpy.argmin((d1[:,0]-j)**2)
		d1[k:k+5,1] = -40.
	for j in sp2:
		k = numpy.argmin((d2[:,0]-j)**2)
		d2[k:k+5,1] = -40.
	pylab.plot(d1[:,0]+200,d1[:,1],'#00CC00',linewidth=4)
	pylab.plot(d2[:,0]+200,d2[:,1],'#006600',linewidth=2)
	pylab.plot([1000,1600],[-50,-50],'k--',linewidth=2)
	pylab.xlim(1000,1600)
	pylab.ylim(-68,-40)
	pylab.xticks([1000,1200,1400,1600])
	pylab.yticks([-60,-50,-40])
	pylab.xlabel('Time (ms)')
	pylab.ylabel('MP (mV)')
	pylab.subplot(223)
	c = numpy.arange(0.,1.01,0.05)
	bin = 5.
	maxtime = 1000000.
	start = 100.
	sem_spk = numpy.empty(c.size)
	spcor_tri = numpy.empty(c.size)
	sem_mp = numpy.empty(c.size)
	mpcor_nospk = numpy.empty(c.size)
	r = numpy.empty(c.size)
	path = './CorrSpikes/Poisson/'
	for j in range(c.size):
		filename = 'n1_cb_'+str(c[j])+'_.gdf'
		spcor_tri[j],sem_spk[j] = spikecorr_tri_conv5(filename,bin,maxtime,path=path)
		mpcor_nospk[j],sem_mp[j] = mpcorr_nospk5(filename,maxtime/10.,path=path)
		r[j] = rate(filename,path=path)
	pylab.fill_between(c,spcor_tri-sem_spk,spcor_tri+sem_spk,alpha=0.5,facecolor='y',edgecolor='white')
	pylab.plot(c,spcor_tri,'y',linewidth=1,label='Spike corr')
	pylab.fill_between(c,mpcor_nospk-sem_mp,mpcor_nospk+sem_mp,alpha=0.5,facecolor='g',edgecolor='white')
	pylab.plot(c,mpcor_nospk,'g',linewidth=1,label='MP corr')
	pylab.legend(loc=2)
	pylab.ylabel('Output correlation')
	pylab.xlabel('SD Input correlation')
	pylab.ylim(-0.1,1.1)
	pylab.xticks([    0,0.5,1],('0','0.5','1'))
	pylab.yticks([    0,0.5,1],('0','0.5','1'))
	pylab.subplot(224)
	path = './CorrSpikes/Poisson/'
	filename = 'n1_cb_0.72_.gdf'
	npre = 300
	npost = 0
	thres = 100.
	mpdata = numpy.loadtxt(path+'v'+filename)
	spkdata = numpy.loadtxt(path+filename)
	spk0 = spkdata[spkdata[:,1]==0.,0]
	spk1 = spkdata[spkdata[:,1]==1.,0]
	v0 = mpdata[mpdata[:,0]==1.,1:]
	v1 = mpdata[mpdata[:,0]==2.,1:]
	count1 = 0
	premp1 = []
	for j in range(spk0.size):
		ind = numpy.argmin((v0[:,0]-spk0[j])**2)
		if j == 0 or spk0[j] - spk0[j-1] > thres:
			count1 += 1
			premp1.append(v0[ind-npre:ind+npost+1,1])
	for j in range(spk1.size):
		ind = numpy.argmin((v1[:,0]-spk1[j])**2)
		if j == 0 or spk1[j] - spk1[j-1] > thres:
			count1 += 1
			premp1.append(v1[ind-npre:ind+npost+1,1])
	count0 = 0
	premp0 = []
	for j in range(spk0.size):
		ind = numpy.argmin((v1[:,0]-spk0[j])**2)
		if spk1[(spk1>=spk0[j]-thres)*(spk1<=spk0[j])].size == 0:
			count0 += 1
			premp0.append(v1[ind-npre:ind+npost+1,1])
	for j in range(spk1.size):
		ind = numpy.argmin((v0[:,0]-spk1[j])**2)
		if spk0[(spk0>=spk1[j]-thres)*(spk0<=spk1[j])].size == 0:
			count0 += 1
			premp0.append(v0[ind-npre:ind+npost+1,1])
	pylab.plot(numpy.arange(-30.,0.,0.1),pylab.mean(premp1,axis=0)[:-1],'k',linewidth=3)
	pylab.plot(numpy.arange(-30.,0.,0.1),pylab.mean(premp0,axis=0)[:-1],'0.5',linewidth=3)
	pylab.xlim(-30,0)
	pylab.ylim(-61,-49)
	pylab.xlabel('Time (ms)')
	pylab.ylabel('STA (mV)')
	pylab.xticks([-30,-20,-10,0])
	pylab.yticks([-60,-50])
	pylab.subplots_adjust(bottom=0.09,left=0.09,right=0.95,wspace=0.3,hspace=0.25)
	pylab.savefig('fig3.svg')

def fig4():
	pylab.figure(figsize=(16, 12))
	pylab.subplot(222)
	filename = './CorrSpikes/MIPcorrbg/Revision/vn1_c_0.05_cb_1.0_q_0.0_r_100.0_.gdf'
	filesp = './CorrSpikes/MIPcorrbg/Revision/n1_c_0.05_cb_1.0_q_0.0_r_100.0_.gdf'
	data = numpy.loadtxt(filename)
	spk = numpy.loadtxt(filesp)
	d1 = data[data[:,0]==1.,1:]
	d2 = data[data[:,0]==2.,1:]
	sp1 = spk[spk[:,1]==0.,0]
	sp2 = spk[spk[:,1]==1.,0]
	for j in sp1:
		k = numpy.argmin((d1[:,0]-j)**2)
		d1[k:k+5,1] = -40.
	for j in sp2:
		k = numpy.argmin((d2[:,0]-j)**2)
		d2[k:k+5,1] = -40.
	pylab.plot(d1[:,0]+900,d1[:,1],'#00CC00',linewidth=4)
	pylab.plot(d2[:,0]+900,d2[:,1],'#006600',linewidth=2)
	pylab.plot([1000,1600],[-50,-50],'k--',linewidth=2.)
	pylab.xlim(1000,1600)
	pylab.ylim(-71,-40)
	pylab.xticks([1000,1200,1400,1600])
	pylab.yticks([-70,-60,-50,-40])
	pylab.xlabel('Time (ms)')
	pylab.ylabel('MP (mV)')
	pylab.subplot(223)
	c = numpy.arange(0.,1.01,0.05)
	bin = 5.
	maxtime = 500000.
	start = 100.
	sem_spk = numpy.empty(c.size)
	spcor_tri = numpy.empty(c.size)
	sem_mp = numpy.empty(c.size)
	mpcor_nospk = numpy.empty(c.size)
	r = numpy.empty(c.size)
	path = './CorrSpikes/MIPcorrbg/Revision/'
	for j in range(c.size):
		filename = 'n1_c_0.05_cb_1.0_q_'+str(c[j])+'_r_100.0_.gdf'
		spcor_tri[j],sem_spk[j] = spikecorr_tri_conv5(filename,bin,maxtime,path=path)
		mpcor_nospk[j],sem_mp[j] = mpcorr_nospk5(filename,maxtime,path=path)
		r[j] = rate(filename,path=path)
	pylab.fill_between(c,spcor_tri-sem_spk,spcor_tri+sem_spk,alpha=0.5,facecolor='y',edgecolor='white')
	pylab.plot(c,spcor_tri,'y',linewidth=1,label='Spike corr')
	pylab.fill_between(c,mpcor_nospk-sem_mp,mpcor_nospk+sem_mp,alpha=0.5,facecolor='g',edgecolor='white')
	pylab.plot(c,mpcor_nospk,'g',linewidth=1,label='MP corr')
	pylab.legend(loc=4)
	pylab.ylabel('Output correlation')
	pylab.xlabel('SD input correlation')
	pylab.ylim(-0.1,1.1)
	pylab.xticks([    0,0.5,1],('0','0.5','1'))
	pylab.yticks([    0,0.5,1],('0','0.5','1'))
	pylab.subplot(224)
	path = './CorrSpikes/MIPcorrbg/Revision/'
	filename = 'n1_c_0.05_cb_1.0_q_0.0_r_100.0_.gdf'
	npre = 500
	npost = 0
	thres = 100.
	mpdata = numpy.loadtxt(path+'v'+filename)
	spkdata = numpy.loadtxt(path+filename)
	spk0 = spkdata[spkdata[:,1]==0.,0]
	spk1 = spkdata[spkdata[:,1]==1.,0]
	v0 = mpdata[mpdata[:,0]==1.,1:]
	v1 = mpdata[mpdata[:,0]==2.,1:]
	count1 = 0
	premp1 = numpy.zeros(npre+npost+1)
	for j in range(spk0.size):
		ind = numpy.argmin((v0[:,0]-spk0[j])**2)
		if j == 0 or spk0[j] - spk0[j-1] > thres:
			count1 = count1 + 1
			premp1 = premp1 + v0[ind-npre:ind+npost+1,1]
	for j in range(spk1.size):
		ind = numpy.argmin((v1[:,0]-spk1[j])**2)
		if j == 0 or spk1[j] - spk1[j-1] > thres:
			count1 = count1 + 1
			premp1 = premp1 + v1[ind-npre:ind+npost+1,1]
	count0 = 0
	premp0 = numpy.zeros(npre+npost+1)
	for j in range(spk0.size):
		ind = numpy.argmin((v1[:,0]-spk0[j])**2)
		if spk1[(spk1>=spk0[j]-thres)*(spk1<=spk0[j])].size == 0:
			count0 = count0 + 1
			premp0 = premp0 + v1[ind-npre:ind+npost+1,1]
	for j in range(spk1.size):
		ind = numpy.argmin((v0[:,0]-spk1[j])**2)
		if spk0[(spk0>=spk1[j]-thres)*(spk0<=spk1[j])].size == 0:
			count0 = count0 + 1
			premp0 = premp0 + v0[ind-npre:ind+npost+1,1]
	premp1 = premp1/count1
	pylab.plot(numpy.arange(-50.,0.,0.1),premp1[:-1],'k',linewidth=3)
	pylab.plot([-0.1,-0.1],[-60,-50],'k',linewidth=3)
	premp0 = premp0/count0
	pylab.plot(numpy.arange(-50.,0.,0.1),premp0[:-1],'0.5',linewidth=3)
	pylab.xlim(-50,0)
	pylab.ylim(-63,-49)
	pylab.xlabel('Time (ms)')
	pylab.ylabel('STA (mV)')
	pylab.xticks([-40,-20,0])
	pylab.yticks([-60,-50])
	pylab.subplots_adjust(bottom=0.09,left=0.09,right=0.95,wspace=0.3,hspace=0.25)
	pylab.savefig('fig4.svg')

def fig5():
	pylab.figure(figsize=(16, 6))
	pylab.subplot(121)
	c = numpy.arange(0.,1.01,0.1)
	bin = 5.
	maxtime = 500000.
	sem_spk = numpy.empty(c.size)
	spcor_tri = numpy.empty(c.size)
	sem_mp = numpy.empty(c.size)
	mpcor_nospk = numpy.empty(c.size)
	r = numpy.empty(c.size)
	path = './CorrSpikes/MIPcorrbg/JitterLong/LONGER/'
	for j in range(c.size):
		filename = 'n1_c_0.05_cb_1.0_q_'+str(c[j])+'_r_100.0_r0_1400.0_.gdf'
		spcor_tri[j],sem_spk[j] = spikecorr_tri_conv5(filename,bin,maxtime,path=path)
		mpcor_nospk[j],sem_mp[j] = mpcorr_nospk5(filename,maxtime/5.,path=path)
		r[j] = rate(filename,path=path)
	pylab.fill_between(c,spcor_tri-sem_spk,spcor_tri+sem_spk,alpha=0.5,facecolor='y',edgecolor='none')
	pylab.plot(c,spcor_tri,'y',linewidth=1,label='Spike corr')
	pylab.fill_between(c,mpcor_nospk-sem_mp,mpcor_nospk+sem_mp,alpha=0.5,facecolor='g',edgecolor='none')
	pylab.plot(c,mpcor_nospk,'g',linewidth=1,label='MP corr')
	pylab.legend(loc=4)
	pylab.ylabel('Output correlation')
	pylab.xlabel('SD input correlation')
	pylab.ylim(-0.1,1.1)
	pylab.xticks([    0,0.5,1],('0','0.5','1'))
	pylab.yticks([    0,0.5,1],('0','0.5','1'))
	pylab.subplot(122)
	path = './CorrSpikes/MIPcorrbg/JitterLong/MP/'
	filename = 'n1_c_005_cb_10_q_00_r_1000_r0_14000_.gdf'
	npre = 500
	npost = 0
	thres = 100.
	mpdata = numpy.loadtxt(path+'v'+filename)
	spkdata = numpy.loadtxt(path+filename)
	spk0 = spkdata[spkdata[:,1]==0.,0]
	spk1 = spkdata[spkdata[:,1]==1.,0]
	v0 = mpdata[mpdata[:,0]==1.,1:]
	v1 = mpdata[mpdata[:,0]==2.,1:]
	count1 = 0
	premp1 = numpy.zeros(npre+npost+1)
	for j in range(spk0.size):
		ind = numpy.argmin((v0[:,0]-spk0[j])**2)
		if j == 0 or spk0[j] - spk0[j-1] > thres:
			count1 = count1 + 1
			premp1 = premp1 + v0[ind-npre:ind+npost+1,1]
	for j in range(spk1.size):
		ind = numpy.argmin((v1[:,0]-spk1[j])**2)
		if j == 0 or spk1[j] - spk1[j-1] > thres:
			count1 = count1 + 1
			premp1 = premp1 + v1[ind-npre:ind+npost+1,1]
	count0 = 0
	premp0 = numpy.zeros(npre+npost+1)
	for j in range(spk0.size):
		ind = numpy.argmin((v1[:,0]-spk0[j])**2)
		if spk1[(spk1>=spk0[j]-thres)*(spk1<=spk0[j])].size == 0:
			count0 = count0 + 1
			premp0 = premp0 + v1[ind-npre:ind+npost+1,1]
	for j in range(spk1.size):
		ind = numpy.argmin((v0[:,0]-spk1[j])**2)
		if spk0[(spk0>=spk1[j]-thres)*(spk0<=spk1[j])].size == 0:
			count0 = count0 + 1
			premp0 = premp0 + v0[ind-npre:ind+npost+1,1]
	premp1 = premp1/count1
	pylab.plot(numpy.arange(-50.,0.,0.1),premp1[:-1],'k',linewidth=3)
	premp0 = premp0/count0
	pylab.plot(numpy.arange(-50.,0.,0.1),premp0[:-1],'0.5',linewidth=3)
	pylab.xlim(-50,0)
	pylab.ylim(-63,-49)
	pylab.xlabel('Time (ms)')
	pylab.ylabel('STA (mV)')
	pylab.xticks([-40,-20,0])
	pylab.yticks([-60,-50])
	pylab.subplots_adjust(bottom=0.15,left=0.09,right=0.95,wspace=0.3,hspace=0.25)
	pylab.savefig('fig5.svg')

def fig6():
	pylab.figure(figsize=(24, 6))
	pylab.subplot(132)
	filename = './CorrSpikes/MIPexc/vn1_c_0.05_q_1.0_r_100.0_.gdf'
	filesp = './CorrSpikes/MIPexc/n1_c_0.05_q_1.0_r_100.0_.gdf'
	data = numpy.loadtxt(filename)
	spk = numpy.loadtxt(filesp)
	d1 = data[data[:,0]==1.,1:]
	d2 = data[data[:,0]==2.,1:]
	sp1 = spk[spk[:,1]==0.,0]
	sp2 = spk[spk[:,1]==1.,0]
	for j in sp1:
		k = numpy.argmin((d1[:,0]-j)**2)
		d1[k:k+5,1] = -40.
	for j in sp2:
		k = numpy.argmin((d2[:,0]-j)**2)
		d2[k:k+5,1] = -40.
	pylab.plot(d1[:,0]-600,d1[:,1],'#00CC00',linewidth=4)
	pylab.plot(d2[:,0]-600,d2[:,1],'#006600',linewidth=2)
	pylab.plot([1000,1600],[-50,-50],'k--',linewidth=2.)
	pylab.xlim(1000,1600)
	pylab.ylim(-68,-40)
	pylab.xticks([1000,1200,1400,1600])
	pylab.yticks([-60,-50,-40])
	pylab.xlabel('Time (ms)')
	pylab.ylabel('MP (mV)')
	pylab.subplot(133)
	c = numpy.arange(0.,1.01,0.05)
	bin = 5.
	maxtime = 100000.
	start = 100.
	sem_spk = numpy.empty(c.size)
	spcor_tri = numpy.empty(c.size)
	sem_mp = numpy.empty(c.size)
	mpcor_nospk = numpy.empty(c.size)
	r = numpy.empty(c.size)
	path = './CorrSpikes/MIPexc/'
	for j in range(c.size):
		filename = 'n1_c_0.05_q_'+str(c[j])+'_r_100.0_.gdf'
		spcor_tri[j],sem_spk[j] = spikecorr_tri_conv5(filename,bin,maxtime,path=path)
		mpcor_nospk[j],sem_mp[j] = mpcorr_nospk5(filename,maxtime,path=path)
		r[j] = rate(filename,path=path)
	pylab.fill_between(c,spcor_tri-sem_spk,spcor_tri+sem_spk,alpha=0.5,facecolor='y',edgecolor='white')
	pylab.plot(c,spcor_tri,'y',linewidth=1,label='Spike corr')
	pylab.fill_between(c,mpcor_nospk-sem_mp,mpcor_nospk+sem_mp,alpha=0.5,facecolor='g',edgecolor='white')
	pylab.plot(c,mpcor_nospk,'g',linewidth=1,label='MP corr')
	pylab.legend(loc=2)
	pylab.ylabel('Output correlation')
	pylab.xlabel('SD input correlation')
	pylab.ylim(-0.1,1.1)
	pylab.yticks([    0,0.5,1],('0','0.5','1'))
	pylab.xticks([    0,0.5,1],('0','0.5','1'))
	pylab.subplots_adjust(bottom=0.14,left=0.08,right=0.95,wspace=0.3,hspace=0.25)
	pylab.savefig('fig6.svg')

def scheme():
	mpl.rcParams['font.size'] = font_size+4
	maxtime = 100000.
	bin = 1.
	start = 100.
	c = numpy.arange(0.,1.01,0.05)
	spcor_tri = numpy.empty(c.size)
	path = './CorrSpikes/Poisson/'
	for j in range(c.size):
		filename = 'n1_cb_'+str(c[j])+'_.gdf'
		spcor_tri[j] = spikecorr_tri_conv(filename,bin,maxtime,start,path=path)
	pylab.figure(figsize=[10,10])
	pylab.fill_between([0,0.1],[0.9,0.9],[1,1],alpha='0.5',facecolor='b',edgecolor='b')
	cor = [0.00314977,0.0032535,0.00447223,0.00630221,0.008616,0.01234402,0.01607021,0.02094502,0.0268024,0.03223732,0.03962614,0.04860187,0.06047121,0.07751882,0.09638086,0.11804299,0.14732138,0.22350812,0.34813916,0.51702234,1.]
	pylab.fill_between(c,c,cor,alpha='0.5',facecolor='r',edgecolor='r')
#	print miscfunc.tri_convolve(spcor_tri)
	pylab.plot([0,1],[0,1],'0.5',linewidth=3)
	pylab.plot([0,1],[1,1],'k--',linewidth=3)
	pylab.plot([1,1],[0,1],'k--',linewidth=3)
	pylab.plot([0,0],[0,1],'k--',linewidth=3)
	pylab.plot([0,1],[0,0],'k--',linewidth=3)
	pylab.plot([0,1],[0,1],'ko',ms=10)
	pylab.text(0.45,0.2,'Correlated\nPoisson\ninput',color='r')
	pylab.text(0.7,1.,'Fully correlated\ninput')
	pylab.text(-0.1,-0.18,'Independent\ninput')
	pylab.text(0.15,0.85,'Synfire\nchain',color='b')
	pylab.ylabel('Spike correlation')
	pylab.xlabel('Membrane potential correlation')
	pylab.xticks([0,1],('0','1'))
	pylab.yticks([0,1],('0','1'))
	pylab.xlim(-0.2,1.2)
	pylab.ylim(-0.2,1.2)	
	pylab.subplots_adjust(bottom=0.12,left=0.12)
	pylab.savefig('scheme.svg')

#########################################################################
def spikecorr_tri_conv(filename,bin=5.,maxtime=10000.,start=100.,path='./'):
	data = numpy.loadtxt(path+filename)
	data = data[data[:,0]>start,:]
	z1 = pylab.histogram(data[data[:,1]==0.,0],numpy.arange(0,maxtime+0.1,0.1))
	z2 = pylab.histogram(data[data[:,1]==1.,0],numpy.arange(0,maxtime+0.1,0.1))
	x1 = miscfunc.tri_convolve(z1[0],bin*10)
	x2 = miscfunc.tri_convolve(z2[0],bin*10)
	cor = miscfunc.corrcoef(x1,x2)
	return cor

def spikecorr_tri_conv5(filename,bin=5.,maxtime=10000.,path='./'):
	data = numpy.loadtxt(path+filename)
	cor5 = []
	for j in range(5):
		z1 = pylab.histogram(data[data[:,1]==0.,0],numpy.arange(j*maxtime/5.,(j+1)*maxtime/5.+0.1,0.1))
		z2 = pylab.histogram(data[data[:,1]==1.,0],numpy.arange(j*maxtime/5.,(j+1)*maxtime/5.+0.1,0.1))
		x1 = miscfunc.tri_convolve(z1[0],bin*10)
		x2 = miscfunc.tri_convolve(z2[0],bin*10)
		cor5.append(miscfunc.corrcoef(x1,x2))
	cor = pylab.mean(cor5)
	sc = pylab.std(cor5)
	return cor,sc

def rate(filename,start=100.,dur=10000.,num=2,path='./'):
        data = numpy.loadtxt(path+filename)
	data = data[data[:,0]>start,0]
        if data.size > 0:
                r = data.size/(num*(dur-start)/1000.)
        else:
                r = 0.
        return r

def mpcorr_nospk5(filename,maxtime=10000.,pre=0.,post=50.,path='./'):
	data = numpy.loadtxt(path+'v'+filename)
	cor5 = []
	f = open(path+filename,'r')
	f.readline()
	f.readline()
	f.readline()
	f.readline()
	if f.readline() != '':
		datasp = numpy.loadtxt(path+filename)
		issubth = numpy.ones(data[:,1].size,dtype=bool)
		for j in range(datasp.size/2):
			if datasp.size == 2:
				id0 = numpy.argmin((data[:,1]-(datasp[j]-pre))**2)
			else:
				id0 = numpy.argmin((data[:,1]-(datasp[j,0]-pre))**2)
			issubth[id0:id0+2*int((pre+post)/0.1)] = 0  # if stepsize = 0.1
	for j in range(5):
		mp = data[(data[:,1]>=j*maxtime/5.)*(data[:,1]<(j+1)*maxtime/5.),0:3:2]
		mp = mp[issubth[j*maxtime*10/5.:(j+1)*maxtime*10/5.],:]
		cor5.append(miscfunc.corrcoef(mp[mp[:,0]==1,1],mp[mp[:,0]==2,1]))
	cor = pylab.mean(cor5)
	sc = pylab.std(cor5)
	return cor,sc
