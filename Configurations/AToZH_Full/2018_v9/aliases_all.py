#Aliases (mostly btag)

mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]
bkg = [skey for skey in samples if not skey.startswith('AZH')]

eleWP_new = 'mvaFall17V2Iso_WP90_tthmva_70'
muWP_new  = 'cut_Tight_HWWW_tthmva_80'

####################################################################################
# b tagging WPs: https://twiki.cern.ch/twiki/bin/view/CMS/BtagRecommendation106XUL18
####################################################################################

# DeepB = DeepCSV
bWP_loose_deepB  = '0.1208'
bWP_medium_deepB = '0.4168' 
bWP_tight_deepB  = '0.7665'

# DeepFlavB = DeepJet
bWP_loose_deepFlavB  = '0.0490'
bWP_medium_deepFlavB = '0.2783'
bWP_tight_deepFlavB  = '0.7100'

# Actual algo and WP definition. BE CONSISTENT!!
bAlgo = 'DeepFlavB' # ['DeepB','DeepFlavB']
bWP   = bWP_medium_deepFlavB
bSF   = 'deepjet' # ['deepcsv','deepjet']

#######################################  b-tag definitions #######################

aliases['bVeto'] = {
        'expr': 'Sum$(CleanJet_pt > 20.0 && abs(CleanJet_eta) < 2.5 && Jet_btag{}[CleanJet_jetIdx] > {}) == 0'.format(bAlgo, bWP)
}

aliases['bVeto_1j'] = {
       'expr': '(Sum$(CleanJet_pt > 30.0 && abs(CleanJet_eta) < 2.5 && Jet_btag{}[CleanJet_jetIdx] > {}) == 1)'.format(bAlgo, bWP)
}

aliases['bReq'] = {
       'expr': '(Sum$(CleanJet_pt > 30.0 && abs(CleanJet_eta) < 2.5 && Jet_btag{}[CleanJet_jetIdx] > {}) >= 2)'. format(bAlgo, bWP)
}

####################################### b-tagging SFs ################################

aliases['bReqSF'] = {
     'expr': '(TMath::Exp(Sum$(TMath::Log((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_{}_shape[CleanJet_jetIdx]+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5)))))'.format(bSF),
     'samples': mc
}

aliases['bVetoSF'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_{}_shape[CleanJet_jetIdx]+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5))))'.format(bSF),
    'samples': mc
}

aliases['btagSF'] = {
    'expr': '((bVeto*bVetoSF) + ((bReq || bVeto_1j)*bReqSF))',
    'samples': mc
}


for syst in ['lf','hf','lfstats1','lfstats2','hfstats1','hfstats2','cferr1','cferr2']:
    for targ in ['bVeto', 'bReq']:
        alias = aliases['%sSF%sup' % (targ, syst)] = copy.deepcopy(aliases['%sSF' % targ])
        alias['expr'] = alias['expr'].replace('btagSF_{}_shape'.format(bSF), 'btagSF_{}_shape_up_{}'.format(bSF,syst))

        alias = aliases['%sSF%sdown' % (targ, syst)] = copy.deepcopy(aliases['%sSF' % targ])
        alias['expr'] = alias['expr'].replace('btagSF_{}_shape'.format(bSF), 'btagSF_{}_shape_down_{}'.format(bSF,syst))
         
    aliases['btagSF'+syst+'up']   = { 
        'expr': aliases['btagSF']['expr'].replace('shape','shape_up_'+syst),
        'samples':mc  
    }

    aliases['btagSF'+syst+'down'] = { 
        'expr': aliases['btagSF']['expr'].replace('shape','shape_down_'+syst),
        'samples':mc  
    }


aliases['Jet_PUIDSF'] = {
   'expr' : 'TMath::Exp(Sum$((Jet_jetId>=2)*TMath::Log(Jet_PUIDSF_loose)))',
   'samples': mc
}

aliases['Jet_PUIDSF_up'] = {
    'expr' : 'TMath::Exp(Sum$((Jet_jetId>=2)*TMath::Log(Jet_PUIDSF_loose_up)))',
    'samples': mc
}

aliases['Jet_PUIDSF_down'] = {
    'expr' : 'TMath::Exp(Sum$((Jet_jetId>=2)*TMath::Log(Jet_PUIDSF_loose_down)))',
    'samples': mc
}

aliases['PromptGenLepMatch2l'] = {
    'expr': 'Alt$(Lepton_promptgenmatched[0]*Lepton_promptgenmatched[1], 0)',
    'samples': mc
}

aliases['PromptGenLepMatch3l'] = {
    'expr': 'Alt$(Lepton_promptgenmatched[0]*Lepton_promptgenmatched[1]*Lepton_promptgenmatched[2], 0)',
    'samples': mc
}

aliases['PromptGenLepMatch4l'] = {
    'expr': 'Alt$(Lepton_promptgenmatched[0]*Lepton_promptgenmatched[1]*Lepton_promptgenmatched[2]*Lepton_promptgenmatched[3], 0)',
    'samples': mc
}

aliases['Top_pTrw'] = {
    'expr': '(topGenPt * antitopGenPt > 0.) * (TMath::Sqrt(TMath::Exp(0.0615 - 0.0005 * topGenPt) * TMath::Exp(0.0615 - 0.0005 * antitopGenPt))) + (topGenPt * antitopGenPt <= 0.)',
    'samples': ['top']
}

#################################### AZH variables ####################################################

aliases['AZH_mA_minus_mH_patch'] = {
    'linesToAdd': [
       '.L %s/src/PlotsConfigurations/Configurations/AToZH_Full/scripts/AZH_patch_2018.cc+' % os.getenv('CMSSW_BASE')
    ],
    'class': 'AZH_patch_2018',
    'args': ("AZH_mA_minus_mH"),
}

aliases['AZH_Amass'] = {
    'class': 'AZH_patch_2018',
    'args': ("AZH_Amass"),
    'samples': [skey for skey in samples if skey not in mc]
}

aliases['nbjet'] = {
    'class': 'AZH_patch_2018',
    'args': ("nbjet"),
}

aliases['AZH_Hmass'] = {
    'class': 'AZH_patch_2018',
    'args': ("AZH_Hmass"),
    'samples': [skey for skey in samples if skey not in mc]
}

aliases['AZH_ChiSquare'] = {
    'class': 'AZH_patch_2018',
    'args': ("AZH_ChiSquare"),
    'samples': [skey for skey in samples if skey not in mc]
}

aliases['AZH_Tophadronic'] = {
    'class': 'AZH_patch_2018',
    'args': ("AZH_Tophadronic")
}

aliases['AZH_mA_minus_mH_onebjet'] = {
    'class' : 'AZH_patch_2018',
    'args' : ("AZH_mA_minus_mH_onebjet")
}

############## ellipse variables ###############

aliases['ellipse_mA_1000_mH_330'] = {
    'linesToAdd' : ['.L %s/src/PlotsConfigurations/Configurations/AToZH_Full/scripts/elliptical_bin.cc+' % os.getenv('CMSSW_BASE')],
    'class' : 'elliptical_bin',
    'args'  : (1000,330,False),
    'samples' : bkg+['AZH_1000_330']
}

aliases['ellipse_mA_1000_mH_350'] = {
    'class' : 'elliptical_bin',
    'args'  : (1000,350,False),
    'samples' : bkg+['AZH_1000_350']
}

aliases['ellipse_mA_1000_mH_400'] = {
    'class' : 'elliptical_bin',
    'args'  : (1000,400,False),
    'samples' : bkg+['AZH_1000_400']
}

