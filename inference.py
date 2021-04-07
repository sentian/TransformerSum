!git clone git@github.com:sentian/TransformerSum.git
!cd transformersum
!conda env create --file environment.yml

import os
os.chdir('/home/sentian/Projects/code/gentext/TransformerSum/src')
from extractive import ExtractiveSummarizer

## the model checkpoint needs to be downloaded from https://github.com/sentian/TransformerSum#extractive
## I use the roberta-base-ext-sum model
## change the path_to_checkpoint below
model = ExtractiveSummarizer.load_from_checkpoint("/home/sentian/Projects/model/gentext/transformersum/roberta-base-ext-sum/epoch=3.ckpt", strict=False)
text_to_summarize = "I love the extra heat rods which make more even heat. The farther back on the rack, \
the hotter it is. The controls are easy to understand and the pre-heat function  is a very nice thing to \
have. It heats up fast. Because the unit is small, the 1800W coils are able to heat it rapidly. \
The heating elements are radiant coils in a quartz tube. I really wish the unit had an extra heating \
element both top and bottom. The Breville is easy to use and heats up quickly. It heats up quickly and \
maintains temperature perfectly. My unit has a 'hot spot' in the right rear corner. It gets a good even \
heat on both sides. It gets hot very quickly so preheating takes no time. The temperature and time display \
is very easy to read. The unit is very light so I can move it to my island if I am worried about the heat. \
It is easy to operate, great dial choices, easy to set or adjust time and temp. Great preheat function. \
The automatic preheat feature is nicer than I expected and the size is perfect. Heats up VERY quickly. \
Way louder than my full size Breville."
summary = model.predict(text_to_summarize, num_summary_sentences=5)
print(summary)
