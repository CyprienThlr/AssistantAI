import os
import azure.cognitiveservices.speech as speechsdk

# API keys & region service
speech_key = "api_key"
service_region = "region"

# Setting up the text-to-speech service
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Voice selection (optional) : choose an available Neural TTS voice
# Se https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support for more voice option
speech_config.speech_synthesis_voice_name = "fr-FR-DeniseNeural"

# Initializing the speech synthesizer
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

# Text to convert to speech
text = "Hi, how can I help you today ?"

# Converting text to speech
result = speech_synthesizer.speak_text_async(text).get()

# Verifying the success of the synthesis
if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Text-to-speech completed successfully.")
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print(f"error : {cancellation_details.reason}")
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print(f"error : {cancellation_details.error_details}")
