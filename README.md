## Shopify Data Science Internship Challenge

This repository contains my solution to the data science challenge for the Winter 2021 Shopify Internship

For reference datasets are contained in the data folder

### Quesiton 1

#### Reference dataset: "data/2019 Winter Data Science Intern Challenge Data Set - Sheet1.csv"


Given some sample data, write a program to answer the following: click here to access the required data set

On Shopify, we have exactly 100 sneaker shops, and each of these shops sells only one model of shoe. We want to do some analysis of the average order value (AOV). When we look at orders data over a 30 day window, we naively calculate an AOV of $3145.13. Given that we know these shops are selling sneakers, a relatively affordable item, something seems wrong with our analysis. 

    a Think about what could be going wrong with our calculation. Think about a better way to evaluate this data. 
    b What metric would you report for this dataset?
    c What is its value?

#### Solution: See the Analysis Notebook


### Question 2

#### Reference database: "orders_data.sqlite"

To re-create the database, run `python create_tables.py` to create the database and tables, and then `python etl.py` for the ETL process that copies data from csv files into the database

Please use queries to answer the following questions. Paste your queries along with your final numerical answers below.

    a How many orders were shipped by Speedy Express in total?
    b What is the last name of the employee with the most orders?
    c What product was ordered the most by customers in Germany?

#### Solution: See the Analysis Notebook