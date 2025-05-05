🧠 Indeed Job Scraper and Data Analyzer
This project consists of a web scraper and a data analysis module designed to extract and analyze job postings from Indeed.com for software-related roles. It provides valuable insights into job titles, locations, companies, salaries, and ratings using Selenium for automation and Pandas/Matplotlib for analysis.

📌 Project Structure
Indeed_scraping.py: Scrapes job listings from Indeed using Selenium and stores them in indeed_jobs.csv.

indeed_analysis.py: Performs data analysis and visualization on the scraped data.

📸 Features
🕸 Web Scraping
Extracts job title, location, company, job type, salary, and ratings.

Navigates through multiple pages.

Handles pop-ups and page delays.

📊 Data Analysis
Displays job distribution by location and company.

Visualizes salary ranges.

Shows average job ratings.

Identifies the most common job types.

🚀 Getting Started
✅ Prerequisites
Make sure you have the following installed:

Python 3.7+

Google Chrome

ChromeDriver

txt
Copy code
selenium
webdriver-manager
pandas
matplotlib
🧪 Usage
1. Run the Scraper
bash
Copy code
python Indeed_scraping.py
This will generate a file: indeed_jobs.csv.

2. Run the Analyzer
bash
Copy code
python indeed_analysis.py
This will generate visual charts based on the extracted data.

📂 Output Example
Sample output columns from indeed_jobs.csv:

Job Title	Location	Company	Job Type	Pay	Rating
Software Engineer	New York	Google	Full-Time	$120K	4.5

📈 Sample Visuals
Top Hiring Companies

Salary Range Distribution

Job Type Frequency

Average Ratings by Company

⚠️ Notes
Use responsibly: This script is for educational purposes and respects Indeed’s Terms of Service.

Data accuracy depends on page structure, which may change.

