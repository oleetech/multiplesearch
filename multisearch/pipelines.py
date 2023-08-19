from itemadapter import ItemAdapter
import json

class MultisearchPipeline:
    def __init__(self):
        self.items = []

    def process_item(self, item, spider):
        self.items.append(item)
        return item

    def close_spider(self, spider):
        self.file_path = "data.json"  # Replace with the actual path of your file
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump([dict(item) for item in self.items], file, ensure_ascii=False, indent=2)

        print(f"Scraped data saved to {self.file_path}")
