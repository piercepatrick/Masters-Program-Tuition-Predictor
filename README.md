# Data Science Related Masters Program Tuition Predictor: https://ds-masters-tuition-predictor.herokuapp.com/ 
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
- Visualized missing values in the DataFrame.  
<img src="/Images%20for%20readme/corr_of_nulls.PNG" width= "500">   
<img src="/Images%20for%20readme/heatmap_of_nulls.PNG" >   

# EDA
- Created interactive dashboard on Tableau that displays each states programs, credits required for each, delivery method, and tuition. 
- **Tableau Workbook:** https://github.com/piercepatrick/Masters-Program-Tuition-Predictor/tree/master/Tableau%20Work  
<img src="/Tableau%20Work/DS%20Masters%20Dashboard.png" width="750">
- I also utilized Python for exploratory data anlaysis. 
<img src="/Images%20for%20readme/corr.PNG" > 
<img src="/Images%20for%20readme/delivered.PNG" > 
<img src="/Images%20for%20readme/disciplines.PNG" >  

# Model Building 
- Created dummy variables 
- Split the data into train and tests sets 
- Models used for predicting tuition: 
  - **Multiple Linear Regression:** MAE = 15258  
  - **Lasso Regression:** MAE = 12644   
  - **Random Forest:** MAE = 10954 
  - **Support Vector Regression:** MAE = 15750
  - **XGBoost:** MAE = 11988 

# Productionization
Built a web app using streamlit that allows the user to adjust program parameters and receive an estimated tuition. I then deployed the web app to a server using heroku. 
The app can be found here: https://ds-masters-tuition-predictor.herokuapp.com/
  
