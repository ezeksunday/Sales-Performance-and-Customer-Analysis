![SALES PERFORMANCE INSIGHTS ANALYSIS](Screenshot 2024-09-19 at 15.49.31)


### OVERVIEW  
The project focuses on analysing Walmart's retail sales data to uncover key insights into sales performance, customer behaviour, product trends, and operational efficiency.  
By leveraging data analytics, the project aims to provide actionable insights that can help optimize business operations, improve customer satisfaction, and drive profitability.  
The analysis is conducted using MySQL for data pre-processing and analysis, while Tableau is employed to create clear and impactful visualizations.

### AIM  
The aim of the project is to analyse Walmart's sales data to gain insights into sales dynamics, customer behaviour, and profitability. This analysis will help optimize Walmart's operations, marketing, and inventory management by identifying time-based trends and providing actionable recommendations.

#### TOOLS UTILIZED:  
•	MySQL Server  
•	MySQL Workbench   
•	Tableau

### ABOUT THE DATASET  
The dataset use for this analysis was obtained from Kaggle Walmart Sales Forecasting Competition. It contains sales transaction data from three different Walmart branches, located in Mandalay, Naypyidaw , and Yangon. The dataset consists of 17 columns and 100 rows.

### COLUMNS IN THE DATASET
- Invoice ID: A unique identifier for each transaction. This can be used to track individual sales and link various items purchased in the same transaction.  
- Branch: Represents different store branches (e.g., A, B, C). This helps in comparing sales performance across different locations.  
- City: The city where the transaction took place (e.g., Yangon, Naypyitaw, Mandalay). This allows for regional sales analysis.  
- Customer Type: Indicates whether the customer is a "Member" or "Normal" (non-member). This can be used to analyse customer loyalty and the impact of membership on sales.  
- Gender: The gender of the customer (Male, Female). This allows for demographic analysis of sales.  
- Product Line: The category of the product purchased (e.g., Health and beauty, Electronic accessories). This helps in understanding which product lines are performing well.
- Unit Price: The price per unit of the product sold. This is essential for calculating total revenue and understanding price sensitivity.
- Quantity: The number of units purchased in a single transaction. This helps in calculating the total revenue per transaction and understanding customer purchase behaviour.
- VAT (Tax 5%): The tax amount for each transaction, calculated as 5% of the cost of goods sold (COGS). This is useful for financial analysis and understanding the tax contribution to the total cost.
- Total: The total amount paid by the customer, including tax. This is the key metric for revenue analysis.
- Date: The date of the transaction. This allows for time-based analysis such as monthly sales trends, day-of-week analysis, and seasonal patterns.
- Time: The time at which the transaction occurred. This is useful for understanding peak shopping hours.
- Payment Method: The payment method used by the customer (e.g., E-wallet, Cash, Credit card). This helps in understanding customer preferences for payment methods.
- COGS (Cost of Goods Sold): The direct cost of the goods sold in the transaction. This is important for profitability analysis.
- Gross Margin Percentage: The percentage of revenue that exceeds the COGS, calculated as (Gross Income / Total Sales) * 100. This is a key metric for understanding the profitability of each sale.
- Gross Income: The income generated from the transaction after deducting COGS. This helps in analysing overall profitability.
- Rating: The customer rating for the transaction (on a scale from 1 - 10). This provides insights into customer satisfaction and product/service quality.

It is very obvious that there are no missing values in the table, as this issue was resolved during the initial table creation process i.e., NOT NULL is set for each field.

### INSIGHT FROM THE DATASET:   
1.	Branch and City Sales Analysis:   
- Objective: To evaluate overall sales performance across different branches and cities.  
- Purpose: Identify which branches or cities are performing the best in terms of total sales and profitability. 
Helps to identifying which branch could benefit from specific strategic interventions and resource allocation.
2.	Customer Behaviour Analysis:   
- Objectives: To understand the purchasing behaviour of different customers by their gender and customer type. For instance, are members buying more than non-members? Do male or female customers prefer certain product lines?
- Purpose: Tailor marketing strategies, promotions, and customer loyalty programs to better meet the needs of different customer groups.
3.	Product Line Analysis:    
- Objective: To assess the profitability and customer satisfaction associated with different product lines.
- Purpose: Focus on promoting high profit-margin and popular products based on sales and rating while identifying underperforming lines for improvement or discontinuation.
This can inform inventory and marketing decisions.
4.	Payment Method Preferences:    
- Objective: To explore customer preferences for payment methods e.g., cash, credit card, e-wallet. 
To understand which payment methods are most popular among customers. 
- Purpose: Ensure that the most preferred payment options are available and consider introducing new payment methods that could enhance the customer experience.
Detailed analysis of sales by payment methods helps inform decisions around payment options offered.