aliases['ellipse_mA_1000_mH_450'] = {
    'class' : 'elliptical_bin',
    'args'  : (1000,450,False),
    'samples' : bkg+['AZH_1000_450']
}

aliases['ellipse_mA_1000_mH_500'] = {
    'class' : 'elliptical_bin',
    'args'  : (1000,500,False),
    'samples' : bkg+['AZH_1000_500']
}

aliases['ellipse_mA_1000_mH_550'] = {
    'class' : 'elliptical_bin',
    'args'  : (1000,550,False),
    'samples' : bkg+['AZH_1000_550']
}

aliases['ellipse_mA_1000_mH_600'] = {
    'class' : 'elliptical_bin',
    'args'  : (1000,600,False),
    'samples' : bkg+['AZH_1000_600']
}

aliases['ellipse_mA_1000_mH_650'] = {
    'class' : 'elliptical_bin',
    'args'  : (1000,650,False),
    'samples' : bkg+['AZH_1000_650']
}

aliases['ellipse_mA_1000_mH_700'] = {
    'class' : 'elliptical_bin',
    'args'  : (1000,700,False),
    'samples' : bkg+['AZH_1000_700']
}

aliases['ellipse_mA_1000_mH_750'] = {
    'class' : 'elliptical_bin',
    'args'  : (1000,750,False),
    'samples' : bkg+['AZH_1000_750']
}

aliases['ellipse_mA_1000_mH_800'] = {
    'class' : 'elliptical_bin',
    'args'  : (1000,800,False),
    'samples' : bkg+['AZH_1000_800']
}

aliases['ellipse_mA_1000_mH_850'] = {
    'class' : 'elliptical_bin',
    'args'  : (1000,850,False),
    'samples' : bkg+['AZH_1000_850']
}

aliases['ellipse_mA_1000_mH_900'] = {
    'class' : 'elliptical_bin',
    'args'  : (1000,900,False),
    'samples' : bkg+['AZH_1000_900']
}

aliases['ellipse_mA_1050_mH_330'] = {
    'class' : 'elliptical_bin',
    'args'  : (1050,330,False),
    'samples' : bkg+['AZH_1050_330']
}

aliases['ellipse_mA_1050_mH_350'] = {
    'class' : 'elliptical_bin',
    'args'  : (1050,350,False),
    'samples' : bkg+['AZH_1050_350']
}

aliases['ellipse_mA_1050_mH_400'] = {
    'class' : 'elliptical_bin',
    'args'  : (1050,400,False),
    'samples' : bkg+['AZH_1050_400']
}

aliases['ellipse_mA_1050_mH_450'] = {
    'class' : 'elliptical_bin',
    'args'  : (1050,450,False),
    'samples' : bkg+['AZH_1050_450']
}

aliases['ellipse_mA_1050_mH_500'] = {
    'class' : 'elliptical_bin',
    'args'  : (1050,500,False),
    'samples' : bkg+['AZH_1050_500']
}

aliases['ellipse_mA_1050_mH_550'] = {
    'class' : 'elliptical_bin',
    'args'  : (1050,550,False),
    'samples' : bkg+['AZH_1050_550']
}

aliases['ellipse_mA_1050_mH_600'] = {
    'class' : 'elliptical_bin',
    'args'  : (1050,600,False),
    'samples' : bkg+['AZH_1050_600']
}

aliases['ellipse_mA_1050_mH_650'] = {
    'class' : 'elliptical_bin',
    'args'  : (1050,650,False),
    'samples' : bkg+['AZH_1050_650']
}

aliases['ellipse_mA_1050_mH_700'] = {
    'class' : 'elliptical_bin',
    'args'  : (1050,700,False),
    'samples' : bkg+['AZH_1050_700']
}

aliases['ellipse_mA_1050_mH_750'] = {
    'class' : 'elliptical_bin',
    'args'  : (1050,750,False),
    'samples' : bkg+['AZH_1050_750']
}

aliases['ellipse_mA_1050_mH_800'] = {
    'class' : 'elliptical_bin',
    'args'  : (1050,800,False),
    'samples' : bkg+['AZH_1050_800']
}

aliases['ellipse_mA_1050_mH_850'] = {
    'class' : 'elliptical_bin',
    'args'  : (1050,850,False),
    'samples' : bkg+['AZH_1050_850']
}

aliases['ellipse_mA_1050_mH_900'] = {
    'class' : 'elliptical_bin',
    'args'  : (1050,900,False),
    'samples' : bkg+['AZH_1050_900']
}

aliases['ellipse_mA_1050_mH_950'] = {
    'class' : 'elliptical_bin',
    'args'  : (1050,950,False),
    'samples' : bkg+['AZH_1050_950']
}

aliases['ellipse_mA_1100_mH_1000'] = {
    'class' : 'elliptical_bin',
    'args'  : (1100,1000,False),
    'samples' : bkg+['AZH_1100_1000']
}

aliases['ellipse_mA_1100_mH_330'] = {
    'class' : 'elliptical_bin',
    'args'  : (1100,330,False),
    'samples' : bkg+['AZH_1100_330']
}

aliases['ellipse_mA_1100_mH_350'] = {
    'class' : 'elliptical_bin',
    'args'  : (1100,350,False),
    'samples' : bkg+['AZH_1100_350']
}

aliases['ellipse_mA_1100_mH_400'] = {
    'class' : 'elliptical_bin',
    'args'  : (1100,400,False),
    'samples' : bkg+['AZH_1100_400']
}

aliases['ellipse_mA_1100_mH_450'] = {
    'class' : 'elliptical_bin',
    'args'  : (1100,450,False),
    'samples' : bkg+['AZH_1100_450']
}

aliases['ellipse_mA_1100_mH_500'] = {
    'class' : 'elliptical_bin',
    'args'  : (1100,500,False),
    'samples' : bkg+['AZH_1100_500']
}

aliases['ellipse_mA_1100_mH_550'] = {
    'class' : 'elliptical_bin',
    'args'  : (1100,550,False),
    'samples' : bkg+['AZH_1100_550']
}

aliases['ellipse_mA_1100_mH_600'] = {
    'class' : 'elliptical_bin',
    'args'  : (1100,600,False),
    'samples' : bkg+['AZH_1100_600']
}

aliases['ellipse_mA_1100_mH_650'] = {
    'class' : 'elliptical_bin',
    'args'  : (1100,650,False),
    'samples' : bkg+['AZH_1100_650']
}

aliases['ellipse_mA_1100_mH_700'] = {
    'class' : 'elliptical_bin',
    'args'  : (1100,700,False),
    'samples' : bkg+['AZH_1100_700']
}

aliases['ellipse_mA_1100_mH_750'] = {
    'class' : 'elliptical_bin',
    'args'  : (1100,750,False),
    'samples' : bkg+['AZH_1100_750']
}

aliases['ellipse_mA_1100_mH_800'] = {
    'class' : 'elliptical_bin',
    'args'  : (1100,800,False),
    'samples' : bkg+['AZH_1100_800']
}

aliases['ellipse_mA_1100_mH_850'] = {
    'class' : 'elliptical_bin',
    'args'  : (1100,850,False),
    'samples' : bkg+['AZH_1100_850']
}

aliases['ellipse_mA_1100_mH_900'] = {
    'class' : 'elliptical_bin',
    'args'  : (1100,900,False),
    'samples' : bkg+['AZH_1100_900']
}

