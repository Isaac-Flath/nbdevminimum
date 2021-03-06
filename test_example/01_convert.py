#export
import os, json, copy
from pathlib import Path

#export
def get_py_files(path): return [f for f in os.listdir(path) if f[-3:] == '.py']

#export
def get_cells_one_nb(path,file_name):

    file = open(path/file_name)
    Lines = file.readlines()

    split_flag = True
    cells = []
    i = -1
    
    for j,line in enumerate(Lines):
        split_criteria = line.startswith(('import ','from ','def ','class ','@',"if __name__ == '__main__':",))
        
        if split_flag != split_criteria:  cells[i].append(line)

        if split_criteria and split_flag:
            i+=1
            cells.append([])
            cells[i].append('#export\n')
            cells[i].append(line)
            split_flag = False
            

        if not split_flag and not split_criteria: split_flag = True    

    return cells

#export
def write_code_cell(code,single_code_cell=single_code_cell):
    out = copy.deepcopy(single_code_cell)
    out["source"] = code
    return out  

#export
def py_to_nb(py_path,nb_pth):
    blank_nb = {"cells": [],"metadata": {},"nbformat": 4, "nbformat_minor": 4}
    single_code_cell = {"cell_type": "code","execution_count": 0,"metadata": {},"outputs": [],"source": []}

    if not os.path.exists(nb_path): os.makedirs(nb_path)
    
    files = get_py_files(py_path)
    
    for i,file in enumerate(files): 
        out_file = f'{file[:-2]}ipynb'; print(f'writing {out_file}') # change extension
        nb = copy.deepcopy(blank_nb) # get new blank notebook dict
        cells = get_cells_one_nb(py_path,files[i]) # get cells that should be written
        for cell in cells: nb["cells"].append(write_code_cell(cell)) # add cells to dict
        with open(nb_path/out_file, 'w') as file: file.write(json.dumps(nb)) # write dict to json

