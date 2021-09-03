# Voyages 4 Speech Synthesis

This tutorial reinforces knowledge of speech synthesis and text-to-speech TTS systems, including manipulating audio files, using a basic concatenative synthesiser and using more advanced systems. The results of a variety of systems are reviewed to understand the difference between them.

## Audio processing with Audacity

1. Download and install Audacity. Choose the installer to suit your system from [https://www.fosshub.com/Audacity.html](https://www.fosshub.com/Audacity.html)

2. Make an audio recording of your student number (you can use one that you’ve recorded before). Save it as a WAV file. 

3. Pitch & duration
    1. Use the Effects > Change Pitch menu item to change the pitch.
    2. Listen to it, and save the file as _student_number_1.wav_
    3. Revert to the original recording.
    4. Try the Change Speed effect.
    5. Listen to it, and save the file as _student_number_2.wav_
    6. Revert to the original recording.
    7. Try the Change Tempo effect.
    8. Listen to it, and save the file as _student_number_3.wav_

4. Normalisation
    1. Download this folder of audio files. 
    2. Open each file in Audacity and compare the waveforms.  
    3. Open the `kicking-mule-very-quiet` audio file.
    4. [Normalise](https://manual.audacityteam.org/man/amplify_and_normalize.html) the levels.

5. Show and tell!


## Speech Synthesis systems

1. Concatenative TTS
    1. Open and copy the [Concatenative demo Colab](https://colab.research.google.com/drive/1958MzguphQEcyr_IQnGYVnZ5ubmHoWZK?usp=sharing)
    2. Run the first code cells to download the Python module.
    3. Type a sentence into the message variable.
    4. Run that cell to generate an audio file of the text.
    5. Preview the audio. 
    6. Comments??

2. DeepVoice3
    1. Open and copy the [DeepVoice demo Colab](https://colab.research.google.com/drive/1nfqx3sc98n1F0D5WSEDjH5Vy6mibOSVt?usp=sharing)
    2. Run the code cells to setup and install the program.
    3. Change the sentence.
    4. Generate speech.
    5. Describe the plots.
    6. More info: [Medium article](https://medium.com/a-paper-a-day-will-have-you-screaming-hurray/day-6-deep-voice-3-scaling-text-to-speech-with-convolutional-sequence-learning-16c3e8be4eda) | [Github](https://github.com/r9y9/deepvoice3_pytorch) | [Baidu](http://research.baidu.com/Blog/index-view?id=91)

3. Tacotron2
    1. Open and copy the [Tacotron2 demo Colab](https://colab.research.google.com/drive/1s0GMSj8kjI_GkG9PSkFztJ2tmC9PnjYA?usp=sharing)
    2. Run the code cells to setup and install the program.
    3. Change the sentence.
    4. Generate the speech.
    5. More info: [GoogleAI blog](https://ai.googleblog.com/2017/12/tacotron-2-generating-human-like-speech.html)

4. Voice cloning
    1. Open and copy the [RealTimeVoiceCloning demo Colab](https://colab.research.google.com/drive/1xvJCK_xMtubrY8CYDPW5CoUDOOJK0Pde?usp=sharing)
    2. Run the code cells to setup and install the program.
    3. Record yourself using the Colab (you may need to authorise the browser to record), read the [Harvard Sentences](http://www.cs.cmu.edu/afs/cs.cmu.edu/project/fgdata/OldFiles/Recorder.app/utterances/Type1/harvsents.txt) or [SUS](https://colab.research.google.com/drive/1wtV13ws3IxmyZ8bOadPJJBcLXiQMi9zH?usp=sharing) or [NIT](http://research.nii.ac.jp/src/en/NITECH-EN.html) sentences.
    4. Write a sentence and synthesise it with your voice-cloned system.
