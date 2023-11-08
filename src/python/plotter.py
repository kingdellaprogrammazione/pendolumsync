import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import math
import ROOT
from ROOT import TMath, Math, TGraph, TF1
from pathlib import Path
from matplotlib.ticker import AutoMinorLocator

# Path setup
homedir = Path.home()
proj_path = "Documenti/università/sistemi_complessi/pendolum_sync"
list_prefix = ["sxpendolum", "dxpendolum", "sxcart", "dxcart"]
extension = ".txt"

paths_list = []

# Load paths
for i in list_prefix:
    last_part = i + "_avg" + extension
    complete_path = homedir / proj_path / "data" / last_part
    assert (complete_path.is_file()), "Filepath not found"
    paths_list.append(complete_path)

# Load files
# order: file_sxpendolum, file_dxpendolum, file_sxcart, file_dxcart]
file_list = []

for i in paths_list:
    file_list.append(open(i, "r"))

# Extract data from the list

data_list = []

for i in file_list:
    listalinee = i.readlines()
    for h in range(len(listalinee)):
        listalinee[h] = [float(x) for x in listalinee[h].split()]
    data_list.append(listalinee)
# in questa lista abbiamo prima il tipo di oggetto, poi il numero della run,
# dentro c'è una lista con le coordinate

# Define the functions for fitting


def h_t(x, par):
    # 0 = A, 1 = gamma, 2 = omega , 3 = beta
    xx = x[0]
    exponential = (TMath.Exp(-par[1] * xx / 2))
    cosine = TMath.Cos(par[2] * xx + par[3])
    y = par[0] * exponential * cosine + par[5]
    return y


def q_t(x, par):
    # 0 = A, 1 = gamma, 2 = omega , 3 = beta
    xx = x[0]
    exponential = (TMath.Exp(-par[1] * xx / 2))
    cosine = TMath.Cos(par[2] * xx + par[3])
    y = par[0] * exponential * cosine + par[5]
    return y


def obtain_distance(a, b):
    return math.sqrt(pow(a[0] - b[0], 2) + pow(a[1] - b[1], 2))


# Conversion from coordinates to angles
# Dx pendolum and cart
# Obtain the angle

# Calculate angles
list_tmp_dx = [data_list[1], data_list[3]]
list_angle_dx = []
assert (len(list_tmp_dx[0]) == len(list_tmp_dx[1])), "Different list lenghts"
for i in range(len(list_tmp_dx[0])):
    point_1 = list_tmp_dx[0][i]  # pendolum point
    point_2 = list_tmp_dx[1][i]  # cart point
    angle = TMath.ASin((point_1[0] - point_2[0]) /
                       obtain_distance(point_1, point_2)) * TMath.RadToDeg()
    # coordinate origin is in figure top left
    list_angle_dx.append(angle)

list_tmp_sx = [data_list[0], data_list[2]]
list_angle_sx = []
assert (len(list_tmp_sx[0]) == len(list_tmp_sx[1])), "Different lenght of lists"
for i in range(len(list_tmp_sx[0])):
    point_1 = list_tmp_sx[0][i]  # pendolum point
    point_2 = list_tmp_sx[1][i]  # cart point
    angle = TMath.ASin((point_1[0] - point_2[0]) /
                       obtain_distance(point_1, point_2)) * TMath.RadToDeg()
    # coordinate origin is in figure top left
    list_angle_sx.append(angle)

assert (
    len(list_angle_sx) == len(list_angle_dx)), "Different lenght of angle lists"

# Draw graphs
# Coordinate h = theta_1 + theta_2
# Coordinate q = theta_1 - theta_2
h_list = [x + y for x, y in zip(list_angle_sx, list_angle_dx)]
q_list = [x - y for x, y in zip(list_angle_sx, list_angle_dx)]

# Recalculate istants using exiftools for fps
fps = 25
instants_list = [i / fps for i in range(len(h_list))]

# Fit
graph_q = TGraph(len(q_list), np.asarray(instants_list), np.asarray(q_list))

# Defining the function: the numbers represent the interval of definition and the
#  number of free parameters

f_q = TF1("fit_q", q_t, 4.6, 53, 5)

# Set initial parameters with the help of desmos
f_q.SetParameters(16, 0.06, 3.4, 0, 0)

Math.MinimizerOptions.SetDefaultTolerance(0.01)

graph_q.Fit("fit_q", "", "", 4.6, 53)
fitted_q = graph_q.GetFunction("fit_q")

