import nltk

# Specify the directory to download the NLTK data
download_dir = './nltk_data'

# Download the required NLTK data packages to the specified directory
nltk.download('punkt_tab', download_dir=download_dir)
nltk.download('averaged_perceptron_tagger', download_dir=download_dir)