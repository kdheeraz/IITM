import sys
import argparse
import wikipedia
import json
import datetime

# Create the parser
parser = argparse.ArgumentParser()
# Adding arguments
parser.add_argument('--keyword', type=str, required=True)
parser.add_argument('--num_urls', type=int, required=True)
parser.add_argument('--output', type=str, required=True)
# Parse the argument
args = parser.parse_args()

keyword = args.keyword

num_urls = int(args.num_urls)
#print("num", num_urls)

output = args.output
wikipedia.set_rate_limiting(rate_limit=1)

print("loading requested data.....")
print("Note: Sometimes due to load wikipidia may return less no. of results.")

page_refs = wikipedia.search(keyword, num_urls)

# print(page_refs)

response_list = []

for page_ref in page_refs:
    page = wikipedia.page(page_ref)
    response_list.append(
        {"url": page.url, "paragraph": wikipedia.summary(page_ref, sentences=2)})
print(response_list)


with open(output, 'w', encoding='utf-8') as f:
    json.dump(response_list, f, ensure_ascii=False, indent=4)