chiSquare_q = fitted_q.GetChisquare()

print("chisquare:" + str(chiSquare_q))
NDOF = fitted_q.GetNDF()
chireduced_q = chiSquare_q / NDOF
print("chisquared/NDOF:" + str(chireduced_q))

# Fit
graph_h = TGraph(len(h_list), np.asarray(instants_list), np.asarray(h_list))

# Defining the function: the numbers represent the interval of definition and the
# number of free parameters
f_h = TF1("fit_h", h_t, 4.6, 8.6, 5)

# Set initial parameters with the help of desmos
f_h.SetParameters(326, 1.2, 5.25, 1, 0)
f_h.SetParLimits(0, 0, 400)
f_h.SetParLimits(1, 0, 3)
f_h.SetParLimits(2, 0, 6)
f_h.SetParLimits(3, 0, 2)
f_h.SetParLimits(4, -0.5, 0.5)

# Modify the expected distance from minimum
Math.MinimizerOptions.SetDefaultTolerance(0.01)

# Remember to put limits in the fit directive
graph_h.Fit("fit_h", "", "", 4.6, 8.6)
fitted_h = graph_h.GetFunction("fit_h")

chiSquare_h = fitted_h.GetChisquare()

print("chisquare:" + str(chiSquare_h))
NDOF = fitted_h.GetNDF()
chireduced_h = chiSquare_h / NDOF
print("chisquared/NDOF:" + str(chireduced_h))

# Figure relative to q(t)

fig1 = plt.figure(1)

frame1_1 = fig1.add_axes((.1, .35, .8, .55))
frame1_1.set_xlabel("Istante (s)")
frame1_1.set_ylabel("q (°)")
frame1_1.set_title("Fit della funzione q(t) e residui")

frame1_1.yaxis.get_ticklocs(minor=True)
frame1_1.xaxis.get_ticklocs(minor=True)
frame1_1.minorticks_on()
frame1_1.yaxis.set_minor_locator(AutoMinorLocator(n=2))

frame1_1.grid(which='minor', alpha=0.2)
frame1_1.grid(which='major', alpha=0.5)

# Set display limits

frame1_1.set_xlim(0, 55)

newyfittedpoints_q = []
new_instants_q = np.arange(4.6, 53, 0.01)
for i in new_instants_q:
    newyfittedpoints_q.append(fitted_q.Eval(i))

line1_2 = plt.plot(instants_list,
                   q_list,
                   '.r',
                   markersize='4',
                   label='Dati acquisiti')
line1_3 = plt.plot(new_instants_q,
                   newyfittedpoints_q,
                   '-b',
                   markersize='3',
                   label='Fit')

yfittedpoints_q = []
for i in instants_list:
    yfittedpoints_q.append(fitted_q.Eval(i))

# Plot the difference between the fit and the points

difference_q = [a - b for a, b in zip(yfittedpoints_q, q_list)]

frame1_2 = fig1.add_axes((.1, .1, .8, .15))
frame1_2.set_xlabel("Istante (s)")
frame1_2.set_ylabel("$\Delta$ (°)")

frame1_2.yaxis.get_ticklocs(minor=True)
frame1_2.xaxis.get_ticklocs(minor=True)
frame1_2.minorticks_on()
frame1_2.yaxis.set_minor_locator(AutoMinorLocator(n=2))

frame1_2.grid(which='minor', alpha=0.2)
frame1_2.grid(which='major', alpha=0.5)

frame1_2.set_xlim(0, 55)

residual_q = plt.plot(instants_list[113:],
                      difference_q[113:],
                      '.r',
                      markersize='2',
                      label='Residui')

frame1_1.legend(loc='upper left', framealpha=0.95)

plt.savefig(homedir / proj_path / "media" / "plot" / "fit_q.pdf")

# Figure relative to q(t)

fig2 = plt.figure(2)

frame2_1 = fig2.add_axes((.1, .35, .8, .55))
frame2_1.set_xlabel("Istante (s)")
frame2_1.set_ylabel("h (°)")
frame2_1.set_title("Fit della funzione h(t) e residui")

frame2_1.yaxis.get_ticklocs(minor=True)
frame2_1.xaxis.get_ticklocs(minor=True)
frame2_1.minorticks_on()
frame2_1.yaxis.set_minor_locator(AutoMinorLocator(n=2))

