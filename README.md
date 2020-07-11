# Data Science Related Masters Program Tuition Predictor
- Created a tool that estimates Data Science related graduate program's tuition (MAE ~ $ 10K) to help Data Scientists explore different options for graduate school.
- Scraped program descriptions from mastersportal.com using simplescraper and beautifulsoup.
- Engineered features from each program to quantify the value universities put on gpa, gre, gmat, toefl, and ielts.
- Created an interactive dashboard using Tableau for students to explore programs listed by state.
- Optimized Linear, Lasso,Random Forest, XGBoost, and Support Vector Regressors using GridsearchCV to reach the best model.
- Deployed a web app using streamlit and heroku.

# Resources Used 
- **Python Version:** 3.7   
- **Tableau Version:** 2020.2   
- **Packages used:** pandas, numpy, matplotlib, sklearn, seaborn, beautifulsoup, urllib, texthero, sidetable, missingno, wordcloud, nltk       
- **Simple Scraper**: https://simplescraper.io/docs/    
- **BeautifulSoup:** https://www.youtube.com/watch?v=Dh9Ihheqyu8&t=493s  
- **Ken Jee's Project from Scratch:** https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t   
- **Streamlit / Heroku:** https://www.youtube.com/watch?v=mQ7rGcE766k   
- **Model Building:**  
-- https://www.kaggle.com/apapiu/regularized-linear-models   
-- https://www.kaggle.com/mrtechnical011/support-vector-regression  

# Web Scraping
Utilized chrome extension simplescraper to scrape urls of each program on mastersportal.com related to Data Science in the USA. With each program I got the following:

- University Name  
- Program Name  
- Tags (M.Sc, M.B.A, etc.)   
- Program Duration (months) 
- Tuition (USD) 
- Apply Date  
- Start Date 
- Program Description  
- State  
- City  
- University World Ranking 
- Role (Full-time or not)  
- Disciplines 
- Delivered (On Campus, Online, Blended) 
- Credits 
- TOEFL Score Required (Test of English as a Foreign Language) 
- IELTS Score Required (International English Language Testing System)
- GPA Required 
- GRE Required or Not 
- GMAT Required or Not  

# Data Cleaning & Feature Engineering
- Filtered the DataFrame for program names that included keywords related to Data Science.  
- Dropped columns 'role', 'apply_date', 'gmat', , &'gre'.  
- Stripped all textual columns of preceding and succeeding brackets and quotation marks.  
- Replaced column values that were empty with Nan.  
- Visualized missing values in the DataFrame. 
- Cleaned the description column using texthero.  
- Created columns for whether or not the program requires the following:  
  - GRE  
  - TOEFL 
  - IELTS 
  - GMAT 
  - GPA 
- Created columns: 
  - Tuition Per Month 
  - Description Length 
  - Fall Start 
  - Spring Start 
  - Summer Start 
  - University Tier Ranking 

# EDA
- Created interactive dashboard on Tableau that displays each states programs, credits required for each, delivery method, and tuition.
- **Tableau Workbook:** https://github.com/piercepatrick/Masters-Program-Tuition-Predictor/tree/master/Tableau%20Work 
- I also utilized Python for exploratory data anlaysis.
