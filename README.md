## NumPy Benchmarks

**Note:** This work will be published on [numpy.org](https://github.com/numpy/numpy.org).  

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

#### To Run the Files
1. Clone the Repository.
	```bash
	git clone https://github.com/khushi-411/numpy-benchmarks
	```
2. To run Python files.
	```bash
	taskset -c 6,7,14,15 python python/filename.py data/dataset_filename.txt
	```
3. To run C++ files.
	```bash
	g++ -o filename cpp/filename.cpp
	cat data/dataset_filename.txt | time ./filename
	```

#### Files
- `cpp/`: Consists of c++ code, used for implementing.
- `python/`: Codes for NumPy, Python, Pythran, Numba.
- `data/`: Six different text files, named as `inputX.txt`, where X is number of particles i.e. 16, 32, 64, 128, 256, 512 and 1000.

#### Dependencies
- Machine: 
	- vendor_id: GenuineIntel
	- model name: Intel(R) Core(TM) i7-10870H CPU @ 2.20GHz
	- RAM: 16GB
- Operating Systems:
	- DISTRIB_ID = ManjaroLinux
	- DISTRIB_RELEASE = 21.1.1
	- DISTRIB_CODENAME = Pahvo
	- DISTRIB_DESCRIPTION = "Manjaro Linux"
- Python: `3.9.6`
- NumPy: `1.20.3`
- Pythran: `0.9.12.post1`
- Transonic: `0.4.10`
- Numba: `0.54.0`
- CMake: `3.21.1`
- GCC: `11.1.0`

#### References
- [The issue for adding content on performance](https://github.com/numpy/numpy.org/issues/370)
- [Wikipedia's Article ob N-Body Problem](https://en.wikipedia.org/wiki/N-body_problem)
- [Pierre Augier's work on N-Body Problem](https://github.com/paugier/nbabel)
