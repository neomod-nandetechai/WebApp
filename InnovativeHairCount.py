import streamlit as st
from PIL import Image  # corrected import for PIL
import numpy as np
import matplotlib.pyplot as plt

# simulate hair follicle counting function (you'd replace this with your actual model)
def count_follicles(image):
    return 997  # example count

# simulate function to segment the image (replace with actual segmentation model)
def segment_image(image):
    return image

# set page config
st.set_page_config(page_title="Innovative Hair Counting", layout="wide")

# create sidebar for navigation
st.sidebar.title("Navigation")
st.sidebar.markdown(
    """
    <style>
    .nav-sidebar {
        background-color: #000080; /* navy blue */
        color: white; /* text color */
    }
    </style>
    """, unsafe_allow_html=True
)

page = st.sidebar.radio("Go to:", ["Home", "Counting", "Visualization", "About"])

# Initialize counts at the start of the app (global variables)
implanted_follicle_count = None
removed_follicle_count = None

if page == "Home":
    # set up homepage with blue background
    st.markdown(
        """
        <style>
        .background {
            background-color: #add8e6;
            min-height: 100vh;
            padding: 20px;
            text-align: center;
            color: black; /* set text color */
        }
        </style>
        <div class="background">
            <h1>Follicle Count App</h1>
            <p>This app helps you count hair follicles in transplant images, reducing costs and enhancing customer satisfaction.</p>
            <p>Navigate to the counting section to start using the app.</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "Counting":
    # page for image upload with background
    st.markdown(
        """
        <style>
        body {
            background-image: url("file:///users/neomodibedi/hairtransplantapp/webapp/generate.png"); /* replace with your local path */
            background-size: cover;
            background-repeat: no-repeat;
            min-height: 100vh;
        }
        </style>
        """, unsafe_allow_html=True)

    st.title("Upload Hair Transplant Images")
    st.write("Upload a hair transplant image to count the number of hair follicles.")

    # upload implanted hair follicles
    st.subheader("Upload Implanted Hair Follicles")
    uploaded_implanted_image = st.file_uploader("Implanted Hair Image", type=["jpg", "png", "jpeg"])

    # upload removed hair follicles
    st.subheader("Upload Removed Hair Follicles")
    uploaded_removed_image = st.file_uploader("Removed Hair Image", type=["jpg", "png", "jpeg"])

    # check if implanted image is uploaded
    if uploaded_implanted_image is not None:  # use None with a capital 'N'
        # open and display the uploaded implanted image
        implanted_image = Image.open(uploaded_implanted_image)
        st.image(implanted_image, caption="Uploaded Implanted Image", use_column_width=True)

        # simulate segmentation and display the segmented implanted image
        segmented_implanted_image = segment_image(implanted_image)
        st.image(segmented_implanted_image, caption="Segmented Implanted Image", use_column_width=True)

        # count the follicles and display the count
        implanted_follicle_count = count_follicles(implanted_image)
        st.write(f"**Implanted Follicle Count**: {implanted_follicle_count} follicles")

    # check if removed image is uploaded
    if uploaded_removed_image is not None:  # use None with a capital 'N'
        # open and display the uploaded removed image
        removed_image = Image.open(uploaded_removed_image)
        st.image(removed_image, caption="Uploaded Removed Image", use_column_width=True)

        # simulate segmentation and display the segmented removed image
        segmented_removed_image = segment_image(removed_image)
        st.image(segmented_removed_image, caption="Segmented Removed Image", use_column_width=True)

        # count the follicles and display the count
        removed_follicle_count = count_follicles(removed_image)
        st.write(f"**Removed Follicle Count**: {removed_follicle_count} follicles")

    # optionally, add footer information
    st.write("---")
    st.write("This app was developed to automate hair follicle counting using machine learning models.")

elif page == "Visualization":
    st.title("Follicle Count Comparison")
    st.write("We compare the counted Implanted Vs Removed Follicles")

    # Check if values are available for comparison
    if implanted_follicle_count is None or removed_follicle_count is None:
        st.write("Nothing to compare so far!!")
    else:
        # Create a bar chart for comparison
        counts = [implanted_follicle_count, removed_follicle_count]
        labels = ['Implanted Follicles', 'Removed Follicles']

        fig, ax = plt.subplots()
        ax.bar(labels, counts, color=['blue', 'orange'])
        ax.set_ylabel('Count of Follicles')
        ax.set_title('Comparison of Follicle Counts')

        st.pyplot(fig)

elif page == "About":
    # about page with blue background
    st.markdown(
        """
        <style>
        .background {
            background-color: #add8e6;
            min-height: 100vh;
            padding: 20px;
            text-align: center;
            color: black; /* set text color */
        }
        </style>
        <div class="background">
            <h1>About Follicle Count App</h1>
            <p>This application leverages advanced image processing techniques to accurately count hair follicles in photographs of hair transplants.</p>
            <p>Our goal is to streamline the process and improve patient satisfaction by providing quicker and more accurate follicle counts.</p>
            <p>For more information, feel free to contact us or check our website.</p>
        </div>
        """, unsafe_allow_html=True)
