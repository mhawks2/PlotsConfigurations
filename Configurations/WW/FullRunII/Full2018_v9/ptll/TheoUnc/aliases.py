import os
import copy
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # TheoUnc
configurations = os.path.dirname(configurations) # ptll
configurations = os.path.dirname(configurations) # Full2018_v9
configurations = os.path.dirname(configurations) # FullRunII_UL
configurations = os.path.dirname(configurations) # WW
configurations = os.path.dirname(configurations) # Configurations

#aliases = {}

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

aliases['genptll'] = {
    'linesToAdd': ['.L %s/WW/FullRunII/Tools/ptll.cc+' % configurations],
    'class': 'PTLL',
    'samples': ['WW','ggWW']
}

aliases['B0'] = {
    'expr' : 'genptll > 30. && genptll <= 35.',
    'samples' : ['WW','ggWW']
}

aliases['B1'] = {
    'expr' : 'genptll > 35. && genptll <= 40.',
    'samples' : ['WW','ggWW']
}

aliases['B2'] = {
    'expr' : 'genptll > 40. && genptll <= 45.',
    'samples' : ['WW','ggWW']
}

aliases['B3'] = {
    'expr' : 'genptll > 45. && genptll <= 50.',
    'samples' : ['WW','ggWW']
}

aliases['B4'] = {
    'expr' : 'genptll > 50. && genptll <= 55.',
    'samples' : ['WW','ggWW']
}

aliases['B5'] = {
    'expr' : 'genptll > 55. && genptll <= 60.',
    'samples' : ['WW','ggWW']
}

aliases['B6'] = {
    'expr' : 'genptll > 60. && genptll <= 70.',
    'samples' : ['WW','ggWW']
}

aliases['B7'] = {
    'expr' : 'genptll > 70. && genptll <= 80.',
    'samples' : ['WW','ggWW']
}

aliases['B8'] = {
    'expr' : 'genptll > 80. && genptll <= 100.',
    'samples' : ['WW','ggWW']
}

aliases['B9'] = {
    'expr' : 'genptll > 100.',
    'samples' : ['WW','ggWW']
}

aliases['fid'] = {
    'expr' : 'fiducial',
    'samples' : ['WW','ggWW']
}
