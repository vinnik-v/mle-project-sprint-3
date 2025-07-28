import requests
import time
import random

URL = "http://localhost:8081/predict"

sample_data = {
    "build_year": 2005,
    "building_age": 20,
    "floor": 5,
    "high_ceiling_flag": 1,
    "is_central": 0,
    "kitchen_area**3": 14,
    "latitude": 55.53,
    "longitude": 37.508,
    "rooms": 2
}

def generate_payload():
    data = sample_data.copy()
    data["floor"] = random.randint(1, 25)
    data["kitchen_area**3"] = round(random.uniform(8.0, 20.0), 1)
    data["rooms"] = random.choice([1, 2, 3])
    return {"model_params": data}

def main():
    for i in range(100):
        payload = generate_payload()
        try:
            response = requests.post(URL, json=payload)
            print(f"[{i+1}] Status: {response.status_code} | Response: {response.json()}")
        except Exception as e:
            print(f"[{i+1}] Error: {e}")
        time.sleep(0.5)  # Пауза между запросами

if __name__ == "__main__":
    main()
