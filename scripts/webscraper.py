import requests
from bs4 import BeautifulSoup

import tkinter as tk
import time
def show_window():
    # Create the main window
    window = tk.Tk()

    # Set the window title
    window.title("Hello, Window!")

    # Create a label with a message
    label = tk.Label(window, text="This is a simple window.")

    # Pack the label into the window
    label.pack()

    # Start the main event loop
    window.mainloop()

# Call the function to show the window
show_window()


def get_last_online_status(url):
    # Send an HTTP request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using Beautiful Soup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the <td> element containing the text "Last online"
        last_online_td = soup.find('td', string='Last online')

        # Check if the element is found
        if last_online_td:
            # Extract the content directly below the "Last Online" <td> element
            next_td = last_online_td.find_next('td')
            if next_td:
                return next_td.text.strip()
            else:
                return "No content found below 'Last Online'."

        else:
            return "'Last Online' not found on the page."

    else:
        return f"Failed to retrieve the page. Status code: {response.status_code}"

print('starting...')
characters = ['Gow Mxligno', 'Taty Gatinha']
for i in range(0, len(characters)):
    characters[i] = characters[i].replace(" ", "%20")

# Use the HTML content directly instead of fetching from a URL
while True:
    for c in characters:
        status = get_last_online_status('https://www.rucoyonline.com/characters/'+c)
        if (status == 'currently online'):
            print('got through!')
            show_window()
            time.sleep(20)
    # else: print('failed')
    time.sleep(3)
