## QWorld's Silver 
Welcome to QWorld's Silver!


Silver is QWorld's intermediate level tutorial on quantum computing and programming focusing on complex numbers, QFT and Shor's Algorithm 

## Installation

In order to work with these jupyter notebooks, you need a number of packages. The following instructions ensure that the python verson and package versions are consistent and work with the notebooks.

1. Download this repository and extract it somewhere.

Then either use Conda, venv or virtualenv as follows.

### Conda (Recommended)

The following two steps are for installing the required packages.

1. Open a terminal or command prompt at the directory where you extracted the files.
2. Run the following command to create a new Conda environment and install all necessary packages.

```bash
conda env create -f environment.yml
```

The following steps should be followed every time you want to work on the notebooks.

1. Activate the Conda environment.

```bash
conda activate silver
```

After activation, your command prompt or terminal prompt should change to indicate that you are now working within the virtual environment. 

2. You can now launch jupyter notebook.

```bash
jupyter notebook
```

3. Deactivate the Conda environment when you're done.

```bash
conda deactivate
```


### Using venv or virtualenv

1. Make sure you are using Python 3.11.8
2. Open a terminal or command prompt at the directory where you extracted the files.
3. Run one of the following commands (depending on whether you want to use venv or virtualenv) to create a virtual environment.

```bash
# create environment using venv
python -m venv silverenv
# OR create environment using virtualenv
pip install virtualenv
virtualenv silverenv
```

4. Activate the virtual environment.

On Windows
```bash
silverenv\Scripts\activate
```

On macOS or Linux:
```bash
source silverenv/bin/activate
```

After activation, your command prompt or terminal prompt should change to indicate that you are now working within the virtual environment.

5. Install packages using pip. 

```bash
pip install -r requirements.txt
```

If you are a Mac OS user you might need to install the qiskit[visualization] in the following way
```bash
pip install 'qiskit[visualization]'
```

6. You can now launch jupyter notebook.

```bash
jupyter notebook
```

7. Deactivate the Conda environment when you're done.

```bash
conda deactivate
```

Every time you work on the notebooks, you should reexecute steps 4, 6 and 7, remembering to switch to the directory where you created the virtual environment.

**Using Binder:** _You may [launch Silver in the cloud with binder](https://mybinder.org/v2/gl/qworld%2Fsilver/HEAD?urlpath=lab/tree/content.ipynb) but **please be aware of that**_ 
- _each time a new session is created, which takes some time to be initiated, and all changes are lost when ending the session; and,_
- _the session might be terminated if a new tab is not opened within 10 minutes._
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gl/qworld%2Fsilver/HEAD?urlpath=lab/tree/content.ipynb) 
</small>

## Credits

Most of the <font style="color: #A9A9A9;"><b><i>Silver</i></b></font> is prepared under the project QPool2019 [GitLab repository](https://gitlab.com/qkitchen/qpool2019) in 2019-2020 and it is expected to have contributions from public as well. 

We would like to thank participants of the QSilver Revision Week organized in January 2021 and the participants of the QSilver Pilot Workshop organized in April 2021 for revising the material.


#### Introduction to Complex Numbers, Bloch Sphere, Operations with Complex Numbers

This part is developed by Dr. Maksim Dimitrijev(<a href="https://qworld.net/qlatvia/" target="_blank">QLatvia</a>). <a href="https://people.fjfi.cvut.cz/gabriaur/ " target="_blank">Dr. Aurél Gábris</a> (<a href="https://qworld.net/qczech/" target="_blank">QCzech</a>) contributed by providing additional content.     

#### Quantum Fourier Transform and Shor's Algorithm

This section is developed by <a href="https://www.cmpe.boun.edu.tr/~ozlem.salehi/" target="_blank">Dr. Özlem Salehi.</a>.

#### QSaudi Arabia QSilver39 — Qiskit Port (2026)

The Quantum Fourier Transform / Shor's Algorithm notebooks (D02–D06), originally implemented in Cirq, were ported to Qiskit by **Ahmed Elghadban** for the QSaudi Arabia QSilver39 course (KACST / Academy 32), together with the accompanying training presentation. All "on paper" math content is preserved unchanged from the original; only the circuit-implementation code was rewritten for Qiskit. See each notebook's header for the specific tasks affected.


## Making Contributions

If you are interested, you are welcome to contribute to Silver. Please read QWorld's rules for developing projects.

http://qworld.lu.lv/wp-content/uploads/2020/09/Rules-for-the-projects-developed-under-the-QEducation-2020-Sep-22.pdf


## License

The text and figures are licensed under the Creative Commons Attribution 4.0 International Public License (CC-BY-4.0), available at https://creativecommons.org/licenses/by/4.0/legalcode.

The code snippets in the notebooks are licensed under Apache License 2.0, available at http://www.apache.org/licenses/LICENSE-2.0.