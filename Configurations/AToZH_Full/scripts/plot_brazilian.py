import argparse
import json 
import os
import re

import numpy as np
import matplotlib.pyplot as plt
import mplhep as hep

from plot_utils import CMSSW_BASE
from plot_utils import PlotMeta


plt.style.use(hep.style.CMS)

class BrazilianPlotter:

    tanb = 1
    BRAZILIAN_BLUE = "#002776"
    BRAZILIAN_GREEN = "#009C3B"
    BRAZILIAN_GOLD = "#FFDF00"

    def __init__(self, year, run_name):
	self.year = year
	self.run_name = run_name
        self.thdmc_brs = self.load_thdmc()
        self.brasilians = self.load_brasilians()
        print(f"Plotting {year}, {run_name}")


    def load_thdmc(self):
	with open(f"/afs/cern.ch/work/s/srudrabh/AZH/TheoryComputations/CMSSW_10_2_22/src/cp3_llbb/Calculators42HDM/AToZH_xsc_br_results.json", 'r') as f:
	    return json.load(f)

    def load_limits(self, mA, mH):
	 fname = f"AsymptoticLimits_AZH_mA-{mA}_mH-{mH}_2DEllipses.log"
	 with open(os.path.join("/pathtomylimitsdir", self.year, self.run_name, fname), 'r') as f:
             flines = [x for x in f if x.startswith("Expected")]

	 limit_vals = []
	 for line in flines:
	     pct_val = float(re.findall(r"\d.\d+", line.split("<")[1])[0])
	     limit_vals.append(pct_val)

         return limit_vals


    def load_brasilians(self):
	with open("signals.txt", 'r') as f:
	    mass_points = np.array([(int(re.findall(r"\d+", x)[0]), int(re.findall(r"\d+", x)[1])) for x in f])
	    a_masses = np.unique(mass_points[:, 0])
	    h_masses = np.unique(mass_points[:, 1])

	    brasilians = {
		"mA_fixed": {mA: np.sort([x[1] for x in mass_points if x[0] == mA]) for mA in a_masses},
		"mH_fixed": {mH: np.sort([x[0] for x in mass_points if x[1] == mH]) for mH in h_masses}
	}

        return brasilians

    def compute_theory_value(self, mA, mH):
	try:
	   br_z_ll = 0.066
	   br_h_tt = self.thdmc_brs[f"{mA},{mH}"]["HtottBR"]
           br_a_zh = self.thdmc_brs[f"{mA},{mH}"]["AtoZHBR"]
	   xsec_a = self.thdmc_brs[f"{mA},{mH}"]["xsec_ggH"]
        except KeyError:
	   return 1
	return xsec_a*br_a_zh*br_h_tt*br_z_ll


    def plot_common(self, ax):
	hep.cms.label(ax=ax, llabel="Work in progress", data=True,
		lumi=PlotMeta.YEAR_LUMI_MAP[self.year],
		year=PlotMeta.UL_YEAR_MAP[self.year])
	ax.set_ylabel(r"$\sigma(A) \times BR(A\rightarrow Z(l\bar{l})H(t\bar{t}))$")
	ax.legend()
        ax.set_yscale("log")

    def plot_fixed_mA(self):
	for mA, mHs in self.brasilians["mA_fixed"].items():
	    print(f"-- MA fixed at {mA} GeV")
	    limits = np.array([self.load_limits(mA, mH) for mH in mHs])
            fig, ax = plt.subplots(figsize=(12, 8))
            ax.fill_between(mHs, limits[:, 0], limits[:, 4], color=self.BRAZILIAN_GOLD, label=r"$2\sigma$")
	    ax.fill_between(mHs, limits[:, 1], limits[:, 3], color=self.BRAZILIAN_GREEN, label=r"$1\sigma$")
	    ax.plot(mHs, limits[:, 2], marker='D', linestyle='--', color=self.BRAZILIAN_BLUE, label="expected limit")
	    
	    
	    #Plot Theory Curves
	    theory_colors = ["red", "orange"]
	    theory_mHs = [i for i in range(min(mHs), min(1200, max(mHs) + 1), 2)]
	    for color in zip(theory_colors):
		theory_values = [self.compute_theory_value(mA, mH) for mH in theory_mHs]
		ax.plot(theory_mHs, theory_values, color=color, label=fr"2HDM type-II $\tan(\beta)=1")

	    ax.set_xlabel(fr"$m_H$ [GeV] ($m_A={mA}$)")
	    self.plot_common(ax)

            os.makedirs("plot_output/brasilians", exist_ok=True)
	    fname = f"MA-{mA}_{self.year}"
	    plt.savefig(f"plot_output/brasilians/{fname}.png")
	    plt.savefig(f"plot_output/brasilians/{fname}.pdf")
	    plt.close()


    def plot_fixed_mH(self):
	for mH, mAs in self.brasilians["mH_fixed"].items():
	    print(f"-- MH fixed at {mH} GeV")
	    limits = np.array([self.load_limits(mA, mH) for mA in mAs])
            fig, ax = plt.subplots(figsize=(12, 8))
            ax.fill_between(mAs, limits[:, 0], limits[:, 4], color=self.BRAZILIAN_GOLD, label=r"$2\sigma$")
	    ax.fill_between(mAs, limits[:, 1], limits[:, 3], color=self.BRAZILIAN_GREEN, label=r"$1\sigma$")
	    ax.plot(mAs, limits[:, 2], marker='D', linestyle='--', color=self.BRAZILIAN_BLUE, label="expected limit")

	    # Plot Theory Curves
	    theory_colors = ["red", "orange"]
	    theory_mAs = [i for i in range(min(mAs), min(1200, max(mAs) + 1), 2)]
	    for color in zip(theory_colors):
		theory_values = [self.compute_theory_value(mA, mH) for mA in theory_mAs]
		ax.plot(theory_mAs, theory_values, color=color, label=fr"2HDM type-II $\tan(\beta)=1")

            ax.set_xlabel(fr"$m_A$ [GeV] ($m_H={mH}$)")
	    self.plot_common(ax)

            os.makedirs("plot_output/brasilians", exist_ok=True)
	    plt.savefig(f"plot_output/brasilians/MH-{mH}_{self.year}.png")
	    plt.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("run_name", type=str, help="Name of the directory containing the inputs.")
    parser.add_argument("--year", type=str, help="all/UL16/UL17/UL18/ULCombined")
    args = parser.parse_args()


    if args.year in ["UL16", "UL17", "UL18", "ULCombined"]:
        YEARS = [args.year]
    if args.year == "all":
        YEARS = ["UL16", "UL17", "UL18", "ULCombined"]


    for year in YEARS:
        plotter = BrazilianPlotter(year=year, run_name=args.run_name)
        plotter.plot_fixed_mA()
        plotter.plot_fixed_mH()

