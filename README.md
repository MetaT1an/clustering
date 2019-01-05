# Clustering
This is a lightweight software with gui for clustering analysis. Two popular clustering algorithms, k-means and DBSCAN, are offered to choose to work with. After data processing is completed, differences of performance in several aspects between the two algorithms will be displayed in charts, and as for the final result of clustering , you can save them as files suffixed with `.txt`

## Get started
### prerequisite
- [Python 3.6](https://www.python.org/downloads/release/python-366/)
- [PyQt5](https://pypi.org/project/PyQt5/)
- [matplotlib](https://matplotlib.org/)

### install
In this project, all the information about the dependences were stored in `Pipfile`, so I highly recommend you to use [Pipenv](https://pipenv.readthedocs.io/en/latest/) to manage it. If you have installed required packages in you system,  you can skip the following steps pertaining to Pipenv (2~4). 

1. Clone the whole project

```
git clone git@github.com:TYC6/clustering.git
```
2. Install Pipenv

```
python3 -m pip install pipenv
```

3. setup a working environment(this may take some time)

```
cd clustering/
pipenv install
```
4. activate the working environment

```
pipenv shell
```
5. run

```
python main.py
```

[Details about using Pipenv](https://github.com/TYC6/clustering/wiki/Details-about-using-Pipenv)

## Preview
![](https://ae01.alicdn.com/kf/HTB1eGLJasfrK1RkSnb45jXHRFXaz.gif)

![](https://ae01.alicdn.com/kf/HTB1TYHSaznuK1RkSmFP763uzFXaY.png)

## Caution
- please make sure the data-files comply with [Formatting rules for data-file](https://github.com/TYC6/clustering/wiki/Formatting-rules-for-data-file)
- please note that [The prerequisite for visualization](https://github.com/TYC6/clustering/wiki/Prerequisite-for-visualization)