aliases['ellipse_mA_1100_mH_950'] = {
    'class' : 'elliptical_bin',
    'args'  : (1100,950,False),
    'samples' : bkg+['AZH_1100_950']
}

aliases['ellipse_mA_1150_mH_1050'] = {
    'class' : 'elliptical_bin',
    'args'  : (1150,1050,False),
    'samples' : bkg+['AZH_1150_1050']
}

aliases['ellipse_mA_1150_mH_330'] = {
    'class' : 'elliptical_bin',
    'args'  : (1150,330,False),
    'samples' : bkg+['AZH_1150_330']
}

aliases['ellipse_mA_1150_mH_350'] = {
    'class' : 'elliptical_bin',
    'args'  : (1150,350,False),
    'samples' : bkg+['AZH_1150_350']
}

aliases['ellipse_mA_1150_mH_450'] = {
    'class' : 'elliptical_bin',
    'args'  : (1150,450,False),
    'samples' : bkg+['AZH_1150_450']
}

aliases['ellipse_mA_1150_mH_550'] = {
    'class' : 'elliptical_bin',
    'args'  : (1150,550,False),
    'samples' : bkg+['AZH_1150_550']
}

aliases['ellipse_mA_1150_mH_650'] = {
    'class' : 'elliptical_bin',
    'args'  : (1150,650,False),
    'samples' : bkg+['AZH_1150_650']
}

aliases['ellipse_mA_1150_mH_750'] = {
    'class' : 'elliptical_bin',
    'args'  : (1150,750,False),
    'samples' : bkg+['AZH_1150_750']
}

aliases['ellipse_mA_1150_mH_850'] = {
    'class' : 'elliptical_bin',
    'args'  : (1150,850,False),
    'samples' : bkg+['AZH_1150_850']
}

aliases['ellipse_mA_1150_mH_950'] = {
    'class' : 'elliptical_bin',
    'args'  : (1150,950,False),
    'samples' : bkg+['AZH_1150_950']
}

aliases['ellipse_mA_1200_mH_1000'] = {
    'class' : 'elliptical_bin',
    'args'  : (1200,1000,False),
    'samples' : bkg+['AZH_1200_1000']
}

aliases['ellipse_mA_1200_mH_1100'] = {
    'class' : 'elliptical_bin',
    'args'  : (1200,1100,False),
    'samples' : bkg+['AZH_1200_1100']
}

aliases['ellipse_mA_1200_mH_330'] = {
    'class' : 'elliptical_bin',
    'args'  : (1200,330,False),
    'samples' : bkg+['AZH_1200_330']
}

aliases['ellipse_mA_1200_mH_350'] = {
    'class' : 'elliptical_bin',
    'args'  : (1200,350,False),
    'samples' : bkg+['AZH_1200_350']
}

aliases['ellipse_mA_1200_mH_400'] = {
    'class' : 'elliptical_bin',
    'args'  : (1200,400,False),
    'samples' : bkg+['AZH_1200_400']
}

aliases['ellipse_mA_1200_mH_500'] = {
    'class' : 'elliptical_bin',
    'args'  : (1200,500,False),
    'samples' : bkg+['AZH_1200_500']
}

aliases['ellipse_mA_1200_mH_600'] = {
    'class' : 'elliptical_bin',
    'args'  : (1200,600,False),
    'samples' : bkg+['AZH_1200_600']
}

aliases['ellipse_mA_1200_mH_700'] = {
    'class' : 'elliptical_bin',
    'args'  : (1200,700,False),
    'samples' : bkg+['AZH_1200_700']
}

aliases['ellipse_mA_1200_mH_800'] = {
    'class' : 'elliptical_bin',
    'args'  : (1200,800,False),
    'samples' : bkg+['AZH_1200_800']
}

aliases['ellipse_mA_1200_mH_850'] = {
    'class' : 'elliptical_bin',
    'args'  : (1200,850,False),
    'samples' : bkg+['AZH_1200_850']
}

aliases['ellipse_mA_1200_mH_900'] = {
    'class' : 'elliptical_bin',
    'args'  : (1200,900,False),
    'samples' : bkg+['AZH_1200_900']
}

aliases['ellipse_mA_1300_mH_1000'] = {
    'class' : 'elliptical_bin',
    'args'  : (1300,1000,False),
    'samples' : bkg+['AZH_1300_1000']
}

aliases['ellipse_mA_1300_mH_1100'] = {
    'class' : 'elliptical_bin',
    'args'  : (1300,1100,False),
    'samples' : bkg+['AZH_1300_1100']
}

aliases['ellipse_mA_1300_mH_1200'] = {
    'class' : 'elliptical_bin',
    'args'  : (1300,1200,False),
    'samples' : bkg+['AZH_1300_1200']
}

aliases['ellipse_mA_1300_mH_350'] = {
    'class' : 'elliptical_bin',
    'args'  : (1300,350,False),
    'samples' : bkg+['AZH_1300_350']
}

aliases['ellipse_mA_1300_mH_400'] = {
    'class' : 'elliptical_bin',
    'args'  : (1300,400,False),
    'samples' : bkg+['AZH_1300_400']
}

aliases['ellipse_mA_1300_mH_500'] = {
    'class' : 'elliptical_bin',
    'args'  : (1300,500,False),
    'samples' : bkg+['AZH_1300_500']
}

aliases['ellipse_mA_1300_mH_600'] = {
    'class' : 'elliptical_bin',
    'args'  : (1300,600,False),
    'samples' : bkg+['AZH_1300_600']
}

aliases['ellipse_mA_1300_mH_700'] = {
    'class' : 'elliptical_bin',
    'args'  : (1300,700,False),
    'samples' : bkg+['AZH_1300_700']
}

aliases['ellipse_mA_1300_mH_800'] = {
    'class' : 'elliptical_bin',
    'args'  : (1300,800,False),
    'samples' : bkg+['AZH_1300_800']
}

aliases['ellipse_mA_1300_mH_900'] = {
    'class' : 'elliptical_bin',
    'args'  : (1300,900,False),
    'samples' : bkg+['AZH_1300_900']
}

aliases['ellipse_mA_1400_mH_1000'] = {
    'class' : 'elliptical_bin',
    'args'  : (1400,1000,False),
    'samples' : bkg+['AZH_1400_1000']
}

aliases['ellipse_mA_1400_mH_1100'] = {
    'class' : 'elliptical_bin',
    'args'  : (1400,1100,False),
    'samples' : bkg+['AZH_1400_1100']
}

aliases['ellipse_mA_1400_mH_1200'] = {
    'class' : 'elliptical_bin',
    'args'  : (1400,1200,False),
    'samples' : bkg+['AZH_1400_1200']
}

aliases['ellipse_mA_1400_mH_1300'] = {
    'class' : 'elliptical_bin',
    'args'  : (1400,1300,False),
    'samples' : bkg+['AZH_1400_1300']
}

aliases['ellipse_mA_1400_mH_350'] = {
    'class' : 'elliptical_bin',
    'args'  : (1400,350,False),
    'samples' : bkg+['AZH_1400_350']
}

aliases['ellipse_mA_1400_mH_400'] = {
    'class' : 'elliptical_bin',
    'args'  : (1400,400,False),
    'samples' : bkg+['AZH_1400_400']
}

aliases['ellipse_mA_1400_mH_500'] = {
    'class' : 'elliptical_bin',
    'args'  : (1400,500,False),
    'samples' : bkg+['AZH_1400_500']
}

