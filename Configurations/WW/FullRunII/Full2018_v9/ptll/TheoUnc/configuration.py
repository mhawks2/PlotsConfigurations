# Configuration file to get normalizations of WW theoretical uncertainties

treeName = 'Events'

tag = 'WW2018_v9_ptll_TheoUnc'

# used by mkShape to define output directory for root files
outputDir = 'rootFile'

# file with TTree aliases
aliasesFile = 'aliases.py'

# file with list of variables
variablesFile = 'variables.py'

# file with list of cuts
cutsFile = 'cuts.py' 

# file with list of samples
samplesFile = 'samples.py' 

# luminosity to normalize to (in 1/fb)
lumi = 59.74

# nuisances file for mkDatacards and for mkShape
nuisancesFile = 'nuisances.py'
