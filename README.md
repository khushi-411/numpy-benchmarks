# NumPy Benchmarks

Benchmarking NumPy in realistic situations.

## Usage

To run the benchmarks, you need to install the following libraries:
```
sudo pacman -S python-numpy
sudo pacman -S python-pythran
pip install transonic
sudo pacman -S python-llvmlite
sudo pacman -S python-setuptools
conda install numba
sudo pacman -S cmake
sudo pacman -S gcc
```

To Run the Files

1. Clone the Repository.
   ```
   git clone https://github.com/khushi-411/numpy-benchmarks
   ```

2. To execute NumPy and Python Code.
   ```
   taskset -c 6,7,14,15 python python/filename.py data/dataset_filename.txt
   ```
   *Note:* To obtain the accurate results the benchmarking is performed on the 4 isolated CPU cores (6, 7, 14, 15).

3. To execute Algorithms using Compiled Methods.
   ```
   transonic -b BACKEND python/filename.py
   TRANSONIC_BACKEND="BACKEND" taskset -c 6,7,15,16 python python/filename.py data/dataset_filename.txt
   ```
   
   Here, `-b` flag used to set the BACKEND (presently, there are 3 backends in Transonic; `cython`, `numba` and `python`. The default backend is `pythran`. Currently, we used `numba` and `pythran` for our implementation.

## Writing Benchmarks

Obtaining stable and reliable benchmark results requires to tune the system and to analyze the results manually.

Some things to consider:
- The first goal is to avoid the outliers caused by noisy applications.
- To set the system state for benchmarking use the [pyperf system tune command](https://pyperf.readthedocs.io/en/latest/cli.html#system-cmd).
- To reduce the system jitter refer [tune the system for benchmarks](https://pyperf.readthedocs.io/en/latest/system.html#system) page.

## File Structure
```
|-- cpp
    |-- main.cpp
|-- python
    |-- compiled_methods.py
    |-- numpy_python.py
    |-- plot.py
    |-- pure_python_particle.py
    |-- pure_python.py
|-- data
    |-- input files in the form of `inputX.txt`, where X = `16`, `32`, `64`, `128`, `256`, `512` and `1k`.
    |-- benchmark_output.csv
|-- images
|-- blog
|-- test
    |-- small tests to check the performance.
```

## Environment configuration

* **CPU Model:** Intel(R) Core(TM) i7-10870H CPU @ 2.20GHz
* **RAM GB:** 16
* **RAM Model:** DDR4
* **Speed:** 3200 MT/s
* **Operating System:** Manjaro Linux 21.1.1, Pahvo
* **Library Versions:**
    * Python: 3.9.6
    * NumPy: 1.20.3
    * Numba: 0.54.0
    * Pythran: 0.9.12.post1
    * Transonic: 0.4.10
    * GCC: 11.1.0
* **Note:** The benchmarking is performed on the $4$ isolated CPU cores for accurate results.

#### References
- [The issue for adding content on performance](https://github.com/numpy/numpy.org/issues/370)
- [Wikipedia's Article ob N-Body Problem](https://en.wikipedia.org/wiki/N-body_problem)
- [Pierre Augier's work on N-Body Problem](https://github.com/paugier/nbabel)
