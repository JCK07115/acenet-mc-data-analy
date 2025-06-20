#!/bin/bash
#SBATCH --time=00:03:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=256M
#SBATCH --output="ojsholola-report.out"

# add modules
module load python/3.13.2 
module list

# create a venv and install the pre-packaged requirements
echo $SLURM_TMPDIR
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_ENVDIR/bin/activate

pip install --no-index --upgrade pip
pip install --no-index -r requirements.txt

srun hostname

# run the weekly report generator using the specified files
python ojsholola-Project-HPC.py