aliases['ellipse_mA_1400_mH_600'] = {
    'class' : 'elliptical_bin',
    'args'  : (1400,600,False),
    'samples' : bkg+['AZH_1400_600']
}

aliases['ellipse_mA_1400_mH_700'] = {
    'class' : 'elliptical_bin',
    'args'  : (1400,700,False),
    'samples' : bkg+['AZH_1400_700']
}

aliases['ellipse_mA_1400_mH_800'] = {
    'class' : 'elliptical_bin',
    'args'  : (1400,800,False),
    'samples' : bkg+['AZH_1400_800']
}

aliases['ellipse_mA_1400_mH_900'] = {
    'class' : 'elliptical_bin',
    'args'  : (1400,900,False),
    'samples' : bkg+['AZH_1400_900']
}

aliases['ellipse_mA_1500_mH_1000'] = {
    'class' : 'elliptical_bin',
    'args'  : (1500,1000,False),
    'samples' : bkg+['AZH_1500_1000']
}

aliases['ellipse_mA_1500_mH_1100'] = {
    'class' : 'elliptical_bin',
    'args'  : (1500,1100,False),
    'samples' : bkg+['AZH_1500_1100']
}

aliases['ellipse_mA_1500_mH_1200'] = {
    'class' : 'elliptical_bin',
    'args'  : (1500,1200,False),
    'samples' : bkg+['AZH_1500_1200']
}

aliases['ellipse_mA_1500_mH_1300'] = {
    'class' : 'elliptical_bin',
    'args'  : (1500,1300,False),
    'samples' : bkg+['AZH_1500_1300']
}

aliases['ellipse_mA_1500_mH_1400'] = {
    'class' : 'elliptical_bin',
    'args'  : (1500,1400,False),
    'samples' : bkg+['AZH_1500_1400']
}

aliases['ellipse_mA_1500_mH_350'] = {
    'class' : 'elliptical_bin',
    'args'  : (1500,350,False),
    'samples' : bkg+['AZH_1500_350']
}

aliases['ellipse_mA_1500_mH_400'] = {
    'class' : 'elliptical_bin',
    'args'  : (1500,400,False),
    'samples' : bkg+['AZH_1500_400']
}

aliases['ellipse_mA_1500_mH_500'] = {
    'class' : 'elliptical_bin',
    'args'  : (1500,500,False),
    'samples' : bkg+['AZH_1500_500']
}

aliases['ellipse_mA_1500_mH_600'] = {
    'class' : 'elliptical_bin',
    'args'  : (1500,600,False),
    'samples' : bkg+['AZH_1500_600']
}

aliases['ellipse_mA_1500_mH_700'] = {
    'class' : 'elliptical_bin',
    'args'  : (1500,700,False),
    'samples' : bkg+['AZH_1500_700']
}

aliases['ellipse_mA_1500_mH_800'] = {
    'class' : 'elliptical_bin',
    'args'  : (1500,800,False),
    'samples' : bkg+['AZH_1500_800']
}

aliases['ellipse_mA_1500_mH_900'] = {
    'class' : 'elliptical_bin',
    'args'  : (1500,900,False),
    'samples' : bkg+['AZH_1500_900']
}

aliases['ellipse_mA_1600_mH_1000'] = {
    'class' : 'elliptical_bin',
    'args'  : (1600,1000,False),
    'samples' : bkg+['AZH_1600_1000']
}

aliases['ellipse_mA_1600_mH_1100'] = {
    'class' : 'elliptical_bin',
    'args'  : (1600,1100,False),
    'samples' : bkg+['AZH_1600_1100']
}

aliases['ellipse_mA_1600_mH_1200'] = {
    'class' : 'elliptical_bin',
    'args'  : (1600,1200,False),
    'samples' : bkg+['AZH_1600_1200']
}

aliases['ellipse_mA_1600_mH_1300'] = {
    'class' : 'elliptical_bin',
    'args'  : (1600,1300,False),
    'samples' : bkg+['AZH_1600_1300']
}

aliases['ellipse_mA_1600_mH_1400'] = {
    'class' : 'elliptical_bin',
    'args'  : (1600,1400,False),
    'samples' : bkg+['AZH_1600_1400']
}

aliases['ellipse_mA_1600_mH_1500'] = {
    'class' : 'elliptical_bin',
    'args'  : (1600,1500,False),
    'samples' : bkg+['AZH_1600_1500']
}

aliases['ellipse_mA_1600_mH_350'] = {
    'class' : 'elliptical_bin',
    'args'  : (1600,350,False),
    'samples' : bkg+['AZH_1600_350']
}

aliases['ellipse_mA_1600_mH_400'] = {
    'class' : 'elliptical_bin',
    'args'  : (1600,400,False),
    'samples' : bkg+['AZH_1600_400']
}

aliases['ellipse_mA_1600_mH_500'] = {
    'class' : 'elliptical_bin',
    'args'  : (1600,500,False),
    'samples' : bkg+['AZH_1600_500']
}

aliases['ellipse_mA_1600_mH_600'] = {
    'class' : 'elliptical_bin',
    'args'  : (1600,600,False),
    'samples' : bkg+['AZH_1600_600']
}

aliases['ellipse_mA_1600_mH_700'] = {
    'class' : 'elliptical_bin',
    'args'  : (1600,700,False),
    'samples' : bkg+['AZH_1600_700']
}

aliases['ellipse_mA_1600_mH_800'] = {
    'class' : 'elliptical_bin',
    'args'  : (1600,800,False),
    'samples' : bkg+['AZH_1600_800']
}

aliases['ellipse_mA_1600_mH_900'] = {
    'class' : 'elliptical_bin',
    'args'  : (1600,900,False),
    'samples' : bkg+['AZH_1600_900']
}

aliases['ellipse_mA_1700_mH_1000'] = {
    'class' : 'elliptical_bin',
    'args'  : (1700,1000,False),
    'samples' : bkg+['AZH_1700_1000']
}

aliases['ellipse_mA_1700_mH_1100'] = {
    'class' : 'elliptical_bin',
    'args'  : (1700,1100,False),
    'samples' : bkg+['AZH_1700_1100']
}

aliases['ellipse_mA_1700_mH_1200'] = {
    'class' : 'elliptical_bin',
    'args'  : (1700,1200,False),
    'samples' : bkg+['AZH_1700_1200']
}

aliases['ellipse_mA_1700_mH_1300'] = {
    'class' : 'elliptical_bin',
    'args'  : (1700,1300,False),
    'samples' : bkg+['AZH_1700_1300']
}

aliases['ellipse_mA_1700_mH_1400'] = {
    'class' : 'elliptical_bin',
    'args'  : (1700,1400,False),
    'samples' : bkg+['AZH_1700_1400']
}

aliases['ellipse_mA_1700_mH_1500'] = {
    'class' : 'elliptical_bin',
    'args'  : (1700,1500,False),
    'samples' : bkg+['AZH_1700_1500']
}

aliases['ellipse_mA_1700_mH_1600'] = {
    'class' : 'elliptical_bin',
    'args'  : (1700,1600,False),
    'samples' : bkg+['AZH_1700_1600']
}

aliases['ellipse_mA_1700_mH_350'] = {
    'class' : 'elliptical_bin',
    'args'  : (1700,350,False),
    'samples' : bkg+['AZH_1700_350']
}

aliases['ellipse_mA_1700_mH_400'] = {
    'class' : 'elliptical_bin',
    'args'  : (1700,400,False),
    'samples' : bkg+['AZH_1700_400']
}

