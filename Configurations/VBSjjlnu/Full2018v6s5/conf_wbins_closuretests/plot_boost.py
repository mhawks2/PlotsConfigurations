# plot configuration

from ROOT import TColor
from itertools import product

# groupPlot = {}
# 
# Groups of samples to improve the plots.
# If not defined, normal plots is used

colors = {
    # https://root.cern.ch/doc/master/classTColor.html#C02
    'kWhite'   : 0,
    'kBlack'   : 1,
    'kGray'    : 920,
    'kRed'     : 632,
    'kGreen'   : 416,
    'kBlue'    : 600,
    'kYellow'  : 400,
    'kMagenta' : 616,
    'kCyan'    : 432,
    'kOrange'  : 800,
    'kSpring'  : 820,
    'kTeal'    : 840,
    'kAzure'   : 860,
    'kViolet'  : 880,
    'kPink'    : 900, 
}

palette = {
    "Orange": (242, 108, 13), #f26c0d  
    "Yellow": (247, 195, 7), #f7c307
    "LightBlue": (153, 204, 255), #99ccff
    "MediumBlue": (72, 145, 234),  #4891ea
    "MediumBlue2": (56, 145, 224),    #3891e0
    "DarkBlue": (8, 103, 136), #086788
    "Green": (47, 181, 85), #2fb555
    "Green2": (55, 183, 76),  #37b74c
    "LightGreen" : (82, 221, 135), #52dd87
    "Violet": (242, 67, 114), #f24372  
     "Pink": (247, 191, 223)
}



wjets_palette = ['#FFC400','#FFEA00',]

wjets_bins = [ "Wjets_boost2","Wjets_boost1"]

for icw, wjetbin in enumerate(wjets_bins):
    color = wjets_palette[icw]
    palette[wjetbin] = color




groupPlot['Fake']  = {  
                'nameHR' : "Non-prompt",
                'isSignal' : 0,
                'color': palette["LightBlue"],   
                'samples'  : ['Fake'],
                'fill': 1001
            }


groupPlot['DY']  = {  
                'nameHR' : "DY",
                'isSignal' : 0,
                'color': palette["Green2"],    
                'samples'  : ['DY'],
                'fill': 1001
            }


groupPlot['vbfV+VV+VVV']  = {  
                  'nameHR' : 'vbfV+VV+VVV',
                  'isSignal' : 0,
                  'color': palette["Pink"],  
                  'samples'  : ['VBF-V','VVV', 'VV'],
                  'fill': 1001
              }




for wjetbin in wjets_bins:
    groupPlot[wjetbin]  = {  
                    'nameHR' : wjetbin,
                    'isSignal' : 0,
                    'color':   palette[wjetbin],
                    'samples'  : [wjetbin],
                    'fill': 1001
            }



groupPlot['top']  = {  
                 'nameHR' : 'top',
                 'isSignal' : 0,
                 'color':  palette["MediumBlue2"],  
                 'samples'  : ['top'],
                 'fill': 1001
             }



groupPlot['VBS']  = {  
                 'nameHR' : 'VBS',
                 'isSignal' : 1,
                 'color': colors["kRed"]+1,   
                 'samples'  : ['VBS'],
                 'fill': 1001
              }



#plot = {}

# keys here must match keys in samples.py    
# 

plot['VVV']  = { 
                  'color': colors["kAzure"] -3,    
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.0
                  }


plot['VV']  = {
                  'color': colors['kGreen']+3,  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.   ,
              }   
         


plot['DY']  = {  
                'color': colors['kMagenta']+1,
                'isSignal' : 0,
                'isData'   : 0, 
                'scale'    : 1.0,
            }

plot['VBF-V']  = {
                  'color': colors['kYellow']+3,  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'scale'    : 1.   ,
              }


plot['Fake']  = {  
                'color': colors['kTeal'],
                'isSignal' : 0,
                'isData'   : 0, 
                'scale'    : 1.0,
            }


plot['top'] = {   
                 'color': colors['kAzure']-1,
                 'isSignal' : 0,
                 'isData'   : 0, 
                 'scale'    : 1.0 #1.08
                 }


wfactors_ele = {
  "Wjets_deta1_jpt1": 1.03 ,
  "Wjets_deta2_jpt1": 1.33 ,
  "Wjets_deta1_jpt2": 0.92 ,
  "Wjets_deta2_jpt2": 1.14 ,
  "Wjets_jpt3": 0.75,
  "Wjets_boost1": 0.58,
  "Wjets_boost2": 0.65,
}

wfactors_mu = {
  "Wjets_deta1_jpt1":  0.99,
  "Wjets_deta2_jpt1": 1.16,
  "Wjets_deta1_jpt2": 0.80,
  "Wjets_deta2_jpt2": 0.92 ,
  "Wjets_jpt3": 0.52,
  "Wjets_boost1": 0.43,
  "Wjets_boost2": 0.60 
}

for wjetbin in wjets_bins:
    plot[wjetbin] = {  
                    'color':  colors['kRed']-3,
                    'isSignal' : 0,
                    'isData'   : 0,
                    'cuts':
                    { cut: wfactors_ele[wjetbin] if "ele" in cut else wfactors_mu[wjetbin]  for cut in cuts  }
                }


plot['VBS']  = {
                  'color': colors["kCyan"]+1, 
                  'isSignal' : 1,
                  'isData'   : 0,
                  'scale'    : 1.   ,
              }

# # data

plot['DATA']  = { 
                 'nameHR' : 'Data',
                 'color': 1 ,  
                 'isSignal' : 0,
                 'isData'   : 1 ,
                 'isBlind'  : 0
             }



# additional options

legend['lumi'] = 'L = 59.74/fb'
legend['sqrt'] = '#sqrt{s} = 13 TeV'


