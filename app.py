import streamlit as st

def dessert_order():
    flavour = st.text_input("What flavour would you like?")
    dessert_type = st.text_input("What type of dessert would you like?")
    order_button = st.button("Place Order")

    if order_button:
        st.write("You have ordered", flavour + "-" + dessert_type)

# Main app
def main():
    st.title("Dessert Ordering App Interface \n \n created by Vignesh for practice purpose")
    dessert_order()

if __name__ == "__main__":
    main()
