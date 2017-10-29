from wordcloud import WordCloud 
import matplotlib.pyplot as plt 
import numpy as np 
 # to import the image 
from PIL import Image

# Create a list of word (https://en.wikipedia.org/wiki/Data_visualization) 
text=("Data visualization or data visualisation is viewed by many disciplines as a modern equivalent of visual communication. It involves the creation and study of the visual representation of data, meaning information that has been abstracted in some schematic form, including attributes or variables for the units of information A primary goal of data visualization is to communicate information clearly and efficiently via statistical graphics, plots and information graphics. Numerical data may be encoded using dots, lines, or bars, to visually communicate a quantitative message.[2] Effective visualization helps users analyze and reason about data and evidence. It makes complex data more accessible, understandable and usable. Users may have particular analytical tasks, such as making comparisons or understanding causality, and the design principle of the graphic (i.e., showing comparisons or showing causality) follows the task. Tables are generally used where users will look up a specific measurement, while charts of various types are used to show patterns or relationships in the data for one or more variables") 

# Load the image (http://www.bio-key.com/img/fingerprint.png) 
image_mask = np.array(Image.open( "fingerprint.png")) 

# Make the figure 
wordcloud = WordCloud(mask=image_mask).generate(text) 
plt.figure() 
plt.imshow(wordcloud, interpolation="bilinear") 
plt.axis("off") 
#plt.margins(x=0, y=0) 
plt.show() 
