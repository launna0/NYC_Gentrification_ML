# NYC Gentrification Dashboard

Launna Atkinson, Christina He, Claudia Levi, Nidhi Pillai, Grace Wang

This project is a user-interactive dashboard aimed to analyze the factors that can help predict gentrification status. Using unsupervised k-means clustering, we have classified NYC neighborhoods as either gentrified, non-gentrified, or gentrifying. Interactive maps of the NYC neighborhoods allow users to select specific variables to view their proportion breakdowns by each classified neighborhood to greater understand the variables that influence gentrification status. The dashboard also contains an interactive sankey diagram that helps break down the racial and income demographics of each gentrification label. 

## SQL Database Setup

Due to the size and expanse of much of our data used to create this project, we decided to store each of the different files into a SQL database to effectively access and process each the data. 

Prior to running any of the Python code, the gentrification database must first be created using a SQL editor program. Within the root user localhost connection, each of the files in the "dump files" folder must be run in order to create and populate each of the tables. These files only need to be run once in order for the gentrification database to be available to access when creating the dashboard. 

### Root Password Storage
Since the database will be stored in the root user's localhost connection, the root password must be stored in order to gain access to the data. Edit the password.txt file, so that it contains only your root password and make sure to save the txt file afterwards. 

## Dashboard Deployment

In order to deploy the dashboard, simply run the dashboard.py file and follow the outputted link.

## Installations

The following packages used within this project must first be installed (if not already) in order to effectively run the dashboard.py file. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install these to your local environment. 

```bash
pip install dash_daq
```
```bash
pip install dash
```
```bash
pip install dash-bootstrap-components
```
```bash
pip install altair
```
```bash
pip install geopandas
```
```bash
pip install pandas
```
```bash
pip install numpy
```
```bash
pip install mysql-connector-python
```
```bash
pip install altair_viewer
```
```bash
pip install scipy
```
```bash
pip install pydeck
```
```bash
pip install dash-deck
```
