import streamlit as st
import requests
import os

st.title("Your Online Bookshelf")
st.markdown("Welcome to Your Online Bookshelf! An app where you can search for any book and instantly receive information about it. Don't forget to leave a rating!")

cover = "images/bookshelf.jpeg"
st.image(cover)

book_title = st.text_input("Please Enter Book Title")

def book_details(book_title):
    base_url = "https://www.googleapis.com/books/v1/volumes"
    params = {'q': book_title}

    response = requests.get(base_url, params=params)
    data = response.json()

    if 'items' in data:
        first_book = data['items'][0]
        volume_info = first_book['volumeInfo']
        title = volume_info.get('title', 'No title available')
        authors = ', '.join(volume_info.get('authors', ['Unknown']))
        description = volume_info.get('description', 'No description available')
        image_link = volume_info['imageLinks']['thumbnail'] if 'imageLinks' in volume_info else None

        return title, authors, description, image_link
    else:
        return None

if st.button("Search"):  # NEW: Button
    if book_title:
        book_details = book_details(book_title)
        if book_details:
            title, authors, description, image_link = book_details

            st.header(title)
            if image_link:
                st.image(image_link, caption=title, use_column_width=True)

            st.subheader("Authors:")
            st.write(authors)

            st.subheader("Description:")
            st.write(description)
        else:
            st.write("Book not found. Please try a different title.")

user_rating = st.slider("Rate this Book (1-5)", min_value=1, max_value=5, value=3)  # NEW: Slider Input

if user_rating:
    st.write(f"You rated this book as: {user_rating} {'⭐️' * user_rating}")

st.markdown("---")

like_reading = st.checkbox("Check if you love reading")  # NEW: Checkbox Input

if like_reading:
    st.write("Go read, you deserve it!")
    st.image("images/goodday.jpeg")

else:
    st.warning("Its ok if you don't, thats why they make movies.")
    st.image("images/niceday.jpeg")

st.markdown("---")
st.markdown("Created by Bailey Finch")
