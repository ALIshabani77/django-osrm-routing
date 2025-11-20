import requests
from rest_framework.exceptions import APIException

class OSRMService:
    BASE_URL = "http://router.project-osrm.org/route/v1/driving"

    @staticmethod
    def calculate_route(start_coords: tuple, end_coords: tuple):
        """
        Calculates distance and duration between two points using OSRM.
        Input: (lat, lon) tuples.
        """
        # OSRM expects: longitude,latitude
        start_str = f"{start_coords[1]},{start_coords[0]}"
        end_str = f"{end_coords[1]},{end_coords[0]}"
        
        url = f"{OSRMService.BASE_URL}/{start_str};{end_str}?overview=false"

        try:
            response = requests.get(url, timeout=5)
            if response.status_code != 200:
                raise APIException(f"OSRM Service Error: {response.status_code}")

            data = response.json()
            if data.get("code") != "Ok":
                raise APIException("Route not found.")

            route = data["routes"][0]
            return {
                "distance_km": round(route["distance"] / 1000, 2),
                "duration_min": round(route["duration"] / 60, 1)
            }
        except requests.RequestException:
            raise APIException("External service unavailable.")