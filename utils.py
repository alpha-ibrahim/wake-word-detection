from gtts import gTTS
def generate_voice(text, file_name, lang='en'):
    """
    A function that generate a voice saying the text that is passed as input

        Parameters
        ----------
        text : str
            The text that will be spelled

        file_name : the file name of the resulting mp3 file
            
        lang : str
            The language in which the text will be spelled
    """

  
    myobj = gTTS(text=text, lang=lang, slow=False)
    
    # Saving the converted audio in a mp3 file named welcome 
    myobj.save(f"{name}.mp3")
