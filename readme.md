These are examples of using montecarlo methods to solve linear programing problems explained in this guides:

 http://www.osemosys.org/uploads/1/8/5/0/18504136/ceron_-_2006_-_the_gnu_linear_programming_kit,_part_1_-_introduction_to_linear_optimization.pdf

 http://www.osemosys.org/uploads/1/8/5/0/18504136/ceron_-_2006_-_the_gnu_linear_programming_kit,_part_2_-_intermediate_problems_in_linear_programming.pdf

 http://www.osemosys.org/uploads/1/8/5/0/18504136/ceron_-_2006_-_the_gnu_linear_programming_kit,_part_3_-_advanced_problems_and_elegant_solutions.pdf


To run them you can install conda python:

#installing Miniconda on Mac

$wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O miniconda.sh

$bash miniconda.sh -p miniconda

##Creating a new conda environment called mc_experiments (you ca call it whatever you want).
# I install also pandas which is a very useful package.

$conda create --name mc_experiments pandas

##Activating it

$source activate mc_experiments
