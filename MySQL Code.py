-- ------------------------------ Create the database that would hold our table -------------------------------
CREATE DATABASE Walmart;

-- ---------------------------------------------- Create  the Table -------------------------------------------
CREATE TABLE Walmartsales(
	Invoice_ID VARCHAR (20) NOT NULL PRIMARY KEY,
    Branch VARCHAR (3) NOT NULL,
    City VARCHAR (20) NOT NULL,
    Customer_type VARCHAR (20) NOT NULL,
    Gender VARCHAR (10) NOT NULL,
    Product_line CHAR (50) NOT NULL,
    Unit_price DEC (10, 2) NOT NULL,
    Quantity INT NOT NULL,
    VAT DEC (10,4) NOT NULL,
    Total DEC (10, 4) NOT NULL,
    Date DATETIME NOT NULL,
    Time TIME NOT NULL,
    Payment_mathod VARCHAR (20) NOT NULL,
    COGS DEC (10, 2) NOT NULL,
    Gross_mergin_ptg DEC (12, 10) NOT NULL,
    Gross_income DEC (10, 4) NOT NULL,
    Rating DEC (2, 1)
);
SELECT * FROM Walmartsales;
-- Load data into the table using  Data Import Wizard......

-- -------------------------------------------------------------------------------------------------------------
-- --------------------------------------------- FEATURE ENGINEERING -------------------------------------------

-- ---- Time_of_date
SELECT Time FROM Walmartsales;  --  Print Time column

SELECT Time,	CASE
					WHEN TIME_FORMAT(Time, '%H:%i:%s') BETWEEN '00:00:00' AND '12:00:00' THEN 'Morning'
					WHEN TIME_FORMAT(Time, '%H:%i:%s') BETWEEN '12:01:00' AND '16:00:00' THEN 'Afternoon'
					ELSE 'Evening'
				END AS Time_of_date
FROM Walmartsales;

ALTER TABLE Walmartsales
ADD COLUMN Time_of_date VARCHAR(10)
AFTER Gross_income;

UPDATE Walmartsales
SET Time_of_date = CASE
						WHEN TIME_FORMAT(Time, '%H:%i:%s') BETWEEN '00:00:00' AND '12:00:00' THEN 'Morning'
						WHEN TIME_FORMAT(Time, '%H:%i:%s') BETWEEN '12:01:00' AND '16:00:00' THEN 'Afternoon'
						ELSE 'Evening'
					END;

-- ---- Day_name
SELECT Date FROM Walmartsales;                           -- --- Print Date ---
SELECT Date, DAYNAME(Date) FROM Walmartsales;            -- --- Print Date and the respective Dayname --- 

ALTER TABLE Walmartsales                                 -- --- Creating a column to hold Day_name ---
ADD COLUMN Day_name VARCHAR (10)
AFTER Gross_income;

UPDATE Walmartsales                                      -- --- populating the column ---
SET Day_name = DAYNAME(Date);

-- ---- Month_name
SELECT Date FROM Walmartsales;
SELECT Date, MONThNAME(Date) FROM Walmartsales;

ALTER TABLE Walmartsales
ADD COLUMN Month_name VARCHAR (10)
AFTER Gross_income;

UPDATE Walmartsales
SET Month_name = MONTHNAME(Date);


-- -------------------------------------------------------------------------------------------------------------------------------
-- --------------------------------------------- EXPLORATORY DATA ANALYSIS -------------------------------------------------------

SELECT * FROM Walmartsales LIMIT 10;                          -- -- Return 10 rows from the table ---

SELECT COUNT(*) AS Row_num                                    -- -- Total numbers of rows in the table ---
FROM Walmartsales;

SELECT COUNT(*) AS ColumnCount                                -- -- Query returns total number of rows ---
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'Walmartsales';

SELECT Invoice_ID, COUNT(*) AS Duplicate_count                -- -- Exploring duplicated field 
FROM Walmartsales
GROUP BY Invoice_ID
HAVING COUNT(*) > 1;

