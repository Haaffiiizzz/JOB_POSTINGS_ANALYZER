import requests
from bs4 import BeautifulSoup

# Set up the search parameters
job_title = "data scientist"
location = "new york"

# Create the URL based on search parameters
url = f"https://www.indeed.com/jobs?q={job_title}&l={location}"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.content, 'html.parser')

# Find all job cards on the page
job_cards = soup.find_all('div', class_='jobsearch-SerpJobCard')

# Loop through each job card and extract details
for job in job_cards:
    title = job.find('h2', class_='title').text.strip()
    company = job.find('span', class_='company').text.strip()

    print(f"Job Title: {title}")
    print(f"Company: {company}")
    print("-" * 40)

print(":done")