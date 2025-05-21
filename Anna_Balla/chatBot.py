# API url
# https://aimlapi.com/app/keys

import requests

def chatbot(query):

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()['choices'][0]['message']['content']
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return "Sorry, something went wrong with the chat service."
    except Exception as err:
        print(f"An error occurred: {err}")
        return "Sorry, something went wrong."

