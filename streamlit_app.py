import streamlit

streamlit.title('my parents new healthy diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🍜Omega 3 and blueberry oatmeal')
streamlit.text('🥗Kale, spinach & rocket smoothie')
streamlit.text('🐔hard-boild and free-range egg')
streamlit.text('🥑🍞avocado toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