5.	Time-Based Trends:   
- Objective: To analyse sales trends and patterns over time, including days, months, and season. 
- Purpose: Optimize store operations, staffing, and promotional activities to align with peak sales periods across different branches and to improve overall efficiency.
6.	Customer Satisfaction Insight:   
- Objective: To track customer satisfaction through ratings provided in transactions.
- Purpose: Identify areas where the customer experience can be improved, such as product quality, service speed, or store ambiance, and take corrective actions to enhance customer loyalty. To identify the overall satisfaction levels and identify areas for improvement.

7.	Strategic Decision-Making
- Objective: To provide data-driven insights that inform strategic decisions at various levels of the organization.
- Purpose: Support long-term planning, such as expansion into new locations, adjusting product offerings, or redesigning marketing strategies to align with data insights.
8.	Expansion Planning  
- Objective: To assess the feasibility of expanding to new locations or introducing new product lines based on sales and customer behaviour data.
- Purpose: Support data-driven decisions regarding store expansions, product launches, or entering new markets.
9.	Inventory Management  
- Objective: To optimize inventory levels based on sales data, ensuring that popular items are always in stock while reducing overstock of less popular items.
- Purpose: Improve inventory turnover rates and reduce storage costs, leading to a more efficient supply chain.


## Business Decisions Questions to Answer

### Generic Questions:
1.	How many unique cities are represented in the data?
2.	How many unique branches are there?
3.	In which city is each branch located?
4.	How many different types of customers are represented in the data?
5.	How many unique payment methods are used?
6.	How many unique product lines does the data have?  

### Sales and Revenue Questions:  
7. What is the most popular payment method?  
8.	What is the total revenue for each payment method?  
9.	What is the total revenue generated by each product
       line?  
10.	What product line generated the most revenue?  
11.	What is the best-selling product line?  
12.	Which product line had the highest VAT costs?  
13.	What is the total revenue for each month?  
14.	Which month had the highest costs of goods sold (COGS)?  
15.	What is the total revenue generated in each city?  
16.	Which city had the highest total revenue?  
17.	What is the total revenue for each customer type?  
18.	Which customer type is most common?  
19.	Which customer type makes the most purchases?  
20.	What is the dominant gender among customers?  
21.	What is the total revenue generated by each branch?  
22.	How are customers distributed by gender across different branches?  
23.	What is the revenue generated  by gender?( Also Categorised as Product Performance)  
24.	How does revenue vary by gender and customer type?  
25.	How much revenue does each gender contribute?  
26.	What is the sales performance of each product line by gender?  

### Product Performance and Customer Feedback Questions:  
27.	Categorize product lines as "Good" or "Bad" based on their sales performance relative to the average.  
28.	Which branch sold more products than the average?  
29.	What is the most common product line among different genders?  
30.	What is the number of sales made in each part of the day per weekday?  
31.	What is the average rating of each product line?  
32.	Which customer type brings the most revenue?  
33.	Which city has the largest tax/VAT percentage?  
34.	Which customer type pays the most in VAT?  
35.	At what times of day do customers most frequently leave ratings?  
36.	When do customers leave the most ratings at each branch?  
37.	Which day of the week has the highest average ratings?  
38.	Which day of the week has the highest average ratings at each branch?  
39.	How do customers rate products by gender?  
40.	How do customers rate products by product line?   



### Feature Engineering
Involve generating additional columns from the existing ones. It helps us to creates new columns by transforming the existing ones.
Therefore, we are going to extract months and days from Date column and time of the day from the Time column, this will enable us to spot and analyse sales trends by months, days of the week and a particular time the transaction occur. 
- Month name: Contains the extracted months of the year in which the transaction occurred (Jan, Feb, Mar). It helps identify which month of the year that generates the highest sales and profits.
- Day name: Contains the extracted days of the week in which the transaction occurred (Mon, Tues, Wed, Thurs, Fri, and Sat). It. helps to determine the busiest day of the week and with the peak sales.
- Time of day: Gives insights of the sales in the morning, afternoon and evening. Help to determine the part of the day with most sales.

