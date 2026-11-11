# csv_practice.py
# Author: Ahraya Dalaq
# Module 12 Lab: Read a Sales CSV, Write a Cleaned Report
#
# Reflection 1: Python is better than Excel for tasks you have to repeat, because once the 
# script is written it can clean and filter the data in seconds every time with no manual clicking. 
# Python can also handle much larger files and automate the whole process. Excel is easier for quickly 
# viewing data, making charts, and sharing with people who don't know how to code. 
#
# Reflection 2: A store could use an append-mode log to record its total sales at the end 
# of each day. Append mode is the right tool because it adds a new line every time instead 
# of erasing the old ones, so the business keeps a full history it can look back on to spot trends.

import csv
from datetime import datetime

SALES_FILE = "data/sales.csv"
CLEANED_FILE = "data/cleaned.csv"
LOG_FILE = "data/run_log.txt"

print("---Exercise 1---")
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    row_count = sum(1 for _ in reader)
    print(f"Opened {SALES_FILE}. Header: {header}, data rows: {row_count}")

print ("---Exercise 2---")

with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print("---Exercise 3---")
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(f"Header: {header}")
    for row in reader:
        print(row)

print("---Exercise 4---")
total_revenue = 0
with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        product, price_str, qty_str = row
        price = float(price_str)
        quantity = int(qty_str)
        total = price * quantity
        total_revenue += total
        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Total revenue: ${total_revenue:.2f}")

print("---Exercise 5---")

high_value = []
rows_read = 0


with open(SALES_FILE, "r") as f:
    reader = csv.reader(f)
    next(reader)  # Skip header
    for row in reader:
        rows_read += 1
        product, price_str, qty_str = row
        price = float(price_str)
        quantity = int(qty_str)
        total = price * quantity
        if total > 100:
            high_value.append((product, f"{price:.2f}", quantity, f"{total:.2f}"))

with open(CLEANED_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Product", "Price", "Qty", "Total"])
    for row in high_value:
        writer.writerow(row)

print(f"Wrote {len(high_value)} of {rows_read} rows to {CLEANED_FILE}.")


print("---Exercise 6---")

# csv.reader is simple and works well when the column order is fixed and known.
# DictReader is clearer and safer when columns might move, since you access fields by name.

dict_total = 0
with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        total = price * quantity
        dict_total += total
        print(f"{row['product']}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Total revenue: ${dict_total:.2f}")


print("---Exercise 7---")
summary = {}

with open(SALES_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        total = float(row["price"]) * int(row["quantity"])
        summary[product] = summary.get(product, 0) + total

for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")


print("---Exercise 8---")

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(LOG_FILE, "a") as f:
    f.write(f"{timestamp} total revenue: ${total_revenue:.2f}\n")

entries = 0
with open(LOG_FILE, "r") as f:
    for line in f:
        entries += 1
        print(line.strip())

print(f"Log entries so far: {entries}")