# Audio Transcription
Transcription of audio files, including preprocessing of ground truth text, using Azure Cognitive Services Custom Speech Service

Preprocessing script [preprocess.py](src/preprocess.py) - standardizes human-labeled ground truth text to prepare it to be used in the [Cognitive Services Custom Speech portal](http://speech.microsoft.com):
* lowercases text
* removes punctuation except apostrophes (')
* truncates 4 or more repeating characters (e.g. "aaaa" -> "aaa")
* truncates 4 or more repeating words (e.g. "yes yes yes yes" -> "yes yes yes"
* spells out numbers (e.g. "16" -> "sixteen")
* removes comments in brackets (e.g. "[laughs]")

