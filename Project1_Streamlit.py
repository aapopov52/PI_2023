import streamlit as st
import moviepy.editor as mp 
import os
from pytube import YouTube
from faster_whisper import WhisperModel
from youtube_transcript_api import YouTubeTranscriptApi

#@st.cache(allow_output_mutation=True)
def load_model():
    return WhisperModel("large-v2")


st.title('Выделяем текст из видео')
model = load_model()

text = st.text_area("Введите Ссылку на страницу в Youtube:")
result = st.button('Выделить текст')
if result:
	#Загружаем файл
	#yt = YouTube('https://www.youtube.com/watch?v=qftVIw5wSbE&t=44s')
	yt = YouTube('https://www.youtube.com/watch?v=7x4eS95mMDE')


	#Указываем интересующий нас код языка (субтитры на котором нас интересуют)
	first_languarge_kod = 'ru'
	bFind = False
	# Информация о субтитрах
	transcript_list = YouTubeTranscriptApi.list_transcripts(yt.video_id)
	# Поиск нужного языка среди субтитров
	for transcript in transcript_list:
		if transcript.language_code == first_languarge_kod:
			Text_sub = transcript.fetch()
			bFind = True # Проставляем метку – язык найден
			
	# Поиск нужного языка среди переводов к субтитрам
	if not bFind:
		for transcript in transcript_list:
			if transcript.is_translatable == True:
				for tr_l in transcript.translation_languages:
					if tr_l['language_code'] == first_languarge_kod:
						Text_sub = transcript.translate(first_languarge_kod).fetch()
						bFind = True # Проставляем метку – язык найден
	# Если нашли нужный язык – распаковываем информацию о нём
	if bFind:
		sText = ''
		for s1 in Text_sub:
			sText += s1['text'] + '\n'
	
		st.write(sText)

	# Потом можно будет в интерефейсе добавить галочку (выполнить распознавание из звуковой дорожки)
	if sText == '':
		# нас интресует толтко аудио - его и грузим
		fileName = yt.streams.filter(type = "audio").first().download()
	
		#print(fileName)
		# Если бы погузили видео, то обработали бы так
		#video = mp.VidoAudioFileClip(fileName) 
		#audio_file = video.audio # из видео можно было бы извлечь так. Но у на аудио, поэтом 
		
		
		# Но у нас сразу же аудио - его обработать проще
		audio_file = mp.AudioFileClip(fileName) 
		audio_file.write_audiofile("vrem.wav") 
		os.remove(fileName)
		model = WhisperModel("large-v2")
	
		segments, info = model.transcribe("vrem.wav")
		for segment in segments:
		    st.write("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
		os.remove("vrem.wav")      
        