-- Descriptive Statistics --
SELECT
    AVG(Unit_price) AS Avg_Unit_Price,
    MIN(Unit_price) AS Min_Unit_Price,
    MAX(Unit_price) AS Max_Unit_Price,
    SUM(Unit_price) AS Total_Unit_Price,
    AVG(Quantity) AS Avg_Quantity,
    MIN(Quantity) AS Min_Quantity,
    MAX(Quantity) AS Max_Quantity,
    SUM(Quantity) AS Total_Quantity,
    AVG(VAT) AS Avg_Tax,
    MIN(VAT) AS Min_Tax,
    MAX(VAT) AS Max_Tax,
    SUM(VAT) AS Total_Tax,
    AVG(Total) AS Avg_Total,
    MIN(Total) AS Min_Total,
    MAX(Total) AS Max_Total,
    SUM(Total) AS Total_Sales,
    AVG(Gross_income) AS Avg_Gross_Income,
    MIN(Gross_income) AS Min_Gross_Income,
    MAX(Gross_income) AS Max_Gross_Income,
    SUM(Gross_income) AS Total_Gross_Income,
    MIN(Rating) AS Min_Rating,
    AVG(Rating) AS Avg_Rating,
    MAX(Rating) AS Max_Rating,
    SUM(Rating) AS Total_Rating
FROM Walmartsales;
-- ------------------------------------------------------------------------------------------
-- ------------------------ GENERIC QUESTIONS -----------------------------------------------

-- Q1. How many unique cities are represented in the data?
SELECT COUNT(DISTINCT City) AS Unique_Cities
FROM Walmartsales;

-- What are the unique cities in the data?
SELECT DISTINCT City
FROM Walmartsales;

-- Q2. How many unique locations are represented in the data?
SELECT COUNT(DISTINCT Branch) AS Unique_Location
FROM Walmartsales;

-- Identify the unique locations in the dataset
SELECT DISTINCT Branch
FROM Walmartsales;

-- Q3. In which city is each branch located?
SELECT DISTINCT Branch, City
FROM Walmartsales
GROUP BY Branch, City;
-- Alternatively:
SELECT City, Branch
FROM Walmartsales
GROUP BY Branch, City;

-- Q4. How many different types of customers are represented in the data?
SELECT COUNT(DISTINCT Customer_type) AS Unique_Customer_Type
FROM Walmartsales;

-- Q5. How many unique payment methods are used?
SELECT COUNT(DISTINCT Payment_mathod) AS Unique_Payment_Method
FROM Walmartsales;

-- How many different types of products are sold?
SELECT COUNT(DISTINCT Product_line) AS Umique_Product_Sold
FROM Walmartsales;

-- Q6. How many unique product line does the data have?
SELECT COUNT(DISTINCT Product_line) AS Unique_Product_Lines
FROM Walmartsales; 

-- What are the distinct product line included in the data
SELECT DISTINCT Product_line
FROM Walmartsales;

-- ------------------------------------------------------------------------------------------
-- ------------------------ SALES AND REVENUE QUESTIONS -------------------------------------
-- Q7. What is the most popular payment method?
SELECT Payment_mathod, COUNT(*) AS Count
FROM Walmartsales
GROUP BY Payment_mathod
ORDER BY Count DESC                      --      Terminating at this line returns all the payment nethods and the count
LIMIT 1;

-- Q8. What is the total revenue for each payment method?
SELECT Payment_mathod, SUM(Total) AS Total_Revenue 
FROM Walmartsales
GROUP BY Payment_mathod
ORDER BY Total_Revenue DESC;

-- Q9. What is the total revenue generated by each product line?
SELECT Product_line, SUM(Total) AS Total_Sales
FROM Walmartsales
GROUP BY Product_line
ORDER BY Total_Sales DESC;

-- Q10. What product line generated the most revenue?
SELECT Product_line, SUM(Total) AS Total_Revenue
FROM Walmartsales
GROUP BY Product_line
ORDER BY Total_Revenue DESC
LIMIT 1;

-- Q11. What is the best selling product line?
SELECT Product_line, SUM(Quantity) AS Total_Quantity
FROM Walmartsales
GROUP BY Product_line
ORDER BY Total_Quantity DESC             --       Terminating at this line returns all the product line and total quantity
LIMIT 1;

-- Q12. Which product line had the highest VAT costs?
SELECT Product_line, SUM(VAT) AS Total_VAT
FROM Walmartsales
GROUP BY Product_line
ORDER BY Total_VAT DESC
LIMIT 1;

-- Q13. What is the total revenue for each month?
SELECT Month_name AS MONTHS, SUM(Total) AS Total_Revenue
FROM Walmartsales
GROUP BY Month_name
ORDER BY Total_Revenue DESC;

-- Q14. Which month had the highest costs of goods sold (COGS)?
SELECT Month_name AS Month, SUM(COGS) AS Total_COGS
FROM Walmartsales
GROUP BY Month
ORDER BY Total_COGS DESC
LIMIT 1;

-- Q15. What is the total revenue generated in each city?
SELECT City, SUM(Total) AS Total_Sales
FROM Walmartsales
GROUP BY City
ORDER BY Total_Sales;

