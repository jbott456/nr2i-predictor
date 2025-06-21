{\rtf1\ansi\ansicpg1252\cocoartf2761
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # \uc0\u9918  NR2I Predictor\
\
**Predict which MLB games are most likely to have no runs scored in the 2nd inning (NR2I).**  \
This app helps bettors and baseball analysts find high-confidence value picks based on early-inning pitcher control, team 2nd-inning scoring stats, and league trends.\
\
---\
\
## \uc0\u55357 \u56589  What It Does\
\
- Displays today\'92s MLB matchups\
- Estimates NR2I probability using:\
  - Pitcher ERA/WHIP performance\
  - Opponent 2nd-inning run rates\
  - League-wide scoring baseline\
- Ranks games and highlights top value plays\
\
---\
\
## \uc0\u55357 \u56960  Try the Live App\
\
\uc0\u55357 \u56393  **Streamlit App:** [https://nr2i-predictor.streamlit.app](https://nr2i-predictor.streamlit.app)  \
> *(Publicly available \'96 no login required)*\
\
---\
\
## \uc0\u55357 \u56567  App Preview\
\
![NR2I Predictor Screenshot](https://user-images.githubusercontent.com/your-username/your-screenshot.png)\
\
*(Optional \'96 add this if you upload a screenshot to the GitHub repo later)*\
\
---\
\
## \uc0\u55358 \u56810  Run Locally\
\
Clone the project and install dependencies:\
\
```bash\
git clone https://github.com/jbott456/nr2i-predictor.git\
cd nr2i-predictor\
python3 -m venv .venv\
source .venv/bin/activate\
pip install -r requirements.txt\
streamlit run app.py\
\uc0\u55357 \u57056 \u65039  Built With\
Python\
\
Streamlit\
\
Pandas\
\
scikit-learn (for future model development)\
\
\uc0\u55357 \u56520  Upcoming Features\
\uc0\u55358 \u56800  True machine learning model w/ 2nd-inning splits\
\
\uc0\u55358 \u56830  Daily sportsbook odds integration\
\
\uc0\u9989  Hit/miss tracker (prediction accuracy)\
\
\uc0\u55357 \u56496  Monetization via subscription or affiliate\
\
\uc0\u55357 \u56424 \u8205 \u55357 \u56507  Author\
Jason Abbott\
txtvis.com\
GitHub: @jbott456\
\
\uc0\u55357 \u56540  License\
MIT License}