from pydub import AudioSegment
import hashlib
import time
input_path = "C:\\Users\\vdocv\\PycharmProjects\\ArtGenerator\\audio_files\\Final-Songs\\"
output_path = "C:\\Users\\vdocv\\PycharmProjects\\ArtGenerator\\audio_output\\"

sound1 = AudioSegment.from_wav(f"{input_path}NFT-1.wav")
sound2 = AudioSegment.from_wav(f"{input_path}NFT-2.wav")

delimiter = "#"

description = "hi"

baseUri = "1234"

extra_metadata = {'external_url':'majesticmantisclub.com'}

def combine_audio_export(export_filename, *sounds):
    combined_sounds = ""
    for sound in range(len(sounds)-1):
        combined_sounds = sounds[sound].overlay(sounds[sound+1])
    combined_sounds.export(f"{output_path}{export_filename}.mp3", format="mp3")

def create_dna(*names):
    total_name = ""
    for param in names:
        total_name += param
    total_name = total_name.encode('utf8')
    encoded_name = hashlib.sha1(total_name)
    dna = encoded_name.hexdigest()
    print(dna)

def getRarityWeight(_str):
    nameWithoutExtension = _str.slice(0, -4)
    nameWithoutWeight = int((nameWithoutExtension.split(delimiter))[1])
    if (nameWithoutWeight) == None:
        nameWithoutWeight = 1
    return nameWithoutWeight




layers = {
    "Beginning", "Middle", "End", "Background", "Foreground"
}



#
# def addMetadata(_dna, _edition):
#     dateTime = int(time.time())
#     tempMetadata = {
#         'name': _edition,
#         'description': description,
#         'image': f'{baseUri}/{_edition}.png',
#         'dna': f'{_dna}',
#         'edition': _edition,
#         'date': dateTime,
#         extra_metadata,
#         'attributes': f"{attributesList}",
#         'compiler': 'Good Art Engine'}


# create_dna("hi", "how", "are", "you")
combine_audio_export("second_nft", sound1, sound2)