## Exploratory Data Analysis (EDA))  
### Descriptive Statistics Analysis  
Summarizes and describes the main features of a dataset. It provides simple summaries and insights about the data through various measures. These summaries can either be numerical or graphical and help in understanding the distribution, central tendency, and variability of the data. 
Hence, some major numerical insights from the datasets are: 
- Unit Price: Ranges from $10.08 to $99.96, with an average of $55.69.
- Quantity: Customers typically purchase between 1 and 10 units, with an average of 5.50 units.
- VAT: The 5% tax amount varies between $0.51 and $49.65, with an average of $15.36.
- Total Sales: Sales range from $10.68 to $1,042.65, with an average of $322.50.
- Gross Income: Average gross income per transaction is $15.36.
- Customer Rating: The ratings range from 4.0 to 10.0, with an average of 6.95.

## Sales, Product Performance and Customers Feedback Analysis  
### Sales Analysis by Payment Method
- Cash: $112,206.57 (Most used)  
- E-wallet: $108,330.04  
- Credit card: $100,349.78 (Least used)  
  
Cash is the most preferred payment method, followed closely by E-wallets.  

### Sales by Product Line
-   Top-selling categories:  
o	Food and Beverages: $56,144.84  
o	Fashion Accessories: $54,305.90  
o	Sports and Travel: $53,936.13  
o	Home and Lifestyle: $53,861.91  
o	Electronic Accessories: $53,783.53   
- Lowest-selling category:    
o	Health and Beauty: $48,854.38  

### Sales by Month:  
- January: $116291.8680  
- February: $95727.3765  
- March: $108867.1500 
   
January had the highest total revenue, followed by March and then February.  
### Sales Analysis by Branch  
- Branch A: $105,861.01  
- Branch B: $104,534.61  
- Branch C: $110,490.78 (highest)  
### Sales by City:   
- Naypyitaw: $110,490.78  
- Yangon: $105,861.01  
- NMandalay: $104,534.61  
  
Naypyitaw top the sales record with a total of  $110,490.78 followed by Yangon with $105,861.01 sales.   
Mandalay recorded the least sales of $104,534.61.
### Sales  by Customer Type 
- Member:	$163,625.10  
- Normal:	$157,261.29 
   
Member customers have generated slightly higher total sales of  $163,625.10 than the Normal customers with $157,261.29.  
Member customers also have a slightly higher average gross income of $15.6 per transaction compared to the Normal Customers with  $15.10 average gross gain.
### Sales Analysis by Gender  
- Female customers contribute more to sales ($166,390.93) compared to the male customers ($154,495.47).  
- Female customers also had a higher average gross income ($15.94) per sale compared to male customers ($14.77). 
   
This data indicates that female customers contribute more both in terms of total sales and profitability per transaction compared to male customers. This could be useful for tailoring marketing strategies or customer engagement based on gender-specific insights.

### Customer Sales Analysis by Gender and Customer Type  
- Female members have the highest total sales ($87,548.60) and the highest average gross income ($16.09).  
- Male members have the lowest total sales ($76,076.50) but still maintain a decent average gross income ($15.09).  
- Normal female and male customers have similar total sales, but females slightly outperform males in terms of both sales and average gross income.  
### Product Line Customer Analysis by Gender
- Female customers tend to spend more on Fashion accessories and Home and lifestyle products compared to Male customers.  
- Male customers tend to spend more on Electronic accessories and Sports and travel products compared to Female customers.  
- Food and beverages are a popular product line for both genders, with Female customers spending slightly more than Male customers.  
  
This analysis can help identify product categories that are more appealing to specific genders and inform marketing and inventory strategies.  
### Product Rating by Gender
- Female customers tend to rate Food and beverages higher than Male customers.  
- Male customers tend to rate Electronic accessories and Sports and travel higher than Female customers.  
- Health and beauty products have a relatively high average rating for both genders with the Female rating slightly higher.  
- Home and lifestyle products have a lower average rating overall.
  
Product Line	    - Gender  - 	Avg_Rating  
- Food and beverages	Male	7.01667  
- Food and beverages	Female	7.20333  
- Health and beauty	Female	7.10159  
- Health and beauty	Male	6.89886  
- Sports and travel	Male	7.04675  
- Sports and travel	Female	6.69186  
- Fashion accessories	Male	6.92195  
- Fashion accessories	Female	7.12083  
- Home and lifestyle	Male	6.90988  
- Home and lifestyle	Female	6.76329  
- Electronic accessories	Male	7.05930  
- Electronic accessories	Female	6.74819   

This analysis can help identify product categories that are more appealing to specific genders and inform product development and marketing strategies.

### Customers Rating by Gender
Male: Total rating of 498 with Average of 6.97  
Female: With a Total rating of 497 with Average of  6.94.  
There is no significant difference in rating gender-wise, hence, Male top with just a little on scale than the female.