-- Q16. Which city had the highest total revenue?
SELECT City, SUM(Total) AS Total_Revenue
FROM Walmartsales
GROUP BY City
ORDER BY Total_Revenue DESC
LIMIT 1;
-- Alternatively
SELECT Branch, City,
SUM(Total) AS Total_Revenue
FROM Walmartsales
GROUP BY City, Branch
ORDER BY Total_Revenue DESC
LIMIT 1;

-- Q17. What is the total revenue for each customer type?
SELECT Customer_type, SUM(Total) AS Total_Revenue
FROM Walmartsales
GROUP BY Customer_type
ORDER BY Total_Revenue DESC;

-- Q18. Which customer type is most common?
SELECT Customer_type, COUNT(*) AS Customers_Count
FROM Walmartsales
GROUP BY Customer_type
ORDER BY Customers_Count DESC
LIMIT 1;

-- Q19. Which customer type makes the most purchases?
SELECT Customer_type, SUM(Quantity) AS Total_Purchase
FROM Walmartsales
GROUP BY Customer_type
ORDER BY Total_Purchase DESC
LIMIT 1;

-- Q20. What is the dominant gender among customers?
SELECT Gender, COUNT(*) AS Gender_Count
FROM Walmartsales
GROUP BY Gender
ORDER BY Gender_Count DESC
LIMIT 1;

-- Q21. What is the total revenue generated by each branch?
SELECT Branch, SUM(Total) AS Total_Revenue
FROM Walmartsales
GROUP BY Branch
ORDER BY Total_Revenue;

-- Q22. How are customers distributed by gender across different branches?
SELECT Branch, Gender, COUNT(*) AS Customer_Count
FROM Walmartsales
GROUP BY Gender, Branch;

-- Q23.	What is the revenue generated  by gender?
SELECT Gender, SUM(Total) AS Total_Revenue
FROM Walmartsales
GROUP BY Gender
ORDER BY Total_Revenue;

-- 24. What gender drives the most sales among the customers?
SELECT Gender, SUM(Total) AS Total_Revenue
FROM Walmartsales
GROUP BY Gender
ORDER BY Total_Revenue DESC
LIMIT 1;

-- Q25. How does revenue vary by gender and customer type?
SELECT Gender, Customer_type, SUM(Total) AS Total_Revenue
FROM Walmartsales
GROUP BY Customer_type, Gender
ORDER BY Total_Revenue DESC;

-- Q26. What is the sales performance of each product line by gender?
SELECT Gender, Product_line, SUM(Total) AS Total_Sales
FROM Walmartsales
GROUP BY Gender, Product_line
ORDER BY Total_Sales;

-- ------------------------------------------------------------------------------------------
-- --------------- PRODUCT PERFOMANCE AND CUSTOMER FEEDBACK QUESTIONS -----------------------

-- Q27. Which branch sold more products than the average?
SELECT Branch, SUM(Quantity) AS Total_Products_Sold
FROM Walmartsales
GROUP BY Branch
HAVING SUM(Quantity) > (SELECT AVG(Quantity) FROM Walmartsales);

-- Q28. Categorize product lines as "Good" or "Bad" based on their sales performance relative to the average.
SELECT Product_line, AVG(Total) AS Avg_Sales, 
		CASE
			WHEN AVG(Total) > (SELECT AVG(Total) FROM Walmartsales) THEN 'Good'
			ELSE 'Bad'
		END AS Category
FROM Walmartsales
GROUP BY Product_line;

-- Q29. The most common product line by genders?
SELECT Product_line, Gender, COUNT(*) AS Product_Count
FROM Walmartsales
GROUP BY Product_line, Gender
ORDER BY Product_Count DESC
LIMIT 1;
-- Alternatively
SELECT Gender,Product_line,
    COUNT(Gender) AS Total_Count
FROM Walmartsales
GROUP BY Product_line, Gender
ORDER BY Total_Count DESC
LIMIT 1;

-- Q30. What is the number of sales made in each part of the day per weekday?
SELECT
    DAYNAME(Date) AS Weekday,
    CASE
        WHEN TIME_FORMAT(Time, '%H:%i:%s') BETWEEN '00:00:00' AND '12:00:00' THEN 'Morning'
        WHEN TIME_FORMAT(Time, '%H:%i:%s') BETWEEN '12:01:00' AND '16:00:00' THEN 'Afternoon'
        ELSE 'Evening'
    END AS Time_of_day,
    COUNT(*) AS Sales_Count
FROM Walmartsales
GROUP BY Weekday, Time_of_day;

-- Q31. What is the average rating of each product line?
SELECT  Product_line , AVG(Rating) AS Avg_Rating
FROM Walmartsales
GROUP BY Product_line;