aliases['ellipse_mA_1700_mH_500'] = {
    'class' : 'elliptical_bin',
    'args'  : (1700,500,False),
    'samples' : bkg+['AZH_1700_500']
}

aliases['ellipse_mA_1700_mH_600'] = {
    'class' : 'elliptical_bin',
    'args'  : (1700,600,False),
    'samples' : bkg+['AZH_1700_600']
}

aliases['ellipse_mA_1700_mH_700'] = {
    'class' : 'elliptical_bin',
    'args'  : (1700,700,False),
    'samples' : bkg+['AZH_1700_700']
}

aliases['ellipse_mA_1700_mH_800'] = {
    'class' : 'elliptical_bin',
    'args'  : (1700,800,False),
    'samples' : bkg+['AZH_1700_800']
}

aliases['ellipse_mA_1700_mH_900'] = {
    'class' : 'elliptical_bin',
    'args'  : (1700,900,False),
    'samples' : bkg+['AZH_1700_900']
}

aliases['ellipse_mA_1800_mH_1000'] = {
    'class' : 'elliptical_bin',
    'args'  : (1800,1000,False),
    'samples' : bkg+['AZH_1800_1000']
}

aliases['ellipse_mA_1800_mH_1100'] = {
    'class' : 'elliptical_bin',
    'args'  : (1800,1100,False),
    'samples' : bkg+['AZH_1800_1100']
}

aliases['ellipse_mA_1800_mH_1200'] = {
    'class' : 'elliptical_bin',
    'args'  : (1800,1200,False),
    'samples' : bkg+['AZH_1800_1200']
}

aliases['ellipse_mA_1800_mH_1300'] = {
    'class' : 'elliptical_bin',
    'args'  : (1800,1300,False),
    'samples' : bkg+['AZH_1800_1300']
}

aliases['ellipse_mA_1800_mH_1400'] = {
    'class' : 'elliptical_bin',
    'args'  : (1800,1400,False),
    'samples' : bkg+['AZH_1800_1400']
}

aliases['ellipse_mA_1800_mH_1500'] = {
    'class' : 'elliptical_bin',
    'args'  : (1800,1500,False),
    'samples' : bkg+['AZH_1800_1500']
}

aliases['ellipse_mA_1800_mH_1600'] = {
    'class' : 'elliptical_bin',
    'args'  : (1800,1600,False),
    'samples' : bkg+['AZH_1800_1600']
}

aliases['ellipse_mA_1800_mH_1700'] = {
    'class' : 'elliptical_bin',
    'args'  : (1800,1700,False),
    'samples' : bkg+['AZH_1800_1700']
}

aliases['ellipse_mA_1800_mH_350'] = {
    'class' : 'elliptical_bin',
    'args'  : (1800,350,False),
    'samples' : bkg+['AZH_1800_350']
}

aliases['ellipse_mA_1800_mH_400'] = {
    'class' : 'elliptical_bin',
    'args'  : (1800,400,False),
    'samples' : bkg+['AZH_1800_400']
}

aliases['ellipse_mA_1800_mH_500'] = {
    'class' : 'elliptical_bin',
    'args'  : (1800,500,False),
    'samples' : bkg+['AZH_1800_500']
}

aliases['ellipse_mA_1800_mH_600'] = {
    'class' : 'elliptical_bin',
    'args'  : (1800,600,False),
    'samples' : bkg+['AZH_1800_600']
}

aliases['ellipse_mA_1800_mH_700'] = {
    'class' : 'elliptical_bin',
    'args'  : (1800,700,False),
    'samples' : bkg+['AZH_1800_700']
}

aliases['ellipse_mA_1800_mH_800'] = {
    'class' : 'elliptical_bin',
    'args'  : (1800,800,False),
    'samples' : bkg+['AZH_1800_800']
}

aliases['ellipse_mA_1800_mH_900'] = {
    'class' : 'elliptical_bin',
    'args'  : (1800,900,False),
    'samples' : bkg+['AZH_1800_900']
}

aliases['ellipse_mA_1900_mH_1000'] = {
    'class' : 'elliptical_bin',
    'args'  : (1900,1000,False),
    'samples' : bkg+['AZH_1900_1000']
}

aliases['ellipse_mA_1900_mH_1100'] = {
    'class' : 'elliptical_bin',
    'args'  : (1900,1100,False),
    'samples' : bkg+['AZH_1900_1100']
}

aliases['ellipse_mA_1900_mH_1200'] = {
    'class' : 'elliptical_bin',
    'args'  : (1900,1200,False),
    'samples' : bkg+['AZH_1900_1200']
}

aliases['ellipse_mA_1900_mH_1300'] = {
    'class' : 'elliptical_bin',
    'args'  : (1900,1300,False),
    'samples' : bkg+['AZH_1900_1300']
}

aliases['ellipse_mA_1900_mH_1400'] = {
    'class' : 'elliptical_bin',
    'args'  : (1900,1400,False),
    'samples' : bkg+['AZH_1900_1400']
}

aliases['ellipse_mA_1900_mH_1500'] = {
    'class' : 'elliptical_bin',
    'args'  : (1900,1500,False),
    'samples' : bkg+['AZH_1900_1500']
}

aliases['ellipse_mA_1900_mH_1600'] = {
    'class' : 'elliptical_bin',
    'args'  : (1900,1600,False),
    'samples' : bkg+['AZH_1900_1600']
}

aliases['ellipse_mA_1900_mH_1700'] = {
    'class' : 'elliptical_bin',
    'args'  : (1900,1700,False),
    'samples' : bkg+['AZH_1900_1700']
}

aliases['ellipse_mA_1900_mH_1800'] = {
    'class' : 'elliptical_bin',
    'args'  : (1900,1800,False),
    'samples' : bkg+['AZH_1900_1800']
}

aliases['ellipse_mA_1900_mH_350'] = {
    'class' : 'elliptical_bin',
    'args'  : (1900,350,False),
    'samples' : bkg+['AZH_1900_350']
}

aliases['ellipse_mA_1900_mH_400'] = {
    'class' : 'elliptical_bin',
    'args'  : (1900,400,False),
    'samples' : bkg+['AZH_1900_400']
}

aliases['ellipse_mA_1900_mH_500'] = {
    'class' : 'elliptical_bin',
    'args'  : (1900,500,False),
    'samples' : bkg+['AZH_1900_500']
}

aliases['ellipse_mA_1900_mH_600'] = {
    'class' : 'elliptical_bin',
    'args'  : (1900,600,False),
    'samples' : bkg+['AZH_1900_600']
}

aliases['ellipse_mA_1900_mH_700'] = {
    'class' : 'elliptical_bin',
    'args'  : (1900,700,False),
    'samples' : bkg+['AZH_1900_700']
}

aliases['ellipse_mA_1900_mH_800'] = {
    'class' : 'elliptical_bin',
    'args'  : (1900,800,False),
    'samples' : bkg+['AZH_1900_800']
}

aliases['ellipse_mA_1900_mH_900'] = {
    'class' : 'elliptical_bin',
    'args'  : (1900,900,False),
    'samples' : bkg+['AZH_1900_900']
}

aliases['ellipse_mA_2000_mH_1000'] = {
    'class' : 'elliptical_bin',
    'args'  : (2000,1000,False),
    'samples' : bkg+['AZH_2000_1000']
}

aliases['ellipse_mA_2000_mH_1100'] = {
    'class' : 'elliptical_bin',
    'args'  : (2000,1100,False),
    'samples' : bkg+['AZH_2000_1100']
}

