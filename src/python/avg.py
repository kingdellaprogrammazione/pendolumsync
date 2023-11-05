from pathlib import Path
from coordinate import Point

# Path setup

homedir = Path.home()
proj_path = "Documenti/università/sistemi_complessi/pendolum_sync"
list_prefix = ["sxpendolum", "dxpendolum", "sxcart","dxcart"]
extension = ".txt"

# Put tracking-files number

max_run_number = 3

# Load paths 
# Order: list_sxpendolum_paths, list_dxpendolum_paths, 
# list_sxcart_paths, list_dxcart_paths

paths_list = [[] for x in range(4)]

for i in range(max_run_number+ 1):
    for j in range(4):
        last_part = list_prefix[j] + "_" + str(i) + extension  
        complete_path = homedir / proj_path / "data" / last_part
        assert (complete_path.is_file()), "Filepath not found,upload max_run_number"
        paths_list[j].append( complete_path )

# Load files 
# Order: file_sxpendolum, file_dxpendolum,
# file_sxcart, file_dxcart

file_list = [[] for x in range(4)]

for i in range(len(file_list)):
    for j in paths_list[i]:
        file_list[i].append(open(j, "r"))

# Extract data from files

data_list = [[] for x in range(4)]
for i in range(len(data_list)):
    for j in file_list[i]:
        listalinee = j.readlines()
        for h in range(len(listalinee)):
            listalinee[h] = [float(x) for x in listalinee[h].split()]
        data_list[i].append(listalinee)

# Check number of instants for each file

tmp = len(data_list[0][0])
for i in data_list:
    for j in i:
        assert (tmp == len(j)), "istants not matching"

# Calculate average

avg_list = [[] for x in range(4)]

for i in range(len(data_list)):
    tmp_list = []
    for j in range(len(data_list[i][0])):
        for h in data_list[i]:
            tmp_list.append(h[j])
        avg_list[i].append([sum(x) for x in zip(*tmp_list)])
        tmp_list.clear()

for i in range(len(avg_list)):
    for j in range(len(avg_list[i])):
        avg_list[i][j] = [h/(max_run_number+1) for h in avg_list[i][j]]

# New average files

avg_paths_list = []

for i in list_prefix:
    last_part = i + "_avg" + extension  
    complete_path = homedir / proj_path / "data" / last_part
    avg_paths_list.append( complete_path )

for i in range(len(avg_paths_list)):
    file = open(avg_paths_list[i],'w')
    for j in avg_list[i]:
        file.write(str(j[0]) + " " + str(j[1]) + "\n")

print("Average files created")




