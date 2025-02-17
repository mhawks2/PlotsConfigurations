import os
import subprocess

global getSampleFiles
from LatinoAnalysis.Tools.commonTools import getSampleFiles, addSampleWeight, getBaseWnAOD
def getSampleFilesNano(inputDir,Sample,absPath=False):
    return getSampleFiles(inputDir,Sample,absPath,'nanoLatino_')
##############################################
###### Tree Directory according to site ######
##############################################

SITE=os.uname()[1]
xrootdPath=''
if    'iihe' in SITE :
  xrootdPath  = 'dcap://maite.iihe.ac.be/'
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015/'
elif  'cern' in SITE :
  #xrootdPath='root://eoscms.cern.ch/'
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/'

directory = treeBaseDir+'Summer20UL16_106x_nAODv9_noHIPM_Full2016v9/MCl1loose2016v9__MCCorr2016v9NoJERInHorn__l2tightOR2016v9'

################################################
############ NUMBER OF LEPTONS #################
################################################

#Nlep='2'
Nlep='3'
#Nlep='4'
ZZWeight='1.07'
WZWeight = '1.138' # NLO to NNLO k-factor

################################################
############### Lepton WP ######################
################################################

eleWP='mvaFall17V2Iso_WP90'
muWP='cut_Tight80x'
eleWP_new = eleWP+'_tthmva_70'
muWP_new  = muWP+'_tthmva_80'

LepWPCut        = 'LepCut'+Nlep+'l__ele_'+eleWP_new+'__mu_'+muWP_new 
#LepWPCut        = 'LepCut'+Nlep+'l__ele_'+eleWP+'__mu_'+muWP
#LepWPweight     = 'ttHMVA_SF_3l[0]' #SF for new WPs, defined in aliases
LepWPweight     = 'LepSF'+Nlep+'l__ele_'+eleWP_new+'__mu_'+muWP_new

################################################
############ BASIC MC WEIGHTS ##################
################################################

XSWeight      = 'XSWeight'
SFweight      = 'SFweight'+Nlep+'l*'+LepWPweight+'*'+LepWPCut+'*PrefireWeight*Jet_PUIDSF'
PromptGenLepMatch   = 'PromptGenLepMatch'+Nlep+'l'
PromptGenLepMatch2l   = 'PromptGenLepMatch'+'2l'
PromptGenLepMatch3l   = 'PromptGenLepMatch'+'3l'

################################################
############## FAKE WEIGHTS ####################
################################################


if Nlep == '2' :
  fakeW = 'fakeW2l_ele_'+eleWP_new+'_mu_'+muWP_new
else:
  fakeW = 'fakeW_ele_'+eleWP_new+'_mu_'+muWP_new+'_'+Nlep+'l'

################################################
############### B-Tag  WP ######################
################################################

SFweight += '*btagSF' #define in aliases.py

################################################
############   MET  FILTERS  ###################
################################################

METFilter_MC   = 'METFilter_MC'
METFilter_DATA = 'METFilter_DATA'

################################################
############ DATA DECLARATION ##################
################################################

DataRun = [
    ['F','Run2016F-UL2016-v1'],
    ['G','Run2016G_UL2016-v1'],
    ['H','Run2016H_UL2016-v1'],
]

DataSets = ['MuonEG','SingleMuon','SingleElectron','DoubleMuon', 'DoubleEG']


DataTrig = {
       'MuonEG'         : ' Trigger_ElMu' ,
       'SingleMuon'     : '!Trigger_ElMu && Trigger_sngMu' ,
       'SingleElectron' : '!Trigger_ElMu && !Trigger_sngMu && Trigger_sngEl',
       'DoubleMuon'     : '!Trigger_ElMu && !Trigger_sngMu && !Trigger_sngEl && Trigger_dblMu',
       'DoubleEG'       : '!Trigger_ElMu && !Trigger_sngMu && !Trigger_sngEl && !Trigger_dblMu && Trigger_dblEl'
}

###########################################
#############  BACKGROUNDS  ###############
###########################################
samples['Zg']  =  {     'name'   :    getSampleFilesNano(directory,'ZGToLLG'),
                        'weight' : XSWeight+'*'+SFweight+'*'+METFilter_MC + '*(Gen_ZGstar_mass <= 0)',
                        'FilesPerJob' : 3 ,
                 }

samples['ZgS']  = {    'name'   :   getSampleFilesNano(directory,'ZGToLLG'),
                       'weight' : XSWeight+'*'+SFweight+'*'+PromptGenLepMatch3l+'*'+METFilter_MC+'*(Gen_ZGstar_mass > 0)',
                       'FilesPerJob' : 3 ,
                 }
