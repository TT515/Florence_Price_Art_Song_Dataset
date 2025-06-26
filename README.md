# Florence Price Art Song Dataset

**This repository is a companion to the ISMIR 2025 paper**  
**“The Florence Price Art Song Dataset and Piano Accompaniment Generator”**

- 📄 [Paper (arXiv)](link/soon)  
- 🎹 [Piano Accompaniment Generator (Colab)](https://colab.research.google.com/drive/1MRuk5y70M_hUjhOkD9KphFgJIgR1C9H-)  
- 🎧 [Listening Examples (GitHub)](https://github.com/m-malandro/Florence-Price-listening-examples)  

---

## Overview

This repository provides access to **112 songs** by composer **Florence B. Price**, manually transcribed into MuseScore from manuscript sources. The transcriptions are sourced from:

- University of Arkansas – David W. Mullins Library  
- University of Pennsylvania – Kislak Center for Special Collections, Rare Books, and Manuscripts

---

## Dataset Structure

### 📁 `price_songs_main/` (107 complete songs)
Organized into three subfolders:

1. **Original Compositions**: 95 songs composed by Price  
2. **Arrangements**: 11 songs arranged by Price, primarily African American folk songs
3. **Thou Art**: This song composed by Price for voice, piano, and cello is separated from the songs composed for voice and piano. We only include the MuseScore file for this song.

Each song folder includes:

- MuseScore file (`.mscz`)  
- MIDI and MusicXML files  
- PDF of the digitized score  
- Lyrics in plain text  
- Two "onsets" files denoting bar-wise section boundaries from two annotators  
- A `metadata` file including:
  - Tempo  
  - Lyricist  
  - Subjective mood annotations:  
    - Happy/Sad  
    - Descriptive adjective  
    - Musical style

#### Audio Files

We recognize the need for audio files of the songs for some researchers. Therefore, we include `audio_script.py`, a script that can render audio for each of the Musescore files in the repository. Please note that rendering the audio for all 112 songs takes a significant amount of time (~1 hour).

> 🔁 **For songs with repeats**, four "onsets" files are included: two based on the **written** bar values, and two based on the **performed** values. See list of songs with repeats below.

### 📁 `price_songs_incomplete/` (6 songs)
These are either incomplete or not scored for solo voice and piano. For each, we include only the `.mscz` file.

### 📝 Edited Scores
Three scores were originally typeset by **Owain Evans** under a CC0 license on MuseScore:

- *Travels End*  
- *Forever*  
- *Fantasy in Purple*

All remaining scores were typeset by the first author.

---

## Notation Details

In the dataset, **oboe** is used as a substitute for the voice part.  
This is consistent with practices in datasets like the [OpenScore Lieder Corpus](https://github.com/MarkGotham/Lieder).  

---

## Songs with Repeats

- City Called Heaven  
- Don’t Blame It on the Moonlight  
- Don’t You Tell Me No  
- Every Dream  
- Peter Go Ring Dem Bells  
- The Superstitious Ghost *(DS notation)*  
- When I Fall On My Knees  
- Why Forget  
- Death’s Gwineter Lay His Cold Icy Hand On Me  
- My Neighbor *(DS notation)*  
- Save Me Lord, Save Me  
- Let’s Build a Little Love Nest  

---

## Copyright Status

### 🟢 **Public Domain Works**
- Published before 1930  
- Unpublished works (entered public domain on Jan 1, 2024 — 70 years after Price's death in 1953)

### 🔴 **Omitted Due to Copyright Risk**
Although we couldn’t confirm renewals, to avoid legal risk, we exclude the following 17 songs from the dataset and training set:

#### **Original Compositions**  
| Title | Year |
|-------|------|
| An April Day | 1949 |
| Desire | 1959 |
| God Gives Me You | 1946 |
| Hitch Up Your Belts, Boys | 1942 |
| In Back o’ the Clouds | 1930 |
| Let’s Build a Little Love Nest | 1930 |
| Night *(Louise Wallace)* | 1973 |
| Out of the South Blew a Soft Sweet Wind | 1973 |
| Songs to the Dark Virgin | 1968 |
| Sunset | 1938 |
| The Moon Bridge | 1957 |
| To My Little Son | 1959 |

#### **Arrangements**  
| Title | Year |
|-------|------|
| I Am Bound for the Kingdom | 1949 |
| I’m Workin’ on My Buildin’ | 1949 |
| My Soul’s Been Anchored in the Lord | 1937 |
| Trouble Done Come My Way | 1964 |
| Weary Traveler | 1959 |

> ℹ️ Reference for US Public Domain Rules: [Cornell Copyright Guide](https://guides.library.cornell.edu/copyright/publicdomain)

---

## License

These scores are released under Creative Commons Zero (CC0). See LICENSE.txt.

All scores not under copyright are provided for academic use.  
Please cite the ISMIR 2025 paper if using this dataset.

---

## Call for Contributions

We welcome contributions to the Florence Price Art Song Dataset! We acknowledge limitations to the annotations due to the lack of annotators. If you wish to help improve the dataset, please contact the authors of the ISMIR 2025 paper.
