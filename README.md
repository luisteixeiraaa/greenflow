# GreenFlow Report API

The GreenFlow Report API is a Flask-based web service that provides insights into resource consumption (energy, water, and CO2 emissions) across different companies and sectors. It allows users to retrieve top consumers, compare sector averages, and fetch company-specific information.

## Table of Contents
- [Features](#features)
- [Endpoints](#endpoints)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Top Consumers**: Retrieve the top consumers of a specific resource (energy, water, CO2).
- **Sector Comparison**: Compare average resource consumption across different sectors.
- **Company Information**: Fetch detailed information about a specific company by its ID.

## Endpoints

### Home
- **GET `/`**: Returns a welcome message and a list of available endpoints.

### Top Consumers
- **GET `/top_consumers/<resource>`**: Returns the top 5 consumers of the specified resource by default.
  - Example: `/top_consumers/energia`
- **GET `/top_consumers/<resource>/<top_n_order>`**: Returns the top N consumers of the specified resource, ordered by ascending or descending.
  - Example: `/top_consumers/energia/10_desc` (top 10 consumers in descending order)

### Sector Comparison
- **GET `/sector_comparison/<resource>`**: Compares average resource consumption across sectors.
  - Example: `/sector_comparison/agua`

### Company Information
- **GET `/company_info/<id>`**: Returns detailed information about a specific company by its ID.
  - Example: `/company_info/123`

## Setup

### Prerequisites
- Python 3.x
- Flask
- Pandas

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/greenflow-report-api.git
   cd greenflow-report-api