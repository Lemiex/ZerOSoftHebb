#!/bin/bash
#SBATCH --nodes=1
#SBATCH --cpus-per-task=4
#SBATCH --time=24:00:00
#SBATCH --partition=csc413
#SBATCH --job-name test
#SBATCH --gres=gpu
#SBATCH --output=test.out

python ray_search.py --preset 2SoftHebbCnnCIFAR --dataset-unsup CIFAR10_1 --dataset-sup CIFAR10_50 --folder-name 'CIFAR10_SoftHebb2' --save-model
