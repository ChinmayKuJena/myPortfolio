import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(
    page_title="Chinmay Jena's Portfolio",
    page_icon="🚀",
    layout="wide",
)

# CSS for background GIF
st.markdown("""
    <style>
        header {visibility: hidden;}
    footer {visibility: hidden;}
    body {
        background-image: url('https://user-images.githubusercontent.com/35409648/74775140-0373ab80-528d-11ea-8acd-9499c85a697f.gif'); /* Add your background image URL */
        background-size: cover;
        background-repeat: no-repeat;
        animation: backgroundAnimation 30s infinite alternate;
    }
        /* Keyframes for Animation */
    @keyframes backgroundAnimation {
        0% { opacity: 1; }
        100% { opacity: 0.7; } /* Adjust opacity for the animation effect */
    }

    .main {
        background: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# Main content
st.title("Chinmay Jena's Portfolio")
st.markdown("### A Passionate Backend Developer with Expertise in Spring Boot and AWS")
st.write("🌱 **Currently learning**: Spring Boot, AWS, NestJS, and TypeScript")
st.write("📫 **Contact**: [chinmay.jena7878@gmail.com](mailto:chinmay.jena7878@gmail.com)")
st.write("[LinkedIn Profile](https://www.linkedin.com/in/chinmay-jena-0234642a0)")

# About Me Section
st.header("About Me")
st.write("""
I am a backend developer dedicated to creating robust applications with cutting-edge technology. 
I specialize in Spring Boot, AWS, and am expanding my expertise to include NestJS and TypeScript.
""")

# Internships Section
st.header("Internships")
st.markdown("""
- **Sandaltreesoft** (Backend Developer): Working on creating models that integrate Google Maps API to provide detailed shop listings.
- **Skytreesoft** (Backend Developer & AWS Specialist): Developed custom image scraping tools using Python and facilitated communication between AWS services like SQS, S3, and RDS.
""")

# Skills Section
st.header("Skills")
skills = [
    "Spring Boot",
    "AWS (S3, RDS, SQS)",
    "Python",
    "Google Maps API",
    "NestJS (learning)",
    "TypeScript (learning)",
    "SQl",
    "PSQL",
    "REDIS",
    "MongoDb"
]
for skill in skills:
    st.markdown(f"- {skill}")

# Projects Section
st.header("Projects")
# projects = {
#     "Shop Listing API using Google Maps": "https://github.com/yourusername/shop-listing-api",
#     "Image Scraping Tool with AWS Integration": "https://github.com/yourusername/image-scraper-aws",
# }
# for project, link in projects.items():
#     st.markdown(f"[{project}]({link})")
st.markdown('Adding soon')
# Footer
st.markdown("---")
st.write("For more details, feel free to contact me at: [chinmay.jena7878@gmail.com](mailto:chinmay.jena7878@gmail.com)")
