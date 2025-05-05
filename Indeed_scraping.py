import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys
sys.stdout.reconfigure(encoding='utf-8')

options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

all_jobs = []

try:
    base_url = "https://www.indeed.com/jobs?q=Software&l=&jobsWithPay=1&sc=0kf%3Aattr%2875GKK%7CCF3CP%7CNJXCK%252COR%29%3B&from=searchOnDesktopSerp&vjk=7b05d7dff0ad1dc9"
    driver.get(base_url)
    time.sleep(5)

    page_number = 1
    total_jobs = 0

    while True:
        print(f"\n--- Page {page_number} ---")

        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.job_seen_beacon"))
        )

        job_cards = driver.find_elements(By.CSS_SELECTOR, "div.job_seen_beacon")
        print(f"Number of jobs on this page: {len(job_cards)}\n")

        for idx, job in enumerate(job_cards, 1):
            try:
                title_element = job.find_element(By.CSS_SELECTOR, "h2.jobTitle a")
                title = job.find_element(By.CSS_SELECTOR, "h2.jobTitle span[title]").get_attribute("title")
                job_link = title_element.get_attribute("href")
            except:
                title = "Job Title Not Found"
                job_link = None

            try:
                loc = job.find_element(By.CSS_SELECTOR, "div[data-testid='text-location']").text.strip().split(',')
                location = loc[0]
            except:
                location = "Location Not Found"

            try:
                company_name = job.find_element(By.CSS_SELECTOR, "span[data-testid='company-name']").text.strip()
            except:
                company_name = "Company Not Found"

            job_type = "N/A"
            pay = "N/A"
            evaluate = "N/A"

            if job_link:
                try:
                    main_window = driver.current_window_handle
                    driver.execute_script(f"window.open('{job_link}');")
                    driver.switch_to.window(driver.window_handles[1])
                    time.sleep(3)

                    try:
                        job_type = driver.find_element(
                            By.CSS_SELECTOR,
                            "div[aria-label='Job type'] span.e1wnkr790"
                        ).text.strip()
                    except:
                        pass

                    try:
                        pay = driver.find_element(
                            By.CSS_SELECTOR,
                            "div[aria-label='Pay'] span.e1wnkr790"
                        ).text.strip()
                    except:
                        pass

                    try:
                        evaluate = driver.find_element(
                            By.CSS_SELECTOR,
                            "div[aria-label*='out of 5 stars']"
                        ).get_attribute("aria-label")
                        evaluate = evaluate.replace(" out of 5 stars", "").strip()
                    except:
                        pass

                    driver.close()
                    driver.switch_to.window(main_window)
                    time.sleep(1)

                except Exception as e:
                    print(f"Error accessing job details: {e}")
                    if len(driver.window_handles) > 1:
                        driver.close()
                        driver.switch_to.window(driver.window_handles[0])

            print(f"{idx}. {title} | {location} | {company_name} | {job_type} | {pay} | {evaluate}")
            total_jobs += 1
            all_jobs.append([title, location, company_name, job_type, pay, evaluate])

        try:
            next_page = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='pagination-page-next']"))
            )
            next_page.click()
            page_number += 1
            time.sleep(3)
        except:
            print("\nNo more pages or the 'Next' button was not found.")
            break

    print(f"\nTotal number of jobs extracted: {total_jobs}")

except Exception as e:
    print("An error occurred:", e)

finally:
    with open("indeed_jobs.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Job Title", "Location", "Company", "Job Type", "Pay", "Rating"])
        writer.writerows(all_jobs)

    driver.quit()
    print("\n✅ Data saved to 'indeed_jobs.csv'")