aliases['ellipse_mA_2000_mH_1200'] = {
    'class' : 'elliptical_bin',
    'args'  : (2000,1200,False),
    'samples' : bkg+['AZH_2000_1200']
}

aliases['ellipse_mA_2000_mH_1300'] = {
    'class' : 'elliptical_bin',
    'args'  : (2000,1300,False),
    'samples' : bkg+['AZH_2000_1300']
}

aliases['ellipse_mA_2000_mH_1400'] = {
    'class' : 'elliptical_bin',
    'args'  : (2000,1400,False),
    'samples' : bkg+['AZH_2000_1400']
}

aliases['ellipse_mA_2000_mH_1500'] = {
    'class' : 'elliptical_bin',
    'args'  : (2000,1500,False),
    'samples' : bkg+['AZH_2000_1500']
}

aliases['ellipse_mA_2000_mH_1600'] = {
    'class' : 'elliptical_bin',
    'args'  : (2000,1600,False),
    'samples' : bkg+['AZH_2000_1600']
}

aliases['ellipse_mA_2000_mH_1700'] = {
    'class' : 'elliptical_bin',
    'args'  : (2000,1700,False),
    'samples' : bkg+['AZH_2000_1700']
}

aliases['ellipse_mA_2000_mH_1800'] = {
    'class' : 'elliptical_bin',
    'args'  : (2000,1800,False),
    'samples' : bkg+['AZH_2000_1800']
}

aliases['ellipse_mA_2000_mH_1900'] = {
    'class' : 'elliptical_bin',
    'args'  : (2000,1900,False),
    'samples' : bkg+['AZH_2000_1900']
}

aliases['ellipse_mA_2000_mH_350'] = {
    'class' : 'elliptical_bin',
    'args'  : (2000,350,False),
    'samples' : bkg+['AZH_2000_350']
}

aliases['ellipse_mA_2000_mH_400'] = {
    'class' : 'elliptical_bin',
    'args'  : (2000,400,False),
    'samples' : bkg+['AZH_2000_400']
}

aliases['ellipse_mA_2000_mH_500'] = {
    'class' : 'elliptical_bin',
    'args'  : (2000,500,False),
    'samples' : bkg+['AZH_2000_500']
}

aliases['ellipse_mA_2000_mH_600'] = {
    'class' : 'elliptical_bin',
    'args'  : (2000,600,False),
    'samples' : bkg+['AZH_2000_600']
}

aliases['ellipse_mA_2000_mH_700'] = {
    'class' : 'elliptical_bin',
    'args'  : (2000,700,False),
    'samples' : bkg+['AZH_2000_700']
}

aliases['ellipse_mA_2000_mH_800'] = {
    'class' : 'elliptical_bin',
    'args'  : (2000,800,False),
    'samples' : bkg+['AZH_2000_800']
}

aliases['ellipse_mA_2000_mH_900'] = {
    'class' : 'elliptical_bin',
    'args'  : (2000,900,False),
    'samples' : bkg+['AZH_2000_900']
}

aliases['ellipse_mA_2100_mH_1000'] = {
    'class' : 'elliptical_bin',
    'args'  : (2100,1000,False),
    'samples' : bkg+['AZH_2100_1000']
}

aliases['ellipse_mA_2100_mH_1100'] = {
    'class' : 'elliptical_bin',
    'args'  : (2100,1100,False),
    'samples' : bkg+['AZH_2100_1100']
}

aliases['ellipse_mA_2100_mH_1200'] = {
    'class' : 'elliptical_bin',
    'args'  : (2100,1200,False),
    'samples' : bkg+['AZH_2100_1200']
}

aliases['ellipse_mA_2100_mH_1300'] = {
    'class' : 'elliptical_bin',
    'args'  : (2100,1300,False),
    'samples' : bkg+['AZH_2100_1300']
}

aliases['ellipse_mA_2100_mH_1400'] = {
    'class' : 'elliptical_bin',
    'args'  : (2100,1400,False),
    'samples' : bkg+['AZH_2100_1400']
}

aliases['ellipse_mA_2100_mH_1500'] = {
    'class' : 'elliptical_bin',
    'args'  : (2100,1500,False),
    'samples' : bkg+['AZH_2100_1500']
}

aliases['ellipse_mA_2100_mH_1600'] = {
    'class' : 'elliptical_bin',
    'args'  : (2100,1600,False),
    'samples' : bkg+['AZH_2100_1600']
}

aliases['ellipse_mA_2100_mH_1700'] = {
    'class' : 'elliptical_bin',
    'args'  : (2100,1700,False),
    'samples' : bkg+['AZH_2100_1700']
}

aliases['ellipse_mA_2100_mH_1800'] = {
    'class' : 'elliptical_bin',
    'args'  : (2100,1800,False),
    'samples' : bkg+['AZH_2100_1800']
}

aliases['ellipse_mA_2100_mH_1900'] = {
    'class' : 'elliptical_bin',
    'args'  : (2100,1900,False),
    'samples' : bkg+['AZH_2100_1900']
}

aliases['ellipse_mA_2100_mH_2000'] = {
    'class' : 'elliptical_bin',
    'args'  : (2100,2000,False),
    'samples' : bkg+['AZH_2100_2000']
}

aliases['ellipse_mA_2100_mH_350'] = {
    'class' : 'elliptical_bin',
    'args'  : (2100,350,False),
    'samples' : bkg+['AZH_2100_350']
}

aliases['ellipse_mA_2100_mH_400'] = {
    'class' : 'elliptical_bin',
    'args'  : (2100,400,False),
    'samples' : bkg+['AZH_2100_400']
}

aliases['ellipse_mA_2100_mH_500'] = {
    'class' : 'elliptical_bin',
    'args'  : (2100,500,False),
    'samples' : bkg+['AZH_2100_500']
}

aliases['ellipse_mA_2100_mH_600'] = {
    'class' : 'elliptical_bin',
    'args'  : (2100,600,False),
    'samples' : bkg+['AZH_2100_600']
}

aliases['ellipse_mA_2100_mH_700'] = {
    'class' : 'elliptical_bin',
    'args'  : (2100,700,False),
    'samples' : bkg+['AZH_2100_700']
}

aliases['ellipse_mA_2100_mH_800'] = {
    'class' : 'elliptical_bin',
    'args'  : (2100,800,False),
    'samples' : bkg+['AZH_2100_800']
}

aliases['ellipse_mA_2100_mH_900'] = {
    'class' : 'elliptical_bin',
    'args'  : (2100,900,False),
    'samples' : bkg+['AZH_2100_900']
}

aliases['ellipse_mA_430_mH_330'] = {
    'class' : 'elliptical_bin',
    'args'  : (430,330,False),
    'samples' : bkg+['AZH_430_330']
}

aliases['ellipse_mA_450_mH_330'] = {
    'class' : 'elliptical_bin',
    'args'  : (450,330,False),
    'samples' : bkg+['AZH_450_330']
}

aliases['ellipse_mA_450_mH_350'] = {
    'class' : 'elliptical_bin',
    'args'  : (450,350,False),
    'samples' : bkg+['AZH_450_350']
}

aliases['ellipse_mA_500_mH_330'] = {
    'class' : 'elliptical_bin',
    'args'  : (500,330,False),
    'samples' : bkg+['AZH_500_330']
}

