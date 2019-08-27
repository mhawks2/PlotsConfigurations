# plot configuration



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
    'kPink'    : 900
}

#
groupPlot['VBS']  = {  
                 'nameHR' : 'VBS',
                 'isSignal' : 1,
                 'color': colors["kCyan"]+1,   
                 'samples'  : ['VBS']
              } 

groupPlot['DY']  = {  
                'nameHR' : "DY",
                'isSignal' : 0,
                'color': colors['kMagenta']+1,    # kGreen+2
                'samples'  : ['DY']
            }

groupPlot['QCD-VV']  = {  
                 'nameHR' : 'QCD-VV',
                 'isSignal' : 0,
                 'color':  colors['kGreen']+3,  
                 'samples'  : ['QCD-VV']
              }    


groupPlot['Wjets']  = {  
                  'nameHR' : 'W+Jets',
                  'isSignal' : 0,
                  'color': colors['kRed']-3,  
                  'samples'  : ['Wjets']
              }

groupPlot['top']  = {  
                 'nameHR' : 'top',
                 'isSignal' : 0,
                 'color':  colors['kAzure'],  
                 'samples'  : ['singleTop', 'ttbar']
             }







# groupPlot['WW']  = {  
#                   'nameHR' : 'WW',
#                   'isSignal' : 0,
#                   'color': 851, # kAzure -9 
#                   'samples'  : ['WW', 'ggWW', 'WWewk']
#               }

# groupPlot['Fake']  = {  
#                   'nameHR' : 'Non-prompt',
#                   'isSignal' : 0,
#                   'color': 921,    # kGray + 1
#                   'samples'  : ['Fake_em', 'Fake_me']
#               }



# groupPlot['VVV']  = {  
#                   'nameHR' : 'VVV',
#                   'isSignal' : 0,
#                   'color': 857, # kAzure -3  
#                   'samples'  : ['VVV']
#               }


# groupPlot['VZ']  = {  
#                   'nameHR' : "VZ",
#                   'isSignal' : 0,
#                   'color'    : 617,   # kViolet + 1  
#                   'samples'  : ['VZ', 'WZ', 'ZZ']
#               }

# groupPlot['Vg']  = {  
#                   'nameHR' : "V#gamma",
#                   'isSignal' : 0,
#                   'color'    : 810,   # kOrange + 10
#                   'samples'  : ['Vg', 'Wg']
#               }

# groupPlot['VgS']  = {
#                   'nameHR' : "V#gamma*",
#                   'isSignal' : 0,
#                   'color'    : 409,   # kGreen - 9
#                   'samples'  : ['VgS']
#               }





#plot = {}

# keys here must match keys in samples.py    
# 

plot['VBS']  = {
                  'color': colors["kCyan"]+1, 
                  'isSignal' : 1,
                  'isData'   : 0,
                  'scale'    : 1.   ,
              }

plot['QCD-VV']  = {
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



plot['singleTop'] = {   
                 'nameHR' : 'singleTop',
                 'color': colors['kAzure']+1,   
                 'isSignal' : 0,
                 'isData'   : 0, 
                 'scale'    : 1.0,
                 }

plot['ttbar'] = {   
                 'nameHR' : 'ttbar',
                 'color': colors['kAzure']-1,
                 'isSignal' : 0,
                 'isData'   : 0, 
                 'scale'    : 1.0,
                 }


plot['Wjets']  = {
                  'color':  colors['kRed']-3,
                  'isSignal' : 0,
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

legend['lumi'] = 'L = 41.5/fb'

legend['sqrt'] = '#sqrt{s} = 13 TeV'



# plot['WW']  = {
#                   'color': 851, # kAzure -9 
#                   'isSignal' : 0,
#                   'isData'   : 0,    
#                   'scale'    : 1.0   # ele/mu trigger efficiency   datadriven
#                   }

# plot['ggWW']  = {
#                   'color': 850, # kAzure -10
#                   'isSignal' : 0,
#                   'isData'   : 0,    
#                   'scale'    : 1.0
#                   }

# plot['WWewk']  = {
#                   'color': 851, # kAzure -9 
#                   'isSignal' : 0,
#                   'isData'   : 0,
#                   'scale'    : 1.0   # ele/mu trigger efficiency   datadriven
#                   }


# plot['Vg']  = { 
#                   'color': 859, # kAzure -1  
#                   'isSignal' : 0,
#                   'isData'   : 0,
#                   'scale'    : 1.0
#                   }

# plot['VgS'] = { 
#                   'color'    : 617,   # kViolet + 1  
#                   'isSignal' : 0,
#                   'isData'   : 0,
#                   'scale'    : 1.0
#                   }

# plot['VZ']  = { 
#                   'color': 858, # kAzure -2  
#                   'isSignal' : 0,
#                   'isData'   : 0,
#                   'scale'    : 1.0
#                   }

# plot['VVV']  = { 
#                   'color': 857, # kAzure -3  
#                   'isSignal' : 0,
#                   'isData'   : 0,
#                   'scale'    : 1.0
#                   }
