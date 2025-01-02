import streamlit as st
from datetime import datetime
import pytz
from PIL import Image

# Function to generate a dynamic greeting
tz = pytz.timezone("Asia/Kolkata")
def get_greeting():
    # Get the current time in the user's time zone
    current_time = datetime.now(tz)
    current_hour = current_time.hour
    current_day = current_time.strftime("%A")

    # Determine greeting based on current hour
    if 5 <= current_hour < 12:
        greeting = "Good Morning ☀️"
    elif 12 <= current_hour < 17:
        greeting = "Good Afternoon🕛🏙️"
    elif 17 <= current_hour < 21:
        greeting = "Good Evening🌃"
    else:
        greeting = "Good Night🌝"

    return f"{greeting},Happy {current_day}! "

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
            background-image: url('https://user-images.githubusercontent.com/35409648/74775140-0373ab80-528d-11ea-8acd-9499c85a697f.gif');
            background-size: cover;
            background-repeat: no-repeat;
            animation: backgroundAnimation 30s infinite alternate;
        }
        /* Keyframes for Animation */
        @keyframes backgroundAnimation {
            0% { opacity: 1; }
            100% { opacity: 0.7; }
        }

        .main {
            background: rgba(255, 255, 255, 0.8);
            border-radius: 10px;
            padding: 10px;
        }
    </style>
    """, unsafe_allow_html=True)

# Main content
current_time = datetime.now(tz)
formatted_date = current_time.strftime("%d/%m/%Y")

st.markdown(f"<h3 style='color:orange;'>{get_greeting()}</h3>", unsafe_allow_html=True)
st.markdown(f"<h3 style='color:orange;'>Today's Date: {formatted_date}</h3>", unsafe_allow_html=True)


st.title("Chinmay Jena's Portfolio")
st.markdown("### A Passionate Backend Developer with Expertise in Spring Boot and AWS")
st.write("🌱 **Currently learning**: Spring Boot, AWS, NestJS, and TypeScript")
st.write("📫 **Contact**: [My Email](mailto:chinmay.jena7878@gmail.com)")
st.write("🏢**LinkedIn**:[ChinmayKuJena](https://www.linkedin.com/in/chinmay-jena-0234642a0)")
st.write("🔥**GitHub**:[ChinmayKuJena](https://github.com/ChinmayKuJena)")

# About Me Section
st.header("About Me")
st.write("""
I am a backend developer dedicated to creating robust applications with cutting-edge technology. 
I specialize in Spring Boot, AWS, and am expanding my expertise to include NestJS and TypeScript.
""")

# Internships Section
st.header("Internships")
st.markdown("""
- [**Sandaltreesoft**](https://www.linkedin.com/company/sandal-tree-soft/) (Backend Developer): Working on creating models that integrate Google Maps API to provide detailed shop listings.
- [**Skytreesoft**](https://www.linkedin.com/company/skytreesoft/) (Backend Developer & AWS Specialist): Developed custom image scraping tools using Python and facilitated communication between AWS services like SQS, S3, and RDS.
""")

# Skills Section
st.header("Skills")
skills_links = [
    "[Spring Boot](https://spring.io/projects/spring-boot)",
    "[AWS (S3, RDS, SQS)](https://aws.amazon.com/)",
    "[Python](https://www.python.org/)",
    "[Google Maps API](https://developers.google.com/maps/documentation)",
    "[NestJS](https://nestjs.com/) (learning)",
    "[TypeScript](https://www.typescriptlang.org/) (learning)",
    "[SQL](https://en.wikipedia.org/wiki/SQL)",
    "[PostgreSQL](https://www.postgresql.org/)",
    "[Redis](https://redis.io/)",
    "[MongoDB](https://www.mongodb.com/)"
]
skills_line = " | ".join(skills_links)
st.markdown(skills_line, unsafe_allow_html=True)

# Projects Section
st.header("Projects")
projects = [
    "This is a Spring Boot service that can scrape nearby places of a particular location and their coordinates. [GitHub Repository](https://github.com/ChinmayKuJena/googleMapScrapper.git)",
    "A simple NestJs API service of Groq AI. [GitHub Repository](https://github.com/ChinmayKuJena/groqApi.git)",
    "This is a Spring Boot service integrated with Groq where we modify the output of Groq and save it as our dataset for Service 1. Known as Service 2. [GitHub Repository](https://github.com/ChinmayKuJena/groqDatacreater.git)",
    "Dynamic Kafka consumer to consume messages from a topic and dynamically CRUD. [GitHub Repository](https://github.com/ChinmayKuJena/Kafka-consumer.git)",
    "Simple tour guide API service with Groq AI, implemented in Python using Streamlit with a UI. [GitHub Repository](https://github.com/ChinmayKuJena/simpleTourGuid.git)",
    "My email service for sending simple, HTML, or attachment emails using Flask and Spring Boot. [GitHub Repository](https://github.com/ChinmayKuJena/myEmailService.git)",
    "Map scraping service for scraping Google Map data of a particular place. This project provides a tool to scrape business information from Google Maps using Python and Playwright, allowing searches based on a query and saving results in CSV and Excel formats. [GitHub Repository](https://github.com/ChinmayKuJena/mapScraping.git)"
]

# Display each project
for project in projects:
    st.markdown(f"- {project}")

# GitHub Stats Section
st.header("GitHub Stats")
st.markdown("""
<p><img align="center" src="https://github-readme-stats.vercel.app/api/top-langs?username=chinmaykujena&show_icons=true&locale=en&layout=compact" alt="Top Languages" /> <img align="center" src="https://github-readme-streak-stats.herokuapp.com/?user=chinmaykujena&" alt="GitHub Streak" /></p>  
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.write("For more details, feel free to contact me at: [chinmay.jena7878@gmail.com](mailto:chinmay.jena7878@gmail.com)")