aliases['ellipse_mA_500_mH_350'] = {
    'class' : 'elliptical_bin',
    'args'  : (500,350,False),
    'samples' : bkg+['AZH_500_350']
}

aliases['ellipse_mA_500_mH_370'] = {
    'class' : 'elliptical_bin',
    'args'  : (500,370,False),
    'samples' : bkg+['AZH_500_370']
}

aliases['ellipse_mA_500_mH_400'] = {
    'class' : 'elliptical_bin',
    'args'  : (500,400,False),
    'samples' : bkg+['AZH_500_400']
}

aliases['ellipse_mA_550_mH_330'] = {
    'class' : 'elliptical_bin',
    'args'  : (550,330,False),
    'samples' : bkg+['AZH_550_330']
}

aliases['ellipse_mA_550_mH_350'] = {
    'class' : 'elliptical_bin',
    'args'  : (550,350,False),
    'samples' : bkg+['AZH_550_350']
}

aliases['ellipse_mA_550_mH_400'] = {
    'class' : 'elliptical_bin',
    'args'  : (550,400,False),
    'samples' : bkg+['AZH_550_400']
}

aliases['ellipse_mA_550_mH_450'] = {
    'class' : 'elliptical_bin',
    'args'  : (550,450,False),
    'samples' : bkg+['AZH_550_450']
}

aliases['ellipse_mA_600_mH_330'] = {
    'class' : 'elliptical_bin',
    'args'  : (600,330,False),
    'samples' : bkg+['AZH_600_330']
}

aliases['ellipse_mA_600_mH_350'] = {
    'class' : 'elliptical_bin',
    'args'  : (600,350,False),
    'samples' : bkg+['AZH_600_350']
}

aliases['ellipse_mA_600_mH_400'] = {
    'class' : 'elliptical_bin',
    'args'  : (600,400,False),
    'samples' : bkg+['AZH_600_400']
}

aliases['ellipse_mA_600_mH_450'] = {
    'class' : 'elliptical_bin',
    'args'  : (600,450,False),
    'samples' : bkg+['AZH_600_450']
}

aliases['ellipse_mA_600_mH_500'] = {
    'class' : 'elliptical_bin',
    'args'  : (600,500,False),
    'samples' : bkg+['AZH_600_500']
}

aliases['ellipse_mA_650_mH_330'] = {
    'class' : 'elliptical_bin',
    'args'  : (650,330,False),
    'samples' : bkg+['AZH_650_330']
}

aliases['ellipse_mA_650_mH_350'] = {
    'class' : 'elliptical_bin',
    'args'  : (650,350,False),
    'samples' : bkg+['AZH_650_350']
}

aliases['ellipse_mA_650_mH_400'] = {
    'class' : 'elliptical_bin',
    'args'  : (650,400,False),
    'samples' : bkg+['AZH_650_400']
}

aliases['ellipse_mA_650_mH_450'] = {
    'class' : 'elliptical_bin',
    'args'  : (650,450,False),
    'samples' : bkg+['AZH_650_450']
}

aliases['ellipse_mA_650_mH_500'] = {
    'class' : 'elliptical_bin',
    'args'  : (650,500,False),
    'samples' : bkg+['AZH_650_500']
}

aliases['ellipse_mA_650_mH_550'] = {
    'class' : 'elliptical_bin',
    'args'  : (650,550,False),
    'samples' : bkg+['AZH_650_550']
}

aliases['ellipse_mA_700_mH_330'] = {
    'class' : 'elliptical_bin',
    'args'  : (700,330,False),
    'samples' : bkg+['AZH_700_330']
}

aliases['ellipse_mA_700_mH_350'] = {
    'class' : 'elliptical_bin',
    'args'  : (700,350,False),
    'samples' : bkg+['AZH_700_350']
}

aliases['ellipse_mA_700_mH_370'] = {
    'class' : 'elliptical_bin',
    'args'  : (700,370,False),
    'samples' : bkg+['AZH_700_370']
}

aliases['ellipse_mA_700_mH_400'] = {
    'class' : 'elliptical_bin',
    'args'  : (700,400,False),
    'samples' : bkg+['AZH_700_400']
}

aliases['ellipse_mA_700_mH_450'] = {
    'class' : 'elliptical_bin',
    'args'  : (700,450,False),
    'samples' : bkg+['AZH_700_450']
}

aliases['ellipse_mA_700_mH_500'] = {
    'class' : 'elliptical_bin',
    'args'  : (700,500,False),
    'samples' : bkg+['AZH_700_500']
}

aliases['ellipse_mA_700_mH_550'] = {
    'class' : 'elliptical_bin',
    'args'  : (700,550,False),
    'samples' : bkg+['AZH_700_550']
}

aliases['ellipse_mA_700_mH_600'] = {
    'class' : 'elliptical_bin',
    'args'  : (700,600,False),
    'samples' : bkg+['AZH_700_600']
}

aliases['ellipse_mA_750_mH_330'] = {
    'class' : 'elliptical_bin',
    'args'  : (750,330,False),
    'samples' : bkg+['AZH_750_330']
}

aliases['ellipse_mA_750_mH_350'] = {
    'class' : 'elliptical_bin',
    'args'  : (750,350,False),
    'samples' : bkg+['AZH_750_350']
}

aliases['ellipse_mA_750_mH_400'] = {
    'class' : 'elliptical_bin',
    'args'  : (750,400,False),
    'samples' : bkg+['AZH_750_400']
}

aliases['ellipse_mA_750_mH_450'] = {
    'class' : 'elliptical_bin',
    'args'  : (750,450,False),
    'samples' : bkg+['AZH_750_450']
}

aliases['ellipse_mA_750_mH_500'] = {
    'class' : 'elliptical_bin',
    'args'  : (750,500,False),
    'samples' : bkg+['AZH_750_500']
}

aliases['ellipse_mA_750_mH_550'] = {
    'class' : 'elliptical_bin',
    'args'  : (750,550,False),
    'samples' : bkg+['AZH_750_550']
}

aliases['ellipse_mA_750_mH_600'] = {
    'class' : 'elliptical_bin',
    'args'  : (750,600,False),
    'samples' : bkg+['AZH_750_600']
}

aliases['ellipse_mA_750_mH_650'] = {
    'class' : 'elliptical_bin',
    'args'  : (750,650,False),
    'samples' : bkg+['AZH_750_650']
}

aliases['ellipse_mA_800_mH_330'] = {
    'class' : 'elliptical_bin',
    'args'  : (800,330,False),
    'samples' : bkg+['AZH_800_330']
}

aliases['ellipse_mA_800_mH_350'] = {
    'class' : 'elliptical_bin',
    'args'  : (800,350,False),
    'samples' : bkg+['AZH_800_350']
}

aliases['ellipse_mA_800_mH_400'] = {
    'class' : 'elliptical_bin',
    'args'  : (800,400,False),
    'samples' : bkg+['AZH_800_400']
}

aliases['ellipse_mA_800_mH_450'] = {
    'class' : 'elliptical_bin',
    'args'  : (800,450,False),
    'samples' : bkg+['AZH_800_450']
}

aliases['ellipse_mA_800_mH_500'] = {
    'class' : 'elliptical_bin',
    'args'  : (800,500,False),
    'samples' : bkg+['AZH_800_500']
}

aliases['ellipse_mA_800_mH_550'] = {
    'class' : 'elliptical_bin',
    'args'  : (800,550,False),
    'samples' : bkg+['AZH_800_550']
}

