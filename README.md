# Stanford Geothermal Python-Sessions -- Intermediate Advanced

## Overview
### Who, when, what


### Structure
The workshop is a mix of lecture and code-along using Jupyter Notebooks. 

## Pre-requites
Below is what I expect you to already know and have installed if you want to participate in the code-along portion of this workshop. You are welcome to attend if you do not meet these pre-requisites but, as this session is designed for intermediate and above, we will be providing limited beginner-level support.

- Familiarity with the syntax of Python including for-loops
- Able to make a basic plot using matplotlib
- OTHER?

***
# Setup Instructions

The workshop material is in Jupyter Notebooks and uses the packages listed in the environment.yml file. Feel free to use your preferred code editor (I prefer VS Studio Code or Jupyter Lab). If you have not already worked with these file type or are unfamiliar with environments, I recommend using the step-by-step instructions below.

## Anaconda Instructions

Download this tutorial from GitHub using the green 'code' button and unzip to somewhere that is easy to find, such as your Documents folder.
 
Download and instal [Anaconda individual edition](https://www.anaconda.com/products/individual) if you don't already have it. When prompted, accept the default installation settings.

In Windows open the anaconda prompt or in macOS open a terminal. Use the prompt/terminal to navigate to where you have saved this repository (hint: use _cd \<path_to_the_repository\>_ to change directory)
 
In the repository folder, you will find an environment.yml file (hint: use _ls_ in MacOS or _dir_ in Windows to list files in your current directory). We will use this file to create an environment that contains the packages we need during the workshop. Execute the following command in the prompt/terminal to create the environment (hint: do not include the $ sign):
 
    $ conda env create -f environment.yml
 
You will see a lot of text scroll past in the the prompt/terminal and may need to respond y + ENTER at some point. The environment is automatically named workshop_env. Once it has built, we need to activate the environment by executing:
 
    $ conda activate workshop_env
 
\(workshop_env\) should now appear on the far left of your current line in the prompt/terminal window. Now you are inside the right environment, you can execute the following command to launch a browser window containing Juypter notebook:
 
    $ jupyter notebook
 
Now you can open the tutorial notebooks and use them. 

When you are finished with Juypter Notebook, you can close the browser window and go back to the prompt/terminal to kill the process with CTRL + C.
 
When you come back to the workshop material at a later date, you will probably have to activate the workshop_env environment again before launching Juypter Notebook.
 
**Other useful commands**
 
Print a list of your conda environments
  
    $ conda env list
 
Print a list of what is inside your active environment
  
    $ conda list

To install an additional package into the active environment

    $ pip install <PackageName>

***
## Binder Instructions (Backup)

 Click the Binder button below and wait for it to load. The first time you do this, Binder can take up to 10 minutes to load. Click 'show' on the 'Build Logs' bar if you want to watch the Binder environment building. 
 
 When Binder has loaded, it will open the tutorial in Jupyter Lab. You can edit and run the code there. You can also save your work and have it retained during that Binder session. However, once you close your browser, any saved work will be lost. 


BINDER LINK HERE
 
