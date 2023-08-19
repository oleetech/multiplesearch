from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from multisearch.spiders.multiplewebsite import MultiplewebsiteSpider
import pandas as pd
import matplotlib.pyplot as plt
# Set the search_query value
search_query = input("Enter search query: ")

# Get the Scrapy settings
settings = get_project_settings()

# Set the search_query in the settings
settings.set('SEARCH_QUERY', search_query)

# Create a CrawlerProcess instance
process = CrawlerProcess(settings)

# Specify the spider name
spider_name = 'multiplewebsite'

# Start the crawl
process.crawl(spider_name)
process.start()

# Load data from JSON file
df = pd.read_json('data.json')

# Convert 'price' column to numeric
df['price'] = df['price'].astype(int)

# Create a bar plot
plt.figure(figsize=(10, 6))
df.plot(kind='bar', x='seller', y='price', legend=None)
plt.title('Price Comparison')
plt.xlabel('Seller')
plt.ylabel('Price')
for i, v in enumerate(df['price']):
    plt.text(i, v, f'{v:.2f}', ha='center', va='bottom')
plt.xticks(rotation=0)  # Rotate x-axis labels if needed
plt.tight_layout()  # Adjust layout for better spacing
plt.show()