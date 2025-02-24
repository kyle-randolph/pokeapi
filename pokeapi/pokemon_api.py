#! python3
import requests

BASE_URL = "https://pokeapi.co/api/v2/"


def get_pokemon(identifier):
    # Fetch Pokemon details by ID or name.
    url = f"{BASE_URL}pokemon/{identifier}/"
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Example: 404 Not Found
    except requests.exceptions.ConnectionError:
        print("Connection error. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")


def list_pokemon():
    url = f"{BASE_URL}pokemon/"
    pokemon_list = []
    """ Iterate through and capture full list of pokemon. This leverages the 'next' url value 
    being returned. Alternatively, pagination could be completed using skip (offset) and limit values
    after capturing the total count from data['count'].
    """
    while url != None:
        try:
            response = requests.get(url)
            data = response.json()
            url = data["next"]
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Example: 404 Not Found
        except requests.exceptions.ConnectionError:
            print("Connection error. Please check your internet connection.")
        except requests.exceptions.Timeout:
            print("Request timed out. Try again later.")
        except requests.exceptions.RequestException as err:
            print(f"An error occurred: {err}")

        for i in range(len(data["results"])):
            pokemon_list.append(data["results"][i]["name"])
    return pokemon_list


# TODO : TTS API for pokemon rap by generation
# Potential API for TTS for pokemon rap https://speechify.com/text-to-speech-api/


def get_generation(identifier):
    # Fetch generation details by ID or name.
    url = f"{BASE_URL}generation/{identifier}/"
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Example: 404 Not Found
    except requests.exceptions.ConnectionError:
        print("Connection error. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")
