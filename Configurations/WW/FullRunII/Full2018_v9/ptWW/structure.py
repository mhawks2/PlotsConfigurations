# structure configuration for datacard
# keys here must match keys in samples.py    
structure ={}

# keys here must match keys in samples.py 
for iproc in samples.keys():
    structure[iproc] = {
        'isSignal' : 1 if 'WW_B' in iproc else 0,
        'isData'   : 1 if iproc == 'DATA' else 0,
    }
'''
structure['Vg']['removeFromCuts'] = ['ww2l2v_13TeV_sr_2j_B1']
structure['WW_B0']['removeFromCuts'] = ['ww2l2v_13TeV_sr_2j_B8']
structure['ggWW_B3']['removeFromCuts'] = ['ww2l2v_13TeV_sr_2j_B8']
structure['WW_B8']['removeFromCuts'] = ['ww2l2v_13TeV_sr_1j_B3', 'ww2l2v_13TeV_sr_1j_B0', 'ww2l2v_13TeV_sr_1j_B1', 'ww2l2v_13TeV_sr_0j_B5', 'ww2l2v_13TeV_sr_0j_B4', 'ww2l2v_13TeV_sr_0j_B3', 'ww2l2v_13TeV_sr_0j_B2', 'ww2l2v_13TeV_sr_0j_B1', 'ww2l2v_13TeV_sr_0j_B0', 'ww2l2v_13TeV_sr_2j_B1', 'ww2l2v_13TeV_sr_2j_B0', 'ww2l2v_13TeV_sr_2j_B3']
structure['WW_B1']['removeFromCuts'] = ['ww2l2v_13TeV_sr_2j_B8']
structure['WW_B2']['removeFromCuts'] = ['ww2l2v_13TeV_sr_0j_B8', 'ww2l2v_13TeV_sr_2j_B8']
structure['WW_B3']['removeFromCuts'] = ['ww2l2v_13TeV_sr_0j_B8']
structure['ggWW_B8']['removeFromCuts'] = ['ww2l2v_13TeV_sr_1j_B1', 'ww2l2v_13TeV_sr_0j_B3', 'ww2l2v_13TeV_sr_0j_B1', 'ww2l2v_13TeV_sr_2j_B1', 'ww2l2v_13TeV_sr_2j_B0']
structure['Fake_me']['removeFromCuts'] = ['ww2l2v_13TeV_sr_2j_B2']
'''

for nuis in nuisances.itervalues():
  if 'cutspost' in nuis:
    nuis['cuts'] = nuis['cutspost'](nuis, cuts)

    print nuis