samples['WZ']  = {    'name':   getSampleFilesNano(directory,'WZTo3LNu_mllmin4p0')
                              + getSampleFilesNano(directory,'WZTo2Q2L_mllmin4p0'),
                       'weight' : XSWeight+'*'+SFweight+'*'+PromptGenLepMatch3l+'*'+METFilter_MC+'*'+WZWeight,
                       'FilesPerJob' : 2 ,
             }

######### TTZToLLNuNu needs to be postprocessed #####################
#samples['ttZ'] = {    'name'   :   getSampleFilesNano(directory,'TTZToLLNuNu_M-10'), 
#                     'weight' : XSWeight+'*'+SFweight+'*'+PromptGenLepMatch+'*'+METFilter_MC ,
#                     'FilesPerJob' : 5,
#                 }
################## ttH ###############

samples['ttH_hww']  = { 'name'   :   getSampleFilesNano(directory,'ttHToNonbb_M125'),
                        'weight' : XSWeight+'*'+SFweight+'*'+PromptGenLepMatch+'*'+METFilter_MC ,
                      }


samples['tZq_ll']  = { 'name'   :   getSampleFilesNano(directory,'tZq_ll_4f'),
                       'weight' : XSWeight+'*'+SFweight+'*'+PromptGenLepMatch+'*'+METFilter_MC ,
                       'FilesPerJob' : 5,                 
}

############ VVV ############

samples['ZZ']  = {  'name'   :   getSampleFilesNano(directory,'ZZTo2L2Nu')
                               + getSampleFilesNano(directory,'ZZTo2Q2L_mllmin4p0')
                               + getSampleFilesNano(directory,'ZZTo4L'),    #check if ggZZ samples are there and add them
                    'weight' : XSWeight+'*'+SFweight+'*'+PromptGenLepMatch+'*'+METFilter_MC+'*'+ZZWeight,
                    'FilesPerJob' : 5,
             }


samples['VVV']  = {  'name'   :   getSampleFilesNano(directory,'ZZZ')
                                + getSampleFilesNano(directory,'WZZ')
                                + getSampleFilesNano(directory,'WWZ')
                                + getSampleFilesNano(directory,'WWW'),
                    'weight' : XSWeight+'*'+SFweight+'*'+PromptGenLepMatch+'*'+METFilter_MC ,
                  }


samples['top'] = {    'name'   :   getSampleFilesNano(directory,'TTTo2L2Nu') 
                                  + getSampleFilesNano(directory,'ST_s-channel')
                                  + getSampleFilesNano(directory,'ST_t-channel_antitop') 
                                  + getSampleFilesNano(directory,'ST_t-channel_top') 
                                  + getSampleFilesNano(directory,'ST_tW_antitop') 
                                  + getSampleFilesNano(directory,'ST_tW_top'),
                      'weight' : XSWeight+'*'+SFweight+'*'+PromptGenLepMatch+'*'+METFilter_MC ,
                      'FilesPerJob' : 5,
}

addSampleWeight(samples,'top','TTTo2L2Nu_PSWeights','Top_pTrw')

samples['TTWJets'] = { 'name': getSampleFilesNano(directory,'TTWJetsToLNu'),
                       'weight' : XSWeight+'*'+SFweight+'*'+PromptGenLepMatch+'*'+METFilter_MC ,
		       'FilesPerJob' : 5,
}

############ AZH SIGNAL SAMPLES ############
samples['AZH_800_600'] = {  'name':  getSampleFilesNano(directory,'AToZHToLLTTbar_MA-800_MH-600'),
                    'weight' : XSWeight+'*'+SFweight+'*'+PromptGenLepMatch3l+'*'+METFilter_MC ,
                  }

samples['AZH_1000_600'] = { 'name': getSampleFilesNano(directory,'AToZHToLLTTbar_MA-1000_MH-600'),
                     'weight' : XSWeight+'*'+SFweight+'*'+PromptGenLepMatch3l+'*'+METFilter_MC ,
                   }

#samples['AZH_1200_1000'] = { 'name': getSampleFilesNano(directory,'AToZHToLLTTbar_MA-1200_MH-1000'),
#                     'weight' : XSWeight+'*'+SFweight+'*'+PromptGenLepMatch3l+'*'+METFilter_MC ,
#}


