import os
import inspect

# /afs/cern.ch/user/n/ntrevisa/work/latinos/unblinding/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/WH_chargeAsymmetry/UL/Full2017_v9/WH3l

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # WH3l
configurations = os.path.dirname(configurations) # Full2017_v9
configurations = os.path.dirname(configurations) # UL
configurations = os.path.dirname(configurations) # WH_chargeAsymmetry
configurations = os.path.dirname(configurations) # ControlRegions
configurations = os.path.dirname(configurations) # Configurations

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, sample):
    try:
        if _samples_noload:
            return []
    except NameError:
        pass

    return getSampleFiles(inputDir, sample, True, 'nanoLatino_')

# samples

try:
    len(samples)
except NameError:
    import collections
    samples = collections.OrderedDict()

################################################
################# SKIMS ########################
################################################

# MC:   /eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Summer20UL17_106x_nAODv9_Full2017v9/MCl1loose2017v9__MCCorr2017v9NoJERInHorn__l2tightOR2017v9/
# DATA: /eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2017_UL2017_nAODv9_Full2017v9/DATAl1loose2017v9__l2loose__l2tightOR2017v9/
# FAKE: /eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano/Run2017_UL2017_nAODv9_Full2017v9/DATAl1loose2017v9__l2loose__fakeW/

mcProduction = 'Summer20UL17_106x_nAODv9_Full2017v9'

dataReco     = 'Run2017_UL2017_nAODv9_Full2017v9'

mcSteps      = 'MCl1loose2017v9__MCCorr2017v9NoJERInHorn__l2tightOR2017v9'

fakeSteps    = 'DATAl1loose2017v9__l2loose__fakeW'

dataSteps    = 'DATAl1loose2017v9__l2loose__l2tightOR2017v9'

# embedReco  = 'Embedding2016_102X_nAODv7_Full2016v7'
# embedSteps = 'DATAl1loose2016v7__l2loose__l2tightOR2016v7__Embedding'

##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
elif  'cern' in SITE:
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'

def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))

mcDirectory = makeMCDirectory()
fakeDirectory = os.path.join(treeBaseDir, dataReco, fakeSteps)
dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)

# embedDirectory = os.path.join(treeBaseDir, embedReco, embedSteps)

################################################
############ DATA DECLARATION ##################
################################################

DataRun = [
    ['B','Run2017B-UL2017-v1'],
    ['C','Run2017C-UL2017-v1'],
    ['D','Run2017D-UL2017-v1'],
    ['E','Run2017E-UL2017-v1'],
    ['F','Run2017F-UL2017-v1'],
]

DataSets = ['MuonEG','SingleMuon','SingleElectron','DoubleMuon', 'DoubleEG']

DataTrig = {
    'MuonEG'         : ' Trigger_ElMu' ,
    'SingleMuon'     : '!Trigger_ElMu && Trigger_sngMu' ,
    'SingleElectron' : '!Trigger_ElMu && !Trigger_sngMu && Trigger_sngEl',
    'DoubleMuon'     : '!Trigger_ElMu && !Trigger_sngMu && !Trigger_sngEl && Trigger_dblMu',
    'DoubleEG'       : '!Trigger_ElMu && !Trigger_sngMu && !Trigger_sngEl && !Trigger_dblMu && Trigger_dblEl'
}

#########################################
############ MC COMMON ##################
#########################################

# SFweight does not include btag weights
mcCommonWeight = 'XSWeight*SFweight*METFilter_MC'
mcCommonWeightMatched = 'XSWeight*SFweight*PromptGenLepMatch3l*METFilter_MC'

###########################################
#############  BACKGROUNDS  ###############
###########################################

##### Top #######

files = nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu') + \
        nanoGetSampleFiles(mcDirectory, 'ST_s-channel') + \
        nanoGetSampleFiles(mcDirectory, 'ST_t-channel_top') + \
        nanoGetSampleFiles(mcDirectory, 'ST_t-channel_antitop') + \
        nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop') + \
        nanoGetSampleFiles(mcDirectory, 'ST_tW_top')

samples['top'] = {
    'name': files,
    'weight': mcCommonWeightMatched,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 1,
}

addSampleWeight(samples,'top','TTTo2L2Nu','Top_pTrw')


###### WW ########

samples['WW'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WWTo2L2Nu'),
    'weight': mcCommonWeightMatched + '*nllW*ewknloW', 
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 1
}

# samples['WWewk'] = {
#     'name': nanoGetSampleFiles(mcDirectory, 'WpWmJJ_EWK_noTop'),
#     'weight': mcCommonWeightMatched + '*(Sum$(abs(GenPart_pdgId)==6 || GenPart_pdgId==25)==0)',
#     'FilesPerJob': 4
# }

# files = nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENEN') + \
#         nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENMN') + \
#         nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENTN') + \
#         nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNEN') + \
#         nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNMN') + \
#         nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNTN') + \
#         nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNEN') + \
#         nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNMN') + \
#         nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNTN')

# samples['ggWW'] = {
#     'name': files,
#     'weight': mcCommonWeightMatched + '*1.53/1.4', # updating k-factor <-- do we still need the k-factor?
#     'FilesPerJob': 4
# }


