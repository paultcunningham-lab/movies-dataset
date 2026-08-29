import altair as alt
import pandas as pd
import streamlit as st
import Exp
import requests
SEARCHKEY = =   st.secrets["SEARCH_API"] 

# Show the page title and description.
st.set_page_config(page_title="Movies dataset", page_icon="🎬")
st.title("🎬 Movies dataset")
st.write(
    """
    This app visualizes data from [The Movie Database (TMDB)](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata).
    It shows which movie genre performed best at the box office over the years. Just 
    click on the widgets below to explore!
    """
)

def brave_search(query, subscription_token, max_results=5):
    url = "https://api.search.brave.com/res/v1/web/search"
    headers = {
        "Accept": "application/json",
        "Accept-Encoding": "gzip",
        "X-Subscription-Token": subscription_token
    }
    params = {"q": query}
    resp = requests.get(url, headers=headers, params=params, timeout=20)
    resp.raise_for_status()
    return resp.json().get("web", {}).get("results", [])[:max_results]
# Load the data from a CSV. We're caching this so it doesn't reload every time the app
# reruns (e.g. if the user interacts with the widgets).

@st.cache_data
def load_data():
    df = pd.read_csv("data/movies_genres_summary.csv")
    return df


#f = load_data()
df= Exp.returner()

with st.form(key="text_form2"):
    # Text entry field
    user_input2 = st.text_input("Enter your text:")

    # Form submit button
    submit_button2 = st.form_submit_button(label="Submit2")

# Process the input only when the submit button is clicked
if submit_button2:
    if user_input2.strip():
        st.success(f"Submitted text: {user_input}")
    else:
        st.warning("Please enter some text before submitting.")

searchterm = user_input2
results= brave_search(user_input2, SEARCHKEY, max_results=5)

df3 = pd.DataFrame(results)[["title"]]



with st.form(key="text_form"):
    # Text entry field
    user_input = st.text_input("Enter your text:")

    # Form submit button
    submit_button = st.form_submit_button(label="Submit")

# Process the input only when the submit button is clicked
if submit_button:
    if user_input.strip():
        st.success(f"Submitted text: {user_input}")
    else:
        st.warning("Please enter some text before submitting.")
# Show a multiselect widget with the genres using `st.multiselect`.


genres = user_input.strip()


months = st.slider("months", 1,12)
                   
# Show a slider widget with the years using `st.slider`.
years = st.slider("Years", 1986, 2006, (2000, 2016))

# Filter the dataframe based on the widget input and reshape it.
#df_filtered = df[(df["genre"] == genres) & (df["year"].between(years[0], yea,rs[1]))]
#df_reshaped = df_filtered.pivot_table(
   # index="year", columns="genre", values="gross", aggfunc="sum", fill_value=0
#)
#df_reshaped = df_reshaped.sort_values(by="year", ascending=False)

df_reshaped=df
# Filter rows where values in Column Index 0 equal "Apple"
df_reshaped = df[df.iloc[:, 5] == genres]
st.dataframe(
    df3,
    use_container_width=True,

)
# Display the data as a table using `st.dataframe`.
st.dataframe(
    df_reshaped,
    use_container_width=True,
    column_config={"year": st.column_config.TextColumn("Year")},
)

