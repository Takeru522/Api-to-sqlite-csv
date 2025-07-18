# 🛒 API to SQLite to CSV Automation

## 🔧 Problem

A business needs to pull product listings from a public API daily, keep the data for records, and share a clean summary (top 5 best-rated products) as a CSV report.

## ✅ Solution

This Python script automates the full workflow:

- Fetches product data from a REST API (`fakestoreapi.com`)
- Filters the top 5 products by rating
- Stores all data in a local SQLite database
- Exports a daily summary to CSV

## 💼 Real-World Use Case

> "A client wants to track daily top-performing products and archive data historically — all automatically."

## ⚙️ Tools Used

- `requests` – fetch data from API
- `pandas` – process/filter/export data
- `sqlite3` – store all product records

## 📁 Folder Structure
