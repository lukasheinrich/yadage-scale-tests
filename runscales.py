import os
import yadage.steering_api
import logging
import time
import shutil
import json

logging.basicConfig(level = logging.ERROR)
def main():
	timingdata = []
	for npar in range(1000,1001):
		print(npar)
		workdir  = os.path.join(os.getcwd(),'workdir')
		if os.path.exists(workdir):
			shutil.rmtree(workdir)
		start = time.time()
		yadage.steering_api.run_workflow(
			workdir,'workflow.yml',
			toplevel = 'workflows/mapreduce_parmount',
			initdata = {'input': range(npar)},
			visualize = False)	
		end = time.time()
		duration = end-start
		nnodes = len(json.load(open('workdir/_yadage/yadage_snapshot_workflow.json'))['dag']['nodes'])

		timingdata.append({'npar': npar, 'duration': duration, 'nnodes': nnodes})
		print('{} seconds'.format(end-start))
	json.dump(timingdata,open('timing.json','w'))
if __name__ == '__main__':
	main()