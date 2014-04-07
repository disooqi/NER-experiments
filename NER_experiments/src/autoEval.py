'''
Created on Dec 17, 2013

@author: meldesouki
'''
import feature_generation as fg
import NER_CRF_eval as CRFeval
import os
import sys
import subprocess


filepath = r'datasets\00_ANERCorp_original'
def ff():
    ##crf_learn template_file train_file model_file
    try:
        subprocess.check_call(['crf_learn', config.NERmodel,
                               os.path.join(config.getWorkingDir(), 'features'),
                               '-o', os.path.join(config.getWorkingDir(), 'featurestagged')],
                               shell=True)
    except subprocess.CalledProcessError as CPerror:
        logging.exception('Problem with crf++ command: %s', CPerror)
        raise
    else:
        logging.debug("-> CRF++ Tagging .... Done!")
def run_CRFplusplusTester():
    exitcode = subprocess.call(['crf_test', '--version'], shell=True)
    if exitcode != 4294967295:
        logging.critical('crf++ is not installed')
        raise errors.CRFplusplusConfigError('exit code '+str(exitcode)+':crf++ is not installed')
    if not os.path.isfile(config.NERmodel):
        logging.critical('The model file is missing in the following path "%s" please edit the path in the NER config file '+
                         'or put the model in the specified path', config.NERmodel)
        raise errors.CRFplusplusConfigError('the model file is missing')
    if not os.path.isfile(os.path.join(config.getWorkingDir(), 'features')):
        logging.critical('"features" file doesn\'t exist in the following path: "%s"', os.path.join(config.getWorkingDir(), 'features'))
        raise errors.CRFplusplusConfigError('The "features" file is not there')

    try:
        subprocess.check_call(['crf_test', '-m', config.NERmodel,
                               os.path.join(config.getWorkingDir(), 'features'),
                               '-o', os.path.join(config.getWorkingDir(), 'featurestagged')],
                               shell=True)
    except subprocess.CalledProcessError as CPerror:
        logging.exception('Problem with crf++ command: %s', CPerror)
        raise
    else:
        logging.debug("-> CRF++ Tagging .... Done!")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        filepath = sys.argv[1]
        
    #generate features
    fg.generateFeaturesForTrainingAndTesting(filepath)
        
    ##train the model
    run_CRFplusplusTrainer()
    run_CRFplusplusTester()
    CRFeval.evaluate_model(outputpath)
    
    
    
    