######## Wg ########

files = nanoGetSampleFiles(mcDirectory, 'WGToLNuG') # same sample as v7 - OK!

samples['Wg'] = {
    'name': files,
    'weight': mcCommonWeight + '*(Gen_ZGstar_mass <= 0)',
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4
}

######## Zg ########

files = nanoGetSampleFiles(mcDirectory, 'ZGToLLG') # Same sample as v7 - OK!

samples['Zg'] = {
    'name': files,
    'weight': mcCommonWeight + '*(Gen_ZGstar_mass <= 0)',
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4
}

######## WgS ######## 

files = nanoGetSampleFiles(mcDirectory, 'WGToLNuG') + \
        nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin4p0') # WZTo3LNu_mllmin0p1

samples['WgS'] = {
    'name': files,
    'weight': mcCommonWeightMatched + ' * (gstarLow * 0.94)',
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4,
}
addSampleWeight(samples, 'WgS', 'WGToLNuG', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass <= 0.1)')
addSampleWeight(samples, 'WgS', 'WZTo3LNu_mllmin4p0', '(Gen_ZGstar_mass > 0.1)')


######## ZgS ########

files = nanoGetSampleFiles(mcDirectory, 'ZGToLLG')

samples['ZgS'] = {
    'name': files,
    'weight': mcCommonWeightMatched,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4,
}
addSampleWeight(samples, 'ZgS', 'ZGToLLG', '(Gen_ZGstar_mass > 0)*0.448') # Do we still need this normalization factor?


############ ZZ ############

samples['ZZ'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'ZZTo4L'),
    'weight': mcCommonWeightMatched,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4
}


############ WZ ############

samples['WZ'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin4p0'), # WZTo3LNu_mllmin0p1
    'weight': mcCommonWeightMatched + ' * (gstarHigh)',
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4
}
#addSampleWeight(samples, 'WZ', 'WZTo3LNu_mllmin4p0', '(0.601644*58.59/4.666)')

########## VVV #########

files = nanoGetSampleFiles(mcDirectory, 'ZZZ') + \
        nanoGetSampleFiles(mcDirectory, 'WZZ') + \
        nanoGetSampleFiles(mcDirectory, 'WWZ') + \
        nanoGetSampleFiles(mcDirectory, 'WWW')

samples['VVV'] = {
    'name': files,
    'weight': mcCommonWeight,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4
}

###########################################
#############   SIGNALS  ##################
###########################################

signals = []

#### ggH -> WW

samples['ggH_hww'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'GluGluHToWWTo2L2Nu_M125_Powheg'),
    'weight': mcCommonWeight,
    'FilesPerJob': 1
}

signals.append('ggH_hww')

############ VBF H->WW ############
samples['qqH_hww'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBFHToWWTo2L2Nu_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

signals.append('qqH_hww')

############ ZH H->WW ############

samples['ZH_hww'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'HZJ_HToWWTo2L2Nu_ZTo2L_M125'), # is it ok for 3l final state?
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

signals.append('ZH_hww')

samples['ggZH_hww'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'GluGluZH_HToWWTo2L2Nu_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

signals.append('ggZH_hww')

############ WH H->WW ############

samples['WH_hww_plus'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'HWplusJ_HToWW_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

signals.append('WH_hww_plus')


samples['WH_hww_minus'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'HWminusJ_HToWW_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

signals.append('WH_hww_minus')

############ ttH ############

samples['ttH_hww'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'ttHToNonbb_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 1
}

signals.append('ttH_hww')

############ H->TauTau ############

samples['ggH_htt'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'GluGluHToTauTau_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 20
}

signals.append('ggH_htt')

samples['qqH_htt'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBFHToTauTau_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 10
}

signals.append('qqH_htt')

samples['ZH_htt'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'ZHToTauTau_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

signals.append('ZH_htt')

############ WH H->TauTau ############

samples['WH_htt_plus'] = {
    'name':  nanoGetSampleFiles(mcDirectory, 'WplusHToTauTau_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

signals.append('WH_htt_plus')

samples['WH_htt_minus'] = {
    'name':  nanoGetSampleFiles(mcDirectory, 'WminusHToTauTau_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

signals.append('WH_htt_minus')


###########################################
################## FAKE ###################
###########################################

samples['Fake'] = {
    'name': [],
    'weight': 'METFilter_DATA*fakeW',
    'weights': [],
    'isData': ['all'],
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 50
}

for _, sd in DataRun:
  for pd in DataSets:

    tag = pd + '_' + sd

    files = nanoGetSampleFiles(fakeDirectory, tag)

    samples['Fake']['name'].extend(files)
    samples['Fake']['weights'].extend([DataTrig[pd]] * len(files))

###########################################
################## DATA ###################
###########################################

samples['DATA'] = {
  'name': [],
  'weight': 'LepWPCut*METFilter_DATA',
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 50
}

for _, sd in DataRun:
  for pd in DataSets:

    tag = pd + '_' + sd

    files = nanoGetSampleFiles(dataDirectory, tag)

    samples['DATA']['name'].extend(files)
    samples['DATA']['weights'].extend([DataTrig[pd]] * len(files))
