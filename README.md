# Weather Application  
ur --> https://weather-api-n4gh.onrender.com

## Overview

This is a simple weather application built using Flask and integrated with the OpenWeather API. Users can enter a city and choose the units to get current weather data.

## Features

- User-friendly web interface.
- Fetches real-time weather data from the OpenWeather API.
- Supports metric and imperial units for temperature.

## Prerequisites

- Python 3.x
- Flask
- `requests` library
- OpenWeather API key

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/GYKrishna25/Weather-Api.git
   cd Weather-Api

## Create Virtual Env

## Install the required dependencies

## Create a .env file in the root directory and add your OpenWeather API key:
API_KEY=your_openweather_api_key_here


## Deployment
This application is deployed on Render.com. If you want to deploy it yourself, follow these steps:

Create a new web service on Render.

Connect your GitHub repository.

Set environment variables in the Render dashboard:

Key: API_KEY
Value: your OpenWeather API key.
Set the start command in Render to:gunicorn app:app
