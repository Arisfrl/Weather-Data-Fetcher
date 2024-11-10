
---

# Weather Data Fetcher 🌤️

This Python script fetches and displays the current weather data for a specified city using the [OpenWeatherMap API](https://openweathermap.org/api). In this example, the city is set to **Kolkata** by default.

## 📋 Prerequisites

Ensure you have the following installed on your system:
- Python 3.x
- `requests` module

To install the `requests` module, use:
```bash
pip install requests
```

## 📂 Project Structure
```
weather-fetcher/
├── script.py
└── api_key.txt
```

- **`script.py`**: The main Python script to fetch weather data.
- **`api_key.txt`**: A text file containing your OpenWeatherMap API key.

## 🔧 Setup Instructions

1. **Clone this repository** (or copy the script into your project):
   ```bash
   git clone https://github.com/Arisfrl/Weather-Data-Fetcher.git
   cd Weather-Data-Fetcher
   ```

2. **Obtain an API key** from [OpenWeatherMap](https://home.openweathermap.org/users/sign_up):
   - Sign up for an account.
   - Navigate to the API section and generate an API key.

3. **Create an `api_key.txt` file** in the project directory:
   - Paste your API key into the `api_key.txt` file.
   - Ensure there are no extra spaces or newlines.

   Example:
   ```
   your_api_key_here
   ```

4. **Run the script**:
   ```bash
   python script.py
   ```

## 📊 Output Example

When the script is run, it fetches the weather data for **Kolkata** and prints it to the console:
```
Weather data for Kolkata is:
{
    "coord": {"lon": 88.3697, "lat": 22.5697},
    "weather": [...],
    "base": "stations",
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

To change the city, modify the `city` variable in the `script.py` file:
```python
city = "YourCityName"
```

## ⚠️ Error Handling

- Ensure the `api_key.txt` file is present and contains a valid API key.
- If the API request fails (status code not `200`), the script will not print the weather data. Ensure that your internet connection is active and the API key is valid.

## 📜 License


---

