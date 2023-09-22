import streamlit as st
import requests
from bs4 import BeautifulSoup

# Define the Streamlit app title
st.title("Web Scraper with Streamlit")

# Create input fields for base_url, start_number, and end_number
base_url = st.text_input("Enter Base URL:", "https://new9.gdtot.cfd/file/")
start_number = st.number_input("Enter Start Number:", 600000000)
end_number = st.number_input("Enter End Number:", 671630612)

# Create a button to trigger the scraping process
if st.button("Scrape URLs"):
    # Initialize a counter for live URLs
    live_url_count = 0

    try:
        # Display progress text
        progress_text = st.empty()

        for file_number in range(int(start_number), int(end_number) + 1):
            # Construct the full URL
            url = base_url + str(file_number)

            # Send an HTTP GET request to the URL
            response = requests.get(url)

            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the HTML content of the page
                soup = BeautifulSoup(response.text, 'html.parser')

                # Find the title tag in the HTML
                title_tag = soup.find('title')

                if title_tag:
                    # Display the text inside the title tag
                    st.write(f"URL: {url}, Title: {title_tag.text}")
                else:
                    st.write(f"URL: {url}, Title not found on the page.")

                # Increment the live URL count
                live_url_count += 1

            # Calculate and display progress
            progress = (file_number - int(start_number)) / (int(end_number) - int(start_number)) * 100
            progress_text.text(f"Progress: {progress:.2f}%")

        # Display the total number of live URLs
        st.write(f"Total Live URLs: {live_url_count}")

    except requests.exceptions.RequestException as e:
        st.error(f"An error occurred: {e}")
