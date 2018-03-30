What years did AFI's best heroes and villains appear in theatres?

This is a Python project for Code Louisville Winter 2018. I took the data from American Film Institute's list of 100 Heroes and Villains. The data includes heroes, villains, the actors who played the characters, films, and film release dates. 

The scatter chart represents all heroes and villains on  the list arranged by year of film release. In the future, I want to add the information about each character on the list. I also want to make graphs showing all the films by year, genre, and Rotten Tomatoes scores.

To view this report:
1. Download the latest version of Python: https://www.python.org/downloads/

2. Download the following:
	-Pip: https://pip.pypa.io/en/stable/installing/
	-SQLite: https://www3.sqlite.org/download.html
	-Pandas: http://pandas.pydata.org/
	-NumPy: https://pypi.python.org/pypi/numpy (Numpy can also be installed via Pip)
	-Bokeh: https://bokeh.pydata.org/en/latest/docs/installation.html

	Bokeh also requires the following libraries to be installed: 
		-Jinja2 >=2.7: http://jinja.pocoo.org/
		-python-dateutil >=2.1: https://pypi.python.org/pypi/python-dateutil
		-PyYAML >=3.10: https://github.com/yaml
		-packaging >=17.1: https://pypi.python.org/pypi/packaging/
		-six >=1.5.2: https://pypi.python.org/pypi/six/1.5.2
		-tornado >=4.3: https://pypi.python.org/pypi/tornado/4.3	

3. Clone or download this repo.

4. In the project's root folder, run index.py

5. index.py will import the heroes and villains information from the included CSV and database files. The file index.html will generate the scatter plot representing the characters on the list with the year of film release.