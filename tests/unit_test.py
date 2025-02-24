#! python3
import pytest
import requests
import pokeapi.pokemon_api as pokemon_api


@pytest.fixture
def api():
    return pokemon_api


def test_get_pokemon_api(api):
    """Test fetching a pokemon from API"""
    identifier_name = "ivysaur"
    identifier_number = 2

    response_by_name = api.get_pokemon(identifier_name)
    # Assertions to check expected response structure
    assert response_by_name is not None
    assert isinstance(response_by_name, dict)
    assert response_by_name.get("name") == "ivysaur"
    assert response_by_name.get("id") == 2

    response_by_number = api.get_pokemon(identifier_number)
    assert response_by_number is not None
    assert isinstance(response_by_number, dict)
    assert response_by_number.get("name") == "ivysaur"
    assert response_by_number.get("id") == 2


# TODO Test cases for list_pokemon


# TODO Test cases for get_generation