-- Q32. Which customer type brings the most revenue?
SELECT Customer_type, SUM(Total) AS Total_Revenue
FROM Walmartsales
GROUP BY Customer_type
ORDER BY Total_Revenue DESC
LIMIT 1;

-- Q33. Which city has the largest tax or VAT percentage?
SELECT City, SUM(VAT)/SUM(Total) AS VAT_Percentage
FROM Walmartsales
GROUP BY City
ORDER BY VAT_Percentage DESC
LIMIT 1;

-- Q34. Which customer type pays the most in VAT?
SELECT Customer_type, SUM(VAT) AS Total_VAT
FROM Walmartsales
GROUP BY Customer_type
ORDER BY Total_VAT DESC
LIMIT 1;

-- 35. At what times of day do customers most frequently leave ratings?
SELECT Time_of_date AS Time_of_day, COUNT(*) AS Rating_Count
FROM Walmartsales
GROUP BY Time_of_day
ORDER BY Rating_Count DESC;

-- Alternatively:
SELECT CASE
			WHEN TIME_FORMAT(Time, '%H:%i:%s') BETWEEN '00:00:00' AND '12:00:00' THEN 'Morning'
			WHEN TIME_FORMAT(Time, '%H:%i:%s') BETWEEN '12:01:00' AND '16:00:00' THEN 'Afternoon'
			ELSE 'Evening'
		END AS Time_of_day, COUNT(*) AS Rating_Count
FROM Walmartsales
GROUP BY Time_of_day
ORDER BY Rating_Count DESC;

-- Q36. When do customers leave the most ratings at each branch?
SELECT Branch, Day_name, Time_of_date, COUNT(*) AS Rating_Count
FROM Walmartsales
GROUP BY Branch, Day_name, Time_of_date
ORDER BY Rating_Count DESC;

-- Alternatively:
SELECT Branch, DAYNAME(Date) AS Weekday,
		CASE
			WHEN TIME_FORMAT(Time, '%H:%i:%s') BETWEEN '00:00:00' AND '12:00:00' THEN 'Morning'
			WHEN TIME_FORMAT(Time, '%H:%i:%s') BETWEEN '12:01:00' AND '16:00:00' THEN 'Afternoon'
			ELSE 'Evening'
		END AS Time_of_day, COUNT(*) AS Rating_Count
FROM Walmartsales
WHERE Rating IS NOT NULL
GROUP BY Branch, Weekday, Time_of_day
ORDER BY Rating_Count DESC;

-- Q37. Which day of the week has the highest average ratings?
SELECT Day_name, AVG(Rating) AS AVG_Rating
FROM Walmartsales
WHERE Rating IS NOT NULL
GROUP BY Day_name
ORDER BY AVG_Rating DESC
LIMIT 1;

-- Alternatively:
SELECT DAYNAME(Date) AS Weekday, AVG(Rating) AS Avg_Rating
FROM Walmartsales
WHERE Rating IS NOT NULL
GROUP BY Weekday
ORDER BY Avg_Rating DESC
LIMIT 1;

-- Q38. Which day of the week has the highest average ratings at each branch?
SELECT Branch, Day_name, AVG(Rating) AS AVG_Rating
FROM Walmartsales
GROUP BY Day_name, Branch
ORDER BY AVG_Rating DESC
LIMIT 3;

-- Alternatively:
SELECT Branch, DAYNAME(Date) AS Weekday, AVG(Rating) AS Avg_Rating
FROM Walmartsales
GROUP BY Branch, Weekday
ORDER BY Avg_Rating DESC
LIMIT 1;

-- Q39. How do customers rate products by gender? (Product Rating by Gender)
SELECT Gender, Product_line, COUNT(*) AS Rating
FROM Walmartsales
GROUP BY Gender, Product_line;
-- Alternatively;
SELECT Gender, Product_line, ROUND(AVG(Rating), 2) AS Avg_Rating
FROM Walmartsales
GROUP BY Gender, Product_line;

-- Q40. How do customers rate products by product line?
SELECT Product_line, AVG(Rating) AS Avg_Rating
FROM Walmartsales
GROUP BY Product_line;
-- Alternatively;
SELECT Product_line,  COUNT(*) AS Rating
FROM Walmartsales
GROUP BY Product_line;

SELECT Gender, COUNT(*) AS Rating
FROM Walmartsales
GROUP BY Gender;
-- Alternatively:
SELECT Gender, ROUND(AVG(Rating), 2) AS Rating
FROM Walmartsales
GROUP BY Gender;