frame2_1.grid(which='minor', alpha=0.2)
frame2_1.grid(which='major', alpha=0.5)

frame2_1.set_xlim(0, 14)

#ax.set_ylim(0.035,0.085)

newyfittedpoints_h = []
new_instants_h = np.arange(4.6, 8.6, 0.01)
for i in new_instants_h:
    newyfittedpoints_h.append(fitted_h.Eval(i))

line2_2 = plt.plot(instants_list,
                   h_list,
                   '.r',
                   markersize='4',
                   label='Dati acquisiti')
line2_3 = plt.plot(new_instants_h,
                   newyfittedpoints_h,
                   '-b',
                   markersize='3',
                   label='Fit')

frame2_1.legend(loc='upper left', framealpha=0.95)

yfittedpoints_h = []
for i in instants_list:
    yfittedpoints_h.append(fitted_h.Eval(i))

# Plot the difference between the fit and the points

difference_h = [a - b for a, b in zip(yfittedpoints_h, h_list)]

frame2_2 = fig2.add_axes((.1, .1, .8, .15))
frame2_2.set_xlabel("Istante (s)")
frame2_2.set_ylabel("$\Delta$ (°)")

frame2_2.yaxis.get_ticklocs(minor=True)
frame2_2.xaxis.get_ticklocs(minor=True)
frame2_2.minorticks_on()
frame2_2.yaxis.set_minor_locator(AutoMinorLocator(n=2))

frame2_2.grid(which='minor', alpha=0.2)
frame2_2.grid(which='major', alpha=0.5)

frame2_2.set_xlim(0, 14)

residual_h = plt.plot(instants_list[113:217],
                      difference_h[113:217],
                      '.r',
                      markersize='2',
                      label='Residui')

plt.savefig(homedir / proj_path / "media" / "plot" / "fit_h.pdf")

# Draw angles with time

fig3 = plt.figure(3)

frame3_1 = fig3.add_axes((.1, .1, .8, .8))
frame3_1.set_xlabel("Istante (s)")
frame3_1.set_ylabel("Angolo (°)")
frame3_1.set_title("Andamento degli angoli $\\theta_1$ e $\\theta_2$")

frame3_1.yaxis.get_ticklocs(minor=True)
frame3_1.xaxis.get_ticklocs(minor=True)
frame3_1.minorticks_on()
frame3_1.yaxis.set_minor_locator(AutoMinorLocator(n=2))

frame3_1.grid(which='minor', alpha=0.2)
frame3_1.grid(which='major', alpha=0.5)

frame3_1.set_xlim(2, 14)

#ax.set_ylim(0.035,0.085)

line3_1 = plt.plot(instants_list,
                   list_angle_sx,
                   '.r',
                   markersize='4',
                   label="$\\theta_1$")
line3_2 = plt.plot(instants_list,
                   list_angle_dx,
                   '.b',
                   markersize='4',
                   label="$\\theta_2$")

frame3_1.legend(loc='upper left', framealpha=0.95)

plt.savefig(homedir / proj_path / "media" / "plot" / "angles_accurate.pdf")

frame3_1.set_xlim(2, 50)

plt.savefig(homedir / proj_path / "media" / "plot" / "angles_full.pdf")

# Draw details

fig4 = plt.figure(4)

frame4_1 = fig4.add_axes((.1, .1, .8, .8))
frame4_1.set_xlabel("Istante (s)")
frame4_1.set_ylabel("Angolo (°)")
frame4_1.set_title("Andamento degli angoli $\\theta_1$ e $\\theta_2$")

frame4_1.yaxis.get_ticklocs(minor=True)
frame4_1.xaxis.get_ticklocs(minor=True)
frame4_1.minorticks_on()
frame4_1.yaxis.set_minor_locator(AutoMinorLocator(n=2))

frame4_1.grid(which='minor', alpha=0.2)
frame4_1.grid(which='major', alpha=0.5)

line3_1 = plt.plot(instants_list,
                   list_angle_sx,
                   '-r',
                   markersize='4',
                   label="$\\theta_1$")
line3_2 = plt.plot(instants_list,
                   list_angle_dx,
                   '-b',
                   markersize='4',
                   label="$\\theta_2$")

frame4_1.set_xlim(10, 50)
frame4_1.set_ylim(6, 8)

frame4_1.legend(loc='upper left', framealpha=0.95)

plt.savefig(homedir / proj_path / "media" / "plot" / "angles_decrease.pdf")

plt.show()
