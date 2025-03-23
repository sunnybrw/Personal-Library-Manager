import streamlit as st
import json
# Load and save Library data
def load_library():
    try:
        with open("library.json","r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
def save_library():
        with open ("library.json","w") as file:
            json.dump(library,file, indent=4)
#Initialize Library
library=load_library()
st.title("Personal Library Manager")
menu = st.sidebar.radio("Select an Option",["View Library","Add Book", "Remove Book","Search Book","Save & Exit"])
if menu == "View Library":
    st.sidebar.title("your Library")
    if library :
            st.table(library)
    else:
            st.write("your library is empty")
    #Add book
elif  menu == "Add Book":
      st.sidebar.title("Add a new Book")
      title = st.text_input("title")
      author = st.text_input("author")
      year = st.number_input("year",min_value=2022,max_value=2100, step=1)
      Genre=st.text_input("Genre")
      read_status=st.checkbox("Mark as read")

      if  st.button("Add Book"):
        library.append({"title":title,"author":author,"year":year,"Genre":Genre,"read_status":read_status,})
        save_library()
        st.success("Books added successfully")
        st.rerun()
#Remove Book
elif menu == "Remove Book":
     st.sidebar.title("Remove Book")
     book_titles = [book["title"] for book in library]
     if book_titles:
        selected_book  = st.selectbox("select a book to remove", book_titles)
        if st.button("Remove Book"):
           library = [ book for book in library if book ["title"] !=selected_book]
        save_library()
        st.success("Books removed successfully")
        st.rerun()
     else :
          st.warning("No Book in your library. Add some books")
#Search books
elif menu == "Search Book" :
    st.sidebar.title("Search Book")
    search_term = st.text_input("Enter title or author name")
    if st.button("Search"):
        results = [book for book in library if search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower()]
        if results:
             st.table(results)
        else:
             st.warning("No Book Found")
elif menu == "Save & Exit":
    save_library()
    st.success("Library saved successfully")
