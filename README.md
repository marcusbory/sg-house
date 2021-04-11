# sg-house

sg-house is a Linear Regression project created by NUS CEG students Marcus Ong, Ng Andre, Muhammad Ashraf, and Mun Le Zong, to predict housing prices in Singapore, based on past datasets.

## Background

Using the HDB resale price dataset obtained in 2019, sg-house applies linear regression, a form of supervised machine learning, in order to investigate the relationship between HDB prices against the given criteria, and provide a reliable prediction of the housing prices. 

Current criteria used: 
- Floor Area in square metres
- Age of house
- Years of lease remaining

## Dependencies

Ensure that the dataset ```hdb_resale_price_Aug2019.csv``` is in the same directory as ```sg-house.py```.

As the program employs certain python3 libraries, check that the following packages are installed on your machine before running:
- numpy
- pandas
- matplotlib
- seaborn
- scikit-learn

### [pip3] To check
```
> pip3 list
```

### [pip3] To install
```
> pip3 install numpy
> pip3 install pandas
> pip3 install matplotlib
> pip3 install seaborn
> pip3 install scikit-learn
```

## Usage
```
usage: python3 sg-house.py
```
Note: The matplotlib plot may not appear if using WSL terminal for execution. Alternatively, run the code via GUI, such as Visual Studio Code or by double clicking the app.

## Inputs & Outputs
```
input:

Choose your town: 
What is the floor_area_sqm
What is the age
What is the remaining_lease_years

output:

Your estimated house price is 
```

## Roadmap for future
As the app is still in its development stage, we will be improving on it. Current plans include:
- Distance to primary schools in vicinity
- Distance to nearest MRT
- Improvement on data visualisation
- Scrape data directly from data.gov.sg for updated housing prices
- Distance to shopping centres and other amenities
