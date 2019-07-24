# structure configuration for datacard

#structure = {}

# keys here must match keys in samples.py    
#                    
structure['DY']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }

structure['Wjets']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }

structure['VgS'] = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }

structure['Fake']  = {  
                  'isSignal' : 0,
                  'isData'   : 0 
              }

structure['Fake_em']  = {  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'removeFromCuts' : [ k for k in cuts if 'me' in k],
              }

structure['Fake_me']  = {  
                  'isSignal' : 0,
                  'isData'   : 0,
                  'removeFromCuts' : [ k for k in cuts if 'em' in k],
              }

structure['top'] = {   
                  'isSignal' : 0,
                  'isData'   : 0 
                  }


structure['WW']  = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['ggWW']  = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }

structure['Vg']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }


structure['WZgS']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }



structure['VZ']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }

structure['WZ']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }


structure['VVV']  = { 
                  'isSignal' : 0,
                  'isData'   : 0 
                  }


structure['Higgs'] = {
                  'isSignal' : 0,
                  'isData'   : 0    
                  }


structure['ggH_hww']  = {  
                  'isSignal' : 1,
                  'isData'   : 0 
              }

structure['qqH_hww']  = {  
                  'isSignal' : 1,
                  'isData'   : 0 
              }

structure['ZH_hww']  = {  
                  'isSignal' : 1,
                  'isData'   : 0 
              }

structure['ggZH_hww']  = {  
                  'isSignal' : 1,
                  'isData'   : 0 
              }

structure['WH_hww']  = {  
                  'isSignal' : 1,
                  'isData'   : 0 
              }

structure['ttH_hww']  = {  
                  'isSignal' : 1,
                  'isData'   : 0 
              }

structure['H_htt']  = {  
                  'isSignal' : 1,
                  'isData'   : 0 
              }


# data

structure['DATA']  = { 
                  'isSignal' : 0,
                  'isData'   : 1 
              }
