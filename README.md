Here’s an updated `README.md` with your additional instructions:

---

# Weather Data Fetcher 🌤️

This Python script fetches and displays the current weather data for a specified city using the [OpenWeatherMap API](https://openweathermap.org/api). By default, the city is set to **Kolkata**.

## 📋 Prerequisites

Make sure you have the following installed:
- **Python 3.x**
- `requests` module

To install the `requests` module:
```bash
pip install requests
```

## 📂 Project Structure
```
Weather-Data-Fetcher/
├── script.py
└── api_key.txt
```

- **`script.py`**: The main Python script to fetch and display weather data.
- **`api_key.txt`**: A text file where you will store your OpenWeatherMap API key.

## 🌐 Step-by-Step Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Arisfrl/Weather-Data-Fetcher.git
   cd Weather-Data-Fetcher
   ```

2. **Create an account on OpenWeatherMap** to get your API key:
   - Sign up at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up).
   - Go to the API section and generate a new API key.

3. **Add your API key**:
   - Open (or create) the file `api_key.txt`.
   - Paste your API key inside the file:
     ```
     your_api_key_here
     ```

4. **Run the script**:
   ```bash
   python script.py
   ```

## 🔄 How It Works

Here’s a summary of what this script does:

🌐 Create an account on OpenWeatherMap for API keys.  
📡 Use the current weather data API by city name.  
🔗 Modify the base URL for temperature units (Celsius/Fahrenheit).  
🐍 Set up a Python script to fetch weather data.  
✅ Check API response status for success.  
🌡️ Extract temperature, weather description, and humidity data.  
🌍 Easily switch city names to get weather data for different locations.  

## 📊 Sample Output

When the script is executed, it fetches the weather data for **Kolkata** and displays it:

```
Weather data for Kolkata is:
{
    "coord": {"lon": 88.3697, "lat": 22.5697},
    "weather": [...],
    "main": {
        "temp": 28.5,
        "feels_like": 31.2,
        "temp_min": 28.5,
        "temp_max": 28.5,
        ...
    },
    ...
}
coord : {'lon': 88.3697, 'lat': 22.5697}
weather : [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}]
main : {'temp': 28.5, 'feels_like': 31.2, 'temp_min': 28.5, 'temp_max': 28.5, 'pressure': 1010, 'humidity': 75}
...
```

## 🛠️ Customization

To change the city, modify the `city` variable in `script.py`:
```python
city = "YourCityName"
```

## ⚠️ Troubleshooting

- Make sure `api_key.txt` is present in the project directory and contains a valid API key.
- Check your internet connection if the API request fails.
- The script only prints data if the status code is `200`. If not, the request might be invalid due to a wrong API key or city name.

## 📜 License

This project is open-source and available under the [Eclipse Public License](LICENSE).

## 📎 Repository Link

Find the project on GitHub: [Weather-Data-Fetcher](https://github.com/Arisfrl/Weather-Data-Fetcher.git)

---