aliases['ellipse_mA_800_mH_600'] = {
    'class' : 'elliptical_bin',
    'args'  : (800,600,False),
    'samples' : bkg+['AZH_800_600']
}

aliases['ellipse_mA_800_mH_650'] = {
    'class' : 'elliptical_bin',
    'args'  : (800,650,False),
    'samples' : bkg+['AZH_800_650']
}

aliases['ellipse_mA_800_mH_700'] = {
    'class' : 'elliptical_bin',
    'args'  : (800,700,False),
    'samples' : bkg+['AZH_800_700']
}

aliases['ellipse_mA_850_mH_330'] = {
    'class' : 'elliptical_bin',
    'args'  : (850,330,False),
    'samples' : bkg+['AZH_850_330']
}

aliases['ellipse_mA_850_mH_350'] = {
    'class' : 'elliptical_bin',
    'args'  : (850,350,False),
    'samples' : bkg+['AZH_850_350']
}

aliases['ellipse_mA_850_mH_400'] = {
    'class' : 'elliptical_bin',
    'args'  : (850,400,False),
    'samples' : bkg+['AZH_850_400']
}

aliases['ellipse_mA_850_mH_450'] = {
    'class' : 'elliptical_bin',
    'args'  : (850,450,False),
    'samples' : bkg+['AZH_850_450']
}

aliases['ellipse_mA_850_mH_500'] = {
    'class' : 'elliptical_bin',
    'args'  : (850,500,False),
    'samples' : bkg+['AZH_850_500']
}

aliases['ellipse_mA_850_mH_550'] = {
    'class' : 'elliptical_bin',
    'args'  : (850,550,False),
    'samples' : bkg+['AZH_850_550']
}

aliases['ellipse_mA_850_mH_600'] = {
    'class' : 'elliptical_bin',
    'args'  : (850,600,False),
    'samples' : bkg+['AZH_850_600']
}

aliases['ellipse_mA_850_mH_650'] = {
    'class' : 'elliptical_bin',
    'args'  : (850,650,False),
    'samples' : bkg+['AZH_850_650']
}

aliases['ellipse_mA_850_mH_700'] = {
    'class' : 'elliptical_bin',
    'args'  : (850,700,False),
    'samples' : bkg+['AZH_850_700']
}

aliases['ellipse_mA_850_mH_750'] = {
    'class' : 'elliptical_bin',
    'args'  : (850,750,False),
    'samples' : bkg+['AZH_850_750']
}

aliases['ellipse_mA_900_mH_330'] = {
    'class' : 'elliptical_bin',
    'args'  : (900,330,False),
    'samples' : bkg+['AZH_900_330']
}

aliases['ellipse_mA_900_mH_350'] = {
    'class' : 'elliptical_bin',
    'args'  : (900,350,False),
    'samples' : bkg+['AZH_900_350']
}

aliases['ellipse_mA_900_mH_370'] = {
    'class' : 'elliptical_bin',
    'args'  : (900,370,False),
    'samples' : bkg+['AZH_900_370']
}

aliases['ellipse_mA_900_mH_400'] = {
    'class' : 'elliptical_bin',
    'args'  : (900,400,False),
    'samples' : bkg+['AZH_900_400']
}

aliases['ellipse_mA_900_mH_450'] = {
    'class' : 'elliptical_bin',
    'args'  : (900,450,False),
    'samples' : bkg+['AZH_900_450']
}

aliases['ellipse_mA_900_mH_500'] = {
    'class' : 'elliptical_bin',
    'args'  : (900,500,False),
    'samples' : bkg+['AZH_900_500']
}

aliases['ellipse_mA_900_mH_550'] = {
    'class' : 'elliptical_bin',
    'args'  : (900,550,False),
    'samples' : bkg+['AZH_900_550']
}

aliases['ellipse_mA_900_mH_600'] = {
    'class' : 'elliptical_bin',
    'args'  : (900,600,False),
    'samples' : bkg+['AZH_900_600']
}

aliases['ellipse_mA_900_mH_650'] = {
    'class' : 'elliptical_bin',
    'args'  : (900,650,False),
    'samples' : bkg+['AZH_900_650']
}

aliases['ellipse_mA_900_mH_700'] = {
    'class' : 'elliptical_bin',
    'args'  : (900,700,False),
    'samples' : bkg+['AZH_900_700']
}

aliases['ellipse_mA_900_mH_750'] = {
    'class' : 'elliptical_bin',
    'args'  : (900,750,False),
    'samples' : bkg+['AZH_900_750']
}

aliases['ellipse_mA_900_mH_800'] = {
    'class' : 'elliptical_bin',
    'args'  : (900,800,False),
    'samples' : bkg+['AZH_900_800']
}

aliases['ellipse_mA_950_mH_330'] = {
    'class' : 'elliptical_bin',
    'args'  : (950,330,False),
    'samples' : bkg+['AZH_950_330']
}

aliases['ellipse_mA_950_mH_350'] = {
    'class' : 'elliptical_bin',
    'args'  : (950,350,False),
    'samples' : bkg+['AZH_950_350']
}

aliases['ellipse_mA_950_mH_400'] = {
    'class' : 'elliptical_bin',
    'args'  : (950,400,False),
    'samples' : bkg+['AZH_950_400']
}

aliases['ellipse_mA_950_mH_450'] = {
    'class' : 'elliptical_bin',
    'args'  : (950,450,False),
    'samples' : bkg+['AZH_950_450']
}

aliases['ellipse_mA_950_mH_500'] = {
    'class' : 'elliptical_bin',
    'args'  : (950,500,False),
    'samples' : bkg+['AZH_950_500']
}

aliases['ellipse_mA_950_mH_550'] = {
    'class' : 'elliptical_bin',
    'args'  : (950,550,False),
    'samples' : bkg+['AZH_950_550']
}

aliases['ellipse_mA_950_mH_600'] = {
    'class' : 'elliptical_bin',
    'args'  : (950,600,False),
    'samples' : bkg+['AZH_950_600']
}

aliases['ellipse_mA_950_mH_650'] = {
    'class' : 'elliptical_bin',
    'args'  : (950,650,False),
    'samples' : bkg+['AZH_950_650']
}

aliases['ellipse_mA_950_mH_700'] = {
    'class' : 'elliptical_bin',
    'args'  : (950,700,False),
    'samples' : bkg+['AZH_950_700']
}

aliases['ellipse_mA_950_mH_750'] = {
    'class' : 'elliptical_bin',
    'args'  : (950,750,False),
    'samples' : bkg+['AZH_950_750']
}

aliases['ellipse_mA_950_mH_800'] = {
    'class' : 'elliptical_bin',
    'args'  : (950,800,False),
    'samples' : bkg+['AZH_950_800']
}

aliases['ellipse_mA_950_mH_850'] = {
    'class' : 'elliptical_bin',
    'args'  : (950,850,False),
    'samples' : bkg+['AZH_950_850']
}

#######################
### SFs for tthMVA  ###
#######################

aliases['SFweightEleUp'] = { 
    'expr': 'LepSF3l__ele_'+eleWP_new+'__Up',
    'samples': mc
}

aliases['SFweightEleDown'] = {
    'expr': 'LepSF3l__ele_'+eleWP_new+'__Do',
    'samples': mc
}

aliases['SFweightMuUp'] = {
    'expr': 'LepSF3l__mu_'+muWP_new+'__Up',
    'samples': mc
}

aliases['SFweightMuDown'] = {
    'expr': 'LepSF3l__mu_'+muWP_new+'__Do',
    'samples': mc
}

