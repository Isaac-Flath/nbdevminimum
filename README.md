# nbdev_minimum
> Notebook -> module conversion with #export flags and nothing else


**Purpose:**  The purpose and main use of this module is for adhoc projects where a full blown nbdev project is not necessary 

**Example Scenario** 

Imagine you are working on a kaggle competition. You may not want the full nbdev.  For example, you don't need separate documentation from your notebooks and you're never going to release it to pip or conda.  This module simplifies the process so you just run one command and it creates .py files from your notebooks.  Maybe you are doing an ensemble and to export the dataloaders from a notebook so you can import them into seperate notebooks for your seperate models, or maybe you have a seperate use case.

That's what this module does.  it's just the #export flags from nbdev and exporting to a module folder with no setup (ie settings.ini, \_\_nbdev.py, etc.) for fast minimal use

## Install

`pip install nbdev_minimum`

## How to use

### Full Directory Conversion

In python run the `simple_export_all_nb` function.  This will:
+ Look through all your notebooks in the directory (nbs_path) for any code cells starting with `#export` or `# export`
+ If any export code cells exist, it will take all the code and put it in a .py file located in `lib_path`
+ The .py module will be named the same as the notebook.  There is no option to specify a seperate .py file name from your notebook name
{% include warning.html content='Any .py files in your lib_path will be removed and replaced.  Do not set lib_path to a folder where you are storing other .py files.  I recommend lib_path being it&#8217;s own folder only for these auto-generated modules' %}


<h4 id="simple_export_all_nb" class="doc_header"><code>simple_export_all_nb</code><a href="https://github.com/Isaac-Flath/nbdev_minimum/tree/{branch}/nbdev_minimum/core.py#L38" class="source_link" style="float:right">[source]</a></h4>

> <code>simple_export_all_nb</code>(**`dir_path`**=*`Path('.')`*, **`lib_path`**=*`Path('src')`*)

clear_all_modules in lib_path
for each notebook in dir_path get_module_text and write_module_text to lib_path


### Single Notebook Conversion

In python run the `simple_export_one_nb` function.  This will:

+ Look through the specified notebook (nb_path) for any code cells starting with `#export` or `# export`
+ If any export code cells exist, it will take all the code and put it in a .py file located in `lib_path`
+ The .py module will be named the same as the notebook.  There is no option to specify a seperate .py file name from your notebook name


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-19-79bf977f9f06> in <module>
    ----> 1 show_doc(simple_export_one_nb)
    

    NameError: name 'simple_export_one_nb' is not defined

