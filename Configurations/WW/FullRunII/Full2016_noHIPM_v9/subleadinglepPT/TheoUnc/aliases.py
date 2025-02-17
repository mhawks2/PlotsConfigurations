import os
import copy
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # TheoUnc
configurations = os.path.dirname(configurations) # subleadinglepPT
configurations = os.path.dirname(configurations) # Full2016_noHIPM_v9
configurations = os.path.dirname(configurations) # FullRunII
configurations = os.path.dirname(configurations) # WW
configurations = os.path.dirname(configurations) # Configurations

aliases['nCleanGenJet'] = {
    'linesToAdd': ['.L %s/Differential/ngenjet.cc+' % configurations],
    'class': 'CountGenJet',
}

aliases['fiducial'] = {
    'linesToAdd': ['.L %s/WW/FullRunII/fiducial.cc+' % configurations],
    'class': 'FiducialRegion',
    'samples': ['WW','ggWW']
}

aliases['nGoodGenJet'] = {
    'linesToAdd': ['.L %s/WW/FullRunII/goodgenjet.cc+' % configurations],
    'class': 'CleanGenJet',
    'args': ("njet"),
    'samples': ['WW','ggWW']
}

aliases['B0'] = {
    'expr' : 'DressedLepton_pt[1] > 20. && DressedLepton_pt[1] <= 30',
    'samples' : ['WW','ggWW']
}

aliases['B1'] = {
    'expr' : 'DressedLepton_pt[1] > 30. && DressedLepton_pt[1] <= 35.',
    'samples' : ['WW','ggWW']
}

aliases['B2'] = {
    'expr' : 'DressedLepton_pt[1] > 35. && DressedLepton_pt[1] <= 40.',
    'samples' : ['WW','ggWW']
}

aliases['B3'] = {
    'expr' : 'DressedLepton_pt[1] > 40. && DressedLepton_pt[1] <= 45.',
    'samples' : ['WW','ggWW']
}

aliases['B4'] = {
    'expr' : 'DressedLepton_pt[1] > 45. && DressedLepton_pt[1] <= 50.',
    'samples' : ['WW','ggWW']
}

aliases['B5'] = {
    'expr' : 'DressedLepton_pt[1] > 50. && DressedLepton_pt[1] <= 60.',
    'samples' : ['WW','ggWW']
}

aliases['B6'] = {
    'expr' : 'DressedLepton_pt[1] > 60.',
    'samples' : ['WW','ggWW']
}

aliases['fid'] = {
    'expr' : 'fiducial',
    'samples' : ['WW','ggWW']
}

