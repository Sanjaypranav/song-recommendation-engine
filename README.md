# Spotify Regional Song Recommendation

## Problem Statement 
To Recommend user choice based on his mood  songs from Spotify data.


## Abstract

Recommender systems have taken the entertainment and e-commerce industries by storm. Amazon, Netflix, and Spotify are great examples. In this project, we have designed song recommendation systems using various algorithms.

We have scraped the data from the spotify using a python library called **[spotipy](https://spotipy.readthedocs.io/en/2.19.0/)** and used the data to build a recommendation model using **content based filtering** method to provide recommendations for songs based on similar songs.



## Dataset description
Regional Spotify songs (Tamil) with features. Data has been collected using Spotipy API 

**Acousticness** — A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic.

**Danceability** — Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is the most danceable

**Energy** — Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy.

**Loudness** — The overall loudness of a track in decibels (dB). Values typical range between -60 and 0 dB.

**Valence** — A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive.

**Tempo** — The overall estimated tempo of a track in beats per minute (BPM).

**Popularity** — The popularity of the track. The value will be between 0 and 100, with 100 being the most popular.
 

# Algorithm used   


    Cosine Similarity 

    

# App deployment  
 
FLASK APP

# To run this Project locally

Step 1: Create conda environment

```
conda create -n env_name python=3.7 -y

```
 Linux users
```
virtual env python=python3.9 env_name

```


Step 2:  clone the repo 

```
git clone https://github.com/Sanjaypranav/song-recommendation-engine.git

```

step 3 :install the requirements

```
pip install -r requirements.txt

```

step 4 : run the app.py file

```
python app.py

```

# Input console 

![toxicity](screenshots/Capture1.png)

# Output console 
![toxicity](screenshots/Capture2.png)

## Heroku deployment

[Launch app](https://tamilspotify.herokuapp.com/)
