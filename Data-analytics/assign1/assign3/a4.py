import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Step 1: Read the WhatsApp chat from the exported .txt file
def read_whatsapp_chat(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Step 2: Tokenize the read data into sentences
def tokenize_sentences(text):
    return sent_tokenize(text)

# Step 3: Remove stopwords and perform lemmatization
def preprocess_text(text):
    # Tokenize into words
    words = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.lower() not in stop_words]
    
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_words]
    
    return lemmatized_words

# Step 4: Plot WordCloud
def plot_wordcloud(text):
    wordcloud = WordCloud(width = 800, height = 800, 
                background_color ='white', 
                stopwords = stopwords, 
                min_font_size = 10).generate(text) 

    # plot the WordCloud image                        
    plt.figure(figsize = (8, 8), facecolor = None) 
    plt.imshow(wordcloud) 
    plt.axis("off") 
    plt.tight_layout(pad = 0) 

    plt.show() 

# Main function
if __name__ == "__main__":
    # i. Read WhatsApp chat
    whatsapp_chat = read_whatsapp_chat("whatsapp_chat.txt")

    # ii. Tokenize into sentences
    sentences = tokenize_sentences(whatsapp_chat)
    print("Tokenized Sentences:")
    for sentence in sentences:
        print(sentence)

    # iii. Remove stopwords and perform lemmatization
    preprocessed_text = preprocess_text(whatsapp_chat)
    print("\nPreprocessed Text:")
    print(preprocessed_text)

    # iv. Plot WordCloud
    text = ' '.join(preprocessed_text)
    plot_wordcloud(text)