#samples['AZH_1200_850'] = { 'name': getSampleFilesNano(directory,'AToZHToLLTTbar_MA-1200_MH-850'),
#                     'weight' : XSWeight+'*'+SFweight+'*'+PromptGenLepMatch3l+'*'+METFilter_MC ,
#}


samples['AZH_500_350'] = { 'name': getSampleFilesNano(directory,'AToZHToLLTTbar_MA-500_MH-350'),
                     'weight' : XSWeight+'*'+SFweight+'*'+PromptGenLepMatch3l+'*'+METFilter_MC ,
}


#samples['AZH_500_400'] = { 'name': getSampleFilesNano(directory,'AToZHToLLTTbar_MA-500_MH-400'),
#                     'weight' : XSWeight+'*'+SFweight+'*'+PromptGenLepMatch3l+'*'+METFilter_MC ,
#}


#samples['AZH_700_350'] = { 'name': getSampleFilesNano(directory,'AToZHToLLTTbar_MA-700_MH-350'),
#                     'weight' : XSWeight+'*'+SFweight+'*'+PromptGenLepMatch3l+'*'+METFilter_MC ,
#}

#samples['AZH_700_370'] = { 'name': getSampleFilesNano(directory,'AToZHToLLTTbar_MA-700_MH-370'),
#                     'weight' : XSWeight+'*'+SFweight+'*'+PromptGenLepMatch3l+'*'+METFilter_MC ,
#}

#samples['AZH_700_400'] = { 'name': getSampleFilesNano(directory,'AToZHToLLTTbar_MA-700_MH-400'),
#                     'weight' : XSWeight+'*'+SFweight+'*'+PromptGenLepMatch3l+'*'+METFilter_MC ,
#}

#samples['AZH_900_370'] = { 'name': getSampleFilesNano(directory,'AToZHToLLTTbar_MA-900_MH-370'),
#                     'weight' : XSWeight+'*'+SFweight+'*'+PromptGenLepMatch3l+'*'+METFilter_MC ,
#}

samples['AZH_900_400'] = { 'name': getSampleFilesNano(directory,'AToZHToLLTTbar_MA-900_MH-400'),
                     'weight' : XSWeight+'*'+SFweight+'*'+PromptGenLepMatch3l+'*'+METFilter_MC ,
}
################## FAKE ###################
###########################################
Fakedirectory = treeBaseDir+'Run2016_UL2016_nAODv9_noHIPM_Full2016v9/DATAl1loose2016v9__l2loose__fakeW'

samples['Fake']  = {   'name': [ ] ,
                       'weight' : fakeW+'*'+METFilter_DATA,
                       'weights' : [ ] ,
                       'isData': ['all'],
                       'FilesPerJob' : 500 ,
                       'suppressNegativeNuisances' :['all'],
                     }


for _, sd in DataRun:
  for pd in DataSets:
      tag = pd + '_' + sd

      if 'DoubleMuon' in pd and 'Run2016G' in sd: # Run2016B-ver2_HIPM_UL2016-v2
           print("sd      = {}".format(sd))
	   print("pd      = {}".format(pd))
	   print("Old tag = {}".format(tag))
	   tag = tag.replace('v1','v2')
	   print("New tag = {}".format(tag))



      FileTarget = getSampleFilesNano(Fakedirectory,tag)
      samples['Fake']['name'].extend(FileTarget)
      samples['Fake']['weights'].extend([DataTrig[pd]] * len(FileTarget))

###########################################
################## DATA ###################
###########################################
Datadirectory = treeBaseDir+'Run2016_UL2016_nAODv9_noHIPM_Full2016v9/DATAl1loose2016v9__l2loose__l2tightOR2016v9'
samples['DATA']  = {   'name': [ ] ,
                       'weight' : METFilter_DATA+'*'+LepWPCut,
                       'weights' : [ ],
                       'isData': ['all'],
                       'FilesPerJob' : 500 ,
                    }


for _, sd in DataRun:
  for pd in DataSets:
      tag = pd + '_' + sd

      if 'DoubleMuon' in pd and 'Run2016G' in sd:  # Run2016B-ver2_HIPM_UL2016-v2
          print("sd      = {}".format(sd))
	  print("pd      = {}".format(pd))
	  print("Old tag = {}".format(tag))
	  tag = tag.replace('v1','v2')
	  print("New tag = {}".format(tag))







      FileTarget = getSampleFilesNano(Datadirectory,tag)
      samples['DATA']['name'].extend(FileTarget)
      samples['DATA']['weights'].extend([DataTrig[pd]] * len(FileTarget))

