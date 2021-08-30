### NumPy Benchmarks

#### Basic Library Installation
- NumPy: `sudo pacman -S python-numpy`
- Pythran: `sudo pacman -S python-pythran`
- Transonic: `pip install transonic`
- Numba:
	- llvmlite: `sudo pacman -S python-llvmlite`
	- setuptools: `sudo pacman -S python-setuptools`
	- Numba: `conda install numba`
- CMake: `sudo pacman -S cmake`
- GCC Compiler: `sudo pacman -S gcc`

#### To Run Files
1. Clone the Repository.
	```
	git clone https://github.com/khushi-411/numpy-benchmarks
	```
2. To run Python files.
	```
	taskset -c 6,7,14,15 python python/filename.py data/dataset_filename.txt
	```
3. To run C++ files.
	```
	g++ -o filename cpp/filename.cpp
	cat data/dataset_filename.txt | time ./filename
	```

#### Dependencies
- Python: 3.9.6
- NumPy: 1.20.3
- Pythran: 0.9.12.post1
- Transonic: 0.4.10
- Numba: 0.54.0
- CMake: 3.21.1
- GCC: 11.1.0


