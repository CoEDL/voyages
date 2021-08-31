# Voyages 4 Automatic Speech Recognition

In the activity we will train Elpis, an Automatic Speech Recognition system, with a "toy corpus" containing very few utterances. The toy corpus is used by the Elpis dev team when working on the software, and in introduction workshops. The small corpus is used to reduce data preparation and training times. 

This activity requires "Docker" to be installed on your computer, which enables Elpis to be run on your computer. See the notes [here about installing Docker](https://elpis.readthedocs.io/en/latest/wiki/install-elpis-docker.html). 

With Docker running, follow the [workshop steps](https://elpis.readthedocs.io/en/latest/wiki/elpis-workshop.html).


Now, repeat the activity with [TIMIT ASR dataset](https://huggingface.co/datasets/timit_asr). This is a dataset that is commonly used in developing and testing speech recognition technologies.

Download training data (choose the one most likely to match your voice pattern).
Women: https://bit.ly/3kZHUNf
Men: https://bit.ly/2Q6vyVw

Prepare data by making a letter-to-sound file
> https://cmusphinx.github.io/wiki/tutorialdict/
- Make a list of unique characters in the lexicon
- Assign a pronunciation symbol (let's use SAMPA)
- Review the pronunciation lexicon when it is created. Could it be corrected? 


Train Elpis using the dataset you downloaded, making a unigram model. Keep a record of the WER results.

Train Elpis again, this time with a trigram model. Keep a copy of the WER results.

Use Elpis to get an ASR transcription of your student number audio, using either the unigram or trigram model. Record yourself reciting your student number in WAV format. We recommend using [Audacity](https://www.audacityteam.org/).

Download the transcription in text format and add a second line containing your student number.
