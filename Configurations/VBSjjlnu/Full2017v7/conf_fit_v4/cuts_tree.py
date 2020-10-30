# cuts

# Second lepton veto already done in post-processing 
#and Lepton WP setup in samples.py
supercut = '(   (abs(Lepton_pdgId[0])==11 && Lepton_pt[0]>38)\
             || (abs(Lepton_pdgId[0])==13 && Lepton_pt[0]>30 ) ) \
            && Alt$(Lepton_pt[1],0)<=10 && Alt$(Lepton_isLoose[1],1)> 0.5 \
            && vbs_0_pt > 50 && vbs_1_pt > 30 \
            && PuppiMET_pt > 30 \
            && deltaeta_vbs >= 2.5  \
            && mjj_vbs >= 500 \
            && Mtw_lep < 185 \
            && (abs(vbs_0_eta)<2.65  || abs(vbs_0_eta)>3.139 || (Jet_puId[VBS_jets_maxmjj_massWZ[0]] & (1 << 0))==1) \
            && (abs(vbs_1_eta)<2.65  || abs(vbs_1_eta)>3.139 || (Jet_puId[VBS_jets_maxmjj_massWZ[1]] & (1 << 0))==1) \
            && (abs(vjet_0_eta)<2.65 || abs(vjet_0_eta)>3.139 || (Jet_puId[V_jets_maxmjj_massWZ[0]] & (1 << 0))==1) \
            && (abs(vjet_1_eta)<2.65 || abs(vjet_1_eta)>3.139 || (Jet_puId[V_jets_maxmjj_massWZ[1]] & (1 << 0))==1) \
            '


############ 
## Signal

cuts["res_sig_ele"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==11 \
                                && vjet_0_pt > 30 && vjet_1_pt > 30 \
                                && mjj_vjet > 65 && mjj_vjet < 105 \
                                && bVeto \
                                && w_had_pt < 200 \
                                && veto_fatjet_wjet90 \
                                '



cuts["res_sig_mu"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==13 \
                                && vjet_0_pt > 30 && vjet_1_pt > 30 \
                                && mjj_vjet > 65 && mjj_vjet < 105 \
                                && bVeto \
                                && w_had_pt < 200 \
                                && veto_fatjet_wjet90 \
                                '

cuts["boost_sig_ele"] = 'VBS_category==0 \
                            && abs(Lepton_pdgId[0])==11 \
                            && fatjetpt09 > 200 \
                            && mjj_vjet09 > 70 && mjj_vjet09 < 115 \
                            && bVeto \
                            '


cuts["boost_sig_mu"] = 'VBS_category==0 \
                            && abs(Lepton_pdgId[0])==13 \
                            && fatjetpt09 > 200 \
                            && mjj_vjet09 > 70 && mjj_vjet09 < 115 \
                            && bVeto \
                            '


###############
##### Wjets

cuts["res_wjetcr_ele"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==11 \
                                && vjet_0_pt > 30 && vjet_1_pt > 30 \
                                && mjj_vjet> 40 && (mjj_vjet <= 65 || mjj_vjet >= 105) \
                                && bVeto \
                                && w_had_pt < 200 \
                                && veto_fatjet_wjet90 \
                                '



cuts["res_wjetcr_mu"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==13 \
                                && vjet_0_pt > 30 && vjet_1_pt > 30 \
                                && mjj_vjet> 40 && (mjj_vjet <= 65 || mjj_vjet >= 105) \
                                && bVeto \
                                && w_had_pt < 200 \
                                && veto_fatjet_wjet90 \
                                '

cuts["boost_wjetcr_ele"] = 'VBS_category==0 \
                            && abs(Lepton_pdgId[0])==11 \
                            && fatjetpt09 > 200 \
                            && mjj_vjet09 > 40 && (mjj_vjet09 <= 70 || mjj_vjet09 >= 115)  \
                            && bVeto \
                            '

cuts["boost_wjetcr_mu"] = 'VBS_category==0 \
                            && abs(Lepton_pdgId[0])==13 \
                            && fatjetpt09 > 200 \
                            && mjj_vjet09 > 40 && (mjj_vjet09 <= 70 || mjj_vjet09 >= 115)  \
                            && bVeto \
                            '



###############
##### Top

### Top Tight region

cuts["res_topcr_ele"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==11 \
                                && vjet_0_pt > 30 && vjet_1_pt > 30 \
                                && mjj_vjet > 65 && mjj_vjet < 105 \
                                && bReqTight \
                                && w_had_pt < 200 \
                                && veto_fatjet_wjet90 \
                                '

cuts["res_topcr_mu"] = 'VBS_category==1 \
                                && abs(Lepton_pdgId[0])==13 \
                                && vjet_0_pt > 30 && vjet_1_pt > 30 \
                                && mjj_vjet > 65 && mjj_vjet < 105 \
                                && bReqTight \
                                && w_had_pt < 200 \
                                && veto_fatjet_wjet90 \
                                '


# Tight top
cuts["boost_topcr_ele"] = 'VBS_category==0 \
                            && abs(Lepton_pdgId[0])==11 \
                            && fatjetpt09 > 200 \
                            && mjj_vjet09 > 70 && mjj_vjet09 < 115 \
                            && bReqTight \
                            '


cuts["boost_topcr_mu"] = 'VBS_category==0 \
                            && abs(Lepton_pdgId[0])==13 \
                            && fatjetpt09 > 200 \
                            && mjj_vjet09 > 70 && mjj_vjet09 < 115 \
                            && bReqTight \
                            '