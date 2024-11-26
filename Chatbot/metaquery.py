import re
from langchain_community.vectorstores import Chroma
import openai
from langchain_openai import OpenAIEmbeddings
import os
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

CHROMA_PATH = "chroma"

openai.api_key = os.getenv("OPENAI_API_KEY")


# Metadata mapping for demonstration (assign dynamically based on your logic)
METADATA_MAP = {
    "bca.md": {"courses": ["BCA","Bachelor in Computer Application","Computer Application"], "university": ["Tribhuvan University", "TU"]},

    "bim.md": {"courses": ["BIM","Bachelor in Information Management","Information Management"], "university": ["Tribhuvan University", "TU"]},

    "csit.md": {"courses": ["CSIT","BSc.CSIT","Bachelor in Computer Science and Information Technology","Computer Science and Information Technology"], "university": ["Tribhuvan University", "TU"]},

    "bit.md": {"courses": ["BIT","Bachelor in Information Technology","Information Technology","Bachelor in IT"], "university": ["Tribhuvan University", "TU"]},

    "cs-ku.md": {"courses": ["BSc.CS","Bachelor in Computer Science","Computer Science"], "university": ["Kathmandu University", "KU"]},

    "btechAI.md": {"courses": ["B.Tech AI","btech AI","Bachelor in Artificial Intelligence","Artificial Intelligence","Bachelor of Technology in AI"], "university": ["Kathmandu University", "KU"]},

    "bce-tu.md": {"courses": ["BCE","Bachelor in Civil Engineering","Civil Engineering","BE Civil","Civil Eng","Civil"], "university": ["Tribhuvan University", "TU"]},

    "ce-ku.md": {"courses": ["BE Civil","Bachelor in Civil Engineering","Civil Engineering","Civil Eng","Civil"], "university": ["Kathmandu University", "KU"]},

    # "be-electrical.md": {"courses": ["BE Electrical","Bachelor in Electrical Engineering","Electrical Engineering","Electrical Eng"], "university": ["Kathmandu University", "KU"]},
    "be-aero-tu.md": {"courses": ["BE Aerospace","Bachelor in Aerospace Engineering","Aerospace Engineering","Aerospace Eng","Aerospace"], "university": ["Tribhuvan University", "TU"]},

    "be-agriculture-tu.md": {"courses": ["BE Agriculture","Bachelor in Agriculture Engineering","Agriculture Engineering","Agriculture Eng"], "university": ["Tribhuvan University", "TU"]},

    "be-automobile-tu.md": {"courses": ["BE Automobile","Bachelor in Automobile Engineering","Automobile Engineering","Automobile Eng"], "university": ["Tribhuvan University", "TU"]},
    
    "be-elect-ku.md": {"courses": ["BE Electrical and Electronics","Bachelor in Electrical and Electronics Engineering","Electrical and Electronics Engineering","Electrical Eng","Electrical Engineering","Electronics Engineering","Electronics Eng","Electronics and Electrical"], "university": ["Kathmandu University", "KU"]},

    "be-geomatics-ku.md": {"courses": ["BE Geomatics","Bachelor in Geomatics Engineering","Geomatics Engineering","Geomatics Eng","Geomatics"], "university": ["Kathmandu University", "KU"]},

    "be-industrial-tu.md": {"courses": ["BE Industrial","Bachelor in Industrial Engineering","Industrial Engineering","Industrial Eng","Industrial"], "university": ["Tribhuvan University", "TU"]},

    "be-mechanical-tu.md": {"courses": ["BE Mechanical","Bachelor in Mechanical Engineering","Mechanical Engineering","Mechanical Eng","Mechanical"], "university": ["Tribhuvan University", "TU"]},

    "be-elect-TU.md": {"courses": ["BE Electronics Information and Communication","Bachelor in Electronics Engineering","Bachelor of Electronics, Communication and Information Engineering","Electronics, Information and Communication Engineering","Electronics Eng","Information Eng","Communication Eng","Electronics Information and Communication"], "university": ["Tribhuvan University", "TU"]},

    "bel-tu.md":{"courses":["BE Electrical","Bachelor in Electrical Engineering","Electrical Engineering","Electrical Eng"], "university": ["Tribhuvan University", "TU"]},

    "bit-herald.md": {"courses": ["BIT","Bachelor in Information Technology","Information Technology","Bachelor in IT","bsc hons","hons"], "university": ["Herald College", "Herald","University of Wolverhampton","Herald College Kathmandu","foreign university"]},

    "bsc-comp-islington.md": {"courses": ["BSc Computing","Bachelor in Computing","Computing","bsc hons","hons"], "university": ["Islington College", "Islington","London Metropolitan University","London Met University","foreign university"]},

    "CE_TU.md":{"courses":["BE Computer","Bachelor in Computer Engineering","Computer Engineering","Computer Eng","Comp Eng","Comp Engineering","Bachelor of Engineering in Computer Engineering"], "university": ["Tribhuvan University", "TU"]},

    "CE-KU.md":{"courses":["BE Computer","Bachelor in Computer Engineering","Computer Engineering","Computer Eng","Comp Eng","Comp Engineering","Bachelor of Engineering in Computer Engineering"], "university": ["Kathmandu University", "KU"]},

    "se-pu.md": {"courses": ["Software Engineering","Bachelor in Software Engineering","Software Eng","Software","Bachelor in Software","Bachelor of Engineering in Software Engineering"], "university": ["Pokhara University", "PU"]},

    "be-chemical-tu.md": {"courses": ["BE Chemical","Bachelor in Chemical Engineering","Chemical Engineering","Chemical Eng","Bachelor of Engineering in Chemical Engineering"], "university": ["Tribhuvan University", "TU"]},

}

