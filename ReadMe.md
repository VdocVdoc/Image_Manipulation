Install PIL

python3 -m pip install --upgrade pip
python3 -m pip install --upgrade Pillow


Install Numpy
#CONDA
Best practice, use an environment rather than install in the base env
conda create -n my-env
conda activate my-env

# The actual install command
conda install numpy

#PIP
pip install numpy
