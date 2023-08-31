import torch
import torchaudio
from seamless_communication.models.inference import Translator

def text2text():
    text = "hello,world"
    # Initialize a Translator object with a multitask model, vocoder on the GPU.
    # cpu torch.float32
    # gpu torch.float16
    translator = Translator("seamlessM4T_medium", "vocoder_36langs", torch.device("cpu"), torch.float32)
    translated_text, _, _ = translator.predict(text ,"t2tt", "cmn", src_lang="eng")
    print(translated_text)