# Create lists of universities and courses to match against
universities = []
courses = []

# Extract universities and courses from METADATA_MAP
for entry in METADATA_MAP.values():
    universities.extend(entry["university"])
    courses.extend(entry["courses"])

# Create a pattern to match whole words from the list (for initial filtering)
university_pattern = r"\b(" + "|".join([re.escape(u) for u in universities]) + r")\b"
course_pattern = r"\b(" + "|".join([re.escape(c) for c in courses]) + r")\b"

# Function to get the best match using fuzzywuzzy
def get_best_match(input_text, options):
    # Use fuzzy matching to find the best match from the list of options
    match, score = process.extractOne(input_text, options, scorer=fuzz.token_sort_ratio)
    return match if score > 80 else None  # Adjust threshold as needed

# Function to extract universities and courses with fuzzy matching
def extract_info_from_prompt(prompt):
    # Find all possible universities and courses using regex
    universities_found = re.findall(university_pattern, prompt,re.IGNORECASE)
    courses_found = re.findall(course_pattern, prompt,re.IGNORECASE)

    # Apply fuzzy matching to the university found in the prompt
    fuzzy_universities = [get_best_match(u, universities) for u in universities_found]
    fuzzy_courses = [get_best_match(c, courses) for c in courses_found]

    # Filter out None values for matches that were too ambiguous
    fuzzy_universities = list(filter(None, fuzzy_universities))
    fuzzy_courses = list(filter(None, fuzzy_courses))

    return fuzzy_universities, fuzzy_courses

# Function to query the metadata map based on extracted course and university
def query_metadata(prompt):
    # Extract course and university from the prompt
    universities_found, courses_found = extract_info_from_prompt(prompt)

    # Inform the user if no course or university is found
    if not universities_found:
        print("No university found in the prompt.")
    if not courses_found:
        print("No course found in the prompt.")

    # If no course or university was found, return empty or default message
    if not universities_found and not courses_found:
        return "Please provide course and university details in the prompt."

    # Filter METADATA_MAP based on extracted course and university
    filtered_results = []
    for key, entry in METADATA_MAP.items():
        # Check if the extracted courses and universities match with the metadata
        course_match = any(course in courses_found for course in entry["courses"]) if courses_found else True
        university_match = any(university in universities_found for university in entry["university"]) if universities_found else True
        
        if course_match and university_match:
            filtered_results.append({key: entry})
    
    # Return the results or a message if no matching entries are found
    if filtered_results:
        return filtered_results
    else:
        return "No matching courses or universities found in the metadata."

# Example usage
prompt = "Can you tell me about the Computer Engineering course ?"

result = query_metadata(prompt)
print(result)
