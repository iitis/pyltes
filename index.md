---
title: PyLTEs
---

# PyLTEs

PyLTEs is a framework that allows to evaluate model of protocols/mechanisms/approach for LTE networks. Because of the wide flexibility it is hard to determine what is possible in them. It is easier to define, that this framework gives an opportunity to develop your own models. Currently there is few use-cases, for which PyLTEs was used.

#Opportunities:
* analyse the average signal level (SINR) in a network,
* evaluate throughput of users in a network,
* find the optimal Tx power of eNodeBs,
* evaluate different Frequency Reuse.

Repository can be found here: [PyLTEs](https://github.com/iitis/PyLTEs)

>This software is a sub-output of [PhD thesis](https://www.iitis.pl/~mslabicki/). It is still under development, so you use it on your own responsibility. Do not give it to children and do not insert it into microwave oven. Remember: software is not a state - it is a process.

# Requirements:
* Python (tested for Python3.5)
* matplotlib
* numpy
* [PyGMO](http://esa.github.io/pygmo/) -- if you plan to use optimization module (you can omit it if you don’t know yet)

# How to run:
Download PyLTEs repository. You can make it via git or manually. In directory "PyLTEs" create a file “firstNetwork.py” and copy below code:
```python
network = CellularNetwork()
network.Generator.create1BSnetwork(1666)

network.Generator.insertUErandomly(20)
network.connectUsersToTheBestBS()

network.Printer.drawHistogramOfUEThroughput("thrHistogram")
network.Printer.drawNetwork(fillMethod="SINR", filename="sinrMap")
```
In terminal runs
```bash
python3.5 firstNetwork.py
```
After few seconds you should see an output on the terminal, and few files in the directory. Have fun!
Note: if you have other Python version you should run this script with your Python.

# Examples:
Download these files, copy to the directory with PyLTEs (as code from “How to run”) and run in Python:
python3.5 small_network_sinr.py
python3.5 small_network_sectors.py
and so on...

# Research papers that used PyLTEs:
* P. Masek, J. Hosek, Y. Zakaria, D. Uhlir, V. Novotny, M. Slabicki, K. Grochla, "Experimental Evaluation of RAN Modelling in Indoor LTE Deployment," in Ultra Modern Telecommunications and Control Systems and Workshops (ICUMT), 2015 7th International Congress on, Brno 2015
* Slabicki, Mariusz, and Krzysztof Grochla. "Local Approach to Power Management in LTE Networks" 38th International Conference on Telecommunications and Signal Processing (TSP), 2015. 
* Grochla, Krzysztof, and Konrad Połys. "Subcarrier Allocation for LTE Soft Frequency Reuse Based on Graph Colouring." Information Sciences and Systems 2015: 30th International Symposium on Computer and Information Sciences (ISCIS 2015). Vol. 363. Springer, 2015.
* Słabicki, Mariusz, and Krzysztof Grochla. "The Automatic Configuration of Transmit Power in LTE Networks Based on Throughput Estimation.", IEEE 33rd International Performance Computing and Communications Conference (IPCCC), 2014

Please let me know if you used this tool, I will be more than happy to add your paper here.

# Todo / Work in Progress:
* documentation,
* functions to generate network (in file generator.py),
* code cleaning (there is a lot to do),
* improve this page.

# Contributors:
* Mariusz Słabicki - main creator [www]( https://www.iitis.pl/~mslabicki/)
* Konrad Polys - sereval small, but important improvements

# Call for participation:
If you see any opportunity to contribute to this project, do not hestitate!
