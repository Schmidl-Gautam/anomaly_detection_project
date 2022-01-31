# Anomaly Detection Project:

Rajaram Gautam  and Scott Schmidl ---------January 31, 2022 -------------- Submitted To: Codeup Data Science Team

# Project Summary:
###### Give answers to the questions asked my management via email by analyzing curriculum_logs database of Codeup


# Project Goals:

1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?
2. Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?
3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?
4. Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses?
5. At some point in 2019, the ability for students and alumni to access both curriculums (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before?
6. What topics are grads continuing to reference after graduation and into their jobs (for each program)?
7. Which lessons are least accessed?
8. Anything else I should be aware of?



# Deliverables:
- Email before due date and time with the summary of the findings and answers to the questions asked
- A link to final notebook on GitHub that asks and answers questions - document the work I did to justify findings
- An Executive Summary Slide with findings

# Executive Summary
### 1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?
The top five lessons or topic accross each programs area as follows:

###### PHP FULL STACK WEB DEV:
|Index | Lesson / Topic | Access Count
|---|---|---|
|0 |  index.html                         | 1011
|1 |  javascript-i                       | 736
|2 |  html-css                           | 542
|3 |  spring                             | 501
|4 |  java-iii                           | 479


###### JAVA FULL STACK WEB DEV:
|Index | Lesson / Topic | Access Count
|---|---|---|
|0 |  javascript-i                         | 17457
|1 |  java-iii                             | 12683
|2 |  html-css                             | 12569
|3 |  java-ii                              | 11719
|4 |  spring                               | 11376


###### FRONT END WEB DEV:
|Index | Lesson / Topic | Access Count
|---|---|---|
|0 |  content/html-css                             | 2
|1 |  content/html-css/gitbook/images/favicon.ico  | 1
|2 |  content/html-css/introduction.html           | 1


###### DATA SCIENCE:
|Index | Lesson / Topic | Access Count
|---|---|---|
|0 |  classification/overview                         | 1785
|1 |  1-fundamentals/1.1-intro-to-data-science        | 1633
|2 |  sql/mysql-overview                              | 1424
|3 |  fundamentals/intro-to-data-science              | 1413
|4 |  6-regression/1-overview                         | 1124


### 2. Is there a cohort that referred to a lesson significantly more than other cohorts seemed to gloss over?
- The Staff accessed the top lessons the most
- Easley cohort accessed the "Stats/compare-means" other cohorts data is missing.
- Easley cohort accessed the "sql/mysql-overview" more than three time as much as Darden or Florence
- Darden accessed anomaly detection, classification  where as there were no other cohorts accessed it.
- Franklin accessed more on JavaScript-i/conditionals, JavaScript-i / introduction / primitives-types,  JavaScript-i/ Introduction and operators where as no other cohorts did.
- Jupiter accessed Spring / Fundamentals / Views, Spring / Fundamentals / Controllers, Spring / Fundamentals / Repositories where as other cohort access count is negligible.
- Niagara (or Appolo confusing) accessed Regression / Evaluate, Stats / Probability Distributions more where as other groups did not access it a lot.


### 3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students?
###### Findings:
|Index | USER_ID | Access Count
|---|---|---|
|0 |  679        | 4
|1 |  956        | 3
|2 |  278        | 3
|3 |  539        | 3
|4 |  832        | 2


### 4. Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses?

ip address with too much access counts
97.105.19.58    241019
97.105.19.61     56968
Name: path, dtype: int64
Thus, there are two anamalous ip addresses, which is active more than 3 σ above the μ.
Its activity has decreased on 2019 and 2020 at one time.

### 5. At some point in 2019, the ability for students and alumni to access both curriculums (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before?
###### Findings:
Although there are less, there are at least two instances of ds students wd site: java-ii/object-oriented-programming and spring
For web Dev, they did seem to access the Data Science curriculum fairly often prior to having access denied. After 2019, there was a large drop off, but there seems to be a few cases where a data science topic was accessed.

### 6. What topics are grads continuing to reference after graduation and into their jobs (for each program)?
### Findings:
Overall, the top ten lessons accessed by post grads are:
|Index | Lesson | Access Count
|---|---|---|
|0 |javascript-i   |4969
|1 |spring         |4272
|2 |html-css       |3687
|3 |java-iii       |3541
|4 |java-ii        |3444
|5 |java-i         |3130
|6 |javascript-ii  |2981
|7 |mysql          |2584
|8 |jquery         |2469
|9 |index.html     |1721

###### Top 3 for PHP
|Index | Lesson | Access Count
|---|---|---|
|0 |index.html    |1011
|1 |javascript-i  |736
|2 |html-css      |542


###### Top 3 for JAVA
|Index | Lesson | Access Count
|---|---|---|
|0 |javascript-i    |4233
|1 |spring          |3771
|2 |html-css        |3145


###### Top 3 for FRONT END
|Index | Lesson | Access Count
|---|---|---|
|0 |content/html-css                                 |2
|1 |content/html-css/gitbook/images/favicon.ico      |1
|2 |content/html-css/introduction.html               |1


###### Top 3 for DS
|Index | Lesson | Access Count
|---|---|---|
|0 |sql/mysql-overview              |275
|1 |classification/overview         |267
|2 |anomaly-detection/overview      |191

### 7. Which lessons are least accessed?
|Index | Lesson | Access Count
|---|---|---|
|0 |npm                                                            | 1
|1 |web-design/ux/layout/.json                                     | 1
|2 |appendix/cls/2-listing-files                                   | 1
|3 |appendix/cli/2-Overview                                        | 1
|4 |appendix/cli/2-overview                                        | 1
|5 |cli/4-navigating-the-filesystem                                | 1
|6 |content/mysql/relationships/indexes.html                       | 1
|7 |5-stats                                                        | 1
|8 |6-stats                                                        | 1
|9 |appendix/professional-development/post-interview-review-form   | 1




# Data dictionary
|Index | Column Name | Description
|---|---|---|
|0 |  path              | URL Path
|1 |  user_id           | User ID
|2 |  cohort_id         | Cohort ID
|3 |  ip                | IP Address
|4 |  name              | Cohort Name
|5 |  slack             | Slack Name
|6 |  start_date        | Start Date
|7 |  end_date          | End Date
|8 |  created_at        | Created Date
|9 |  updated_at        | Updated Date
|10|  program_id        | Program ID
|11|  course_name       | Course Name
|12|  course_subdomain  | Subdomain
|13|  date_time         | date time (Derived Column)
|14|  date_year         | Year Timestamp
|15|  date_month        | Month Timestamp
|16|  date_weekday      | Weekday Timestamp
|17|  hour              | Hour Timestamp



# Project Specifications

### Plan:
We need to retrieve data of curriculum logs from Codeup MySQL Server from curriculum_logs database. We need to clean the data, so that we can answers the questions of our project goals. We can modify our cleaned data in jupyter notebook as well if needed.

### Acquire
We can acquire data from Codeup MySQL Server from curriculum_logs database. We can convert our dataframe to .csv file. Here we converted it to curriculum_logs.csv and put it in working directory. So that we can have access to our data, even our internrt is down.

### Prep
Steps performed in preparation phase in order are as follows:
- Creatd a function to create a couse name and course sub domain.
- Droping column deleted_at
- filtering out just a single null value in path
- Combining date and time
- Converting date to pandas datetime format
- Creating columns date_year, date_month, date_weekday, hour
- Converting all date columns to pandas datetime format
- Droping date and time
- Changing datatype of cohort_id and program_id


# Reproduce My Project

- Read this README.md
- Clone the repo to your local working directory
- Run the report.ipynb notebook

