
# Web Scraper Dashboard

A web application that scrapes data from a public website and displays it on a centralized platform with authentication and responsive design.

## Table of content

1. Introduction
2. Project Overview
3. Features
4. TechStack
5. Screenshots
6. Instructions to Run the Project
7. Author
8. Demo
## Project Overview
- **Backend**: Scrapes data using Python(BeautifulSoup,Request) then stores it as `data.json`.  
- **Frontend**: React app fetches the JSON data and displays it in a clean, responsive UI.  
## Features

- 🔐 OAuth 2.0 Authentication – Secure access using Google or other identity providers.
- 🕸️ Web Scraping Engine – Fetches structured data (like titles, price, description, or other details) from public website.
- 📊 Centralized Dashboard – All scraped data is displayed in one place for easy viewing.
- 📱 Responsive Design – Works seamlessly across desktops, tablets, and mobile devices.


## Tech Stack

**Client:** React.js , CSS

**Server:** Python, BeautifulSoup, Request.

**other:** JSON


## Screenshots

### Login With Google
![image alt](https://github.com/ShivamRaj12/assignment/blob/a13ae9c17e699fbd222d2a892bdaffa56aa9151a/loginpage.png?raw=true)

###  authentication 
![Google authentication]( https://github.com/ShivamRaj12/assignment/blob/04ada141906e3ad9cec18f2521e3f6e4feb91b91/auth.png?raw=true)

 ### Home Screen 
![home]( https://github.com/ShivamRaj12/assignment/blob/04ada141906e3ad9cec18f2521e3f6e4feb91b91/table.png?raw=true)
## Installation

### Frontend (react + vite)


* Create a new Vite + React project
```bash
  npm create vite@latest my-app
  cd my-app

```
* Core React dependencies (usually installed by Vite)
```bash
  npm install react react-dom


```
* For OAuth 2.0 authentication
```bash
  npm install @react-oauth/google


```
* React Router (optional, if you plan multiple pages)
```bash
  npm install react-router-dom


```
* Run development server:
```bash
  npm run dev


```

### Backend (Python)
    

  1) Create a virtual environment  
```bash
cd backend
python -m venv venv
# Activate it:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate


```

2) Install Python dependencies

```bash

# FastAPI web framework
pip install fastapi

# ASGI server to run FastAPI
pip install "uvicorn[standard]"

# For making HTTP requests
pip install requests

# For web scraping and parsing HTML
pip install beautifulsoup4

# For loading environment variables from .env
pip install python-dotenv

# For verifying Google OAuth 2.0 tokens
pip install google-auth

```


## Authors

- [ShivamRaj12 (github)](https://github.com/ShivamRaj12)


## Demo

https://shivamrajassignment.vercel.app/

