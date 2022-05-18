from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ResuméForm
from .models import Resumé


def textes_resumés(request):
    import os
    import subprocess

    # Save PATH
    source = "Path where the file is uploaded"

    # GCS_URL
    GCS_BASE = "gs://Bucket name/"

    # Save results
    speech_result = ""

    if request.method == 'POST':
        # Google Storage environment preparation
        from google.cloud import storage
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'json PATH'
        client = storage.Client()
        bucket = client.get_bucket('Google Storage bucket name')

        # Save upload file
        form = ResuméForm(request.POST, request.FILES)
        form.save()

        # Get the uploaded file name
        # Separate file name and extension(ext->extension(.py))
        transcribe_file = request.FILES['document'].name
        name, ext = os.path.splitext(transcribe_file)

        if ext == ".wav":
            # Upload to Google Storage
            blob = bucket.blob(transcribe_file)
            blob.upload_from_filename(filename=source + transcribe_file)

            # Get play time
            from pydub import AudioSegment
            sound = AudioSegment.from_file(source + transcribe_file)
            length = sound.duration_seconds
            length += 1

            # Delete working files
            cmd = 'rm -f ' + source + transcribe_file
            subprocess.call(cmd, shell=True)

            # Transcription
            from google.cloud import speech

            client = speech.SpeechClient()

            gcs_uri = GCS_BASE + transcribe_file

            audio = speech.RecognitionAudio(uri=gcs_uri)
            config = speech.RecognitionConfig(
                encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
                # sample_rate_hertz=16000,
                language_code="ja_JP",
                enable_automatic_punctuation=True,
            )

            operation = client.long_running_recognize(config=config, audio=audio)

            response = operation.result(timeout=round(length))

            for result in response.results:
                speech_result += result.alternatives[0].transcript

            # Google Storage file deletion
            blob.delete()

        else:
            # File conversion process
            f_input = source + transcribe_file
            f_output = source + name + ".wav"
            upload_file_name = name + ".wav"
            cmd = 'ffmpeg -i ' + f_input + ' -ar 16000 -ac 1 ' + f_output
            subprocess.call(cmd, shell=True)

            # Upload to Google Storage
            blob = bucket.blob(upload_file_name)
            blob.upload_from_filename(filename=f_output)

            # Get play time
            from pydub import AudioSegment
            sound = AudioSegment.from_file(source + transcribe_file)
            length = sound.duration_seconds
            length += 1

            # Delete working files
            cmd = 'rm -f ' + f_input + ' ' + f_output
            subprocess.call(cmd, shell=True)

            # Transcription
            from google.cloud import speech

            client = speech.SpeechClient()

            gcs_uri = GCS_BASE + upload_file_name

            audio = speech.RecognitionAudio(uri=gcs_uri)
            config = speech.RecognitionConfig(
                encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
                # sample_rate_hertz=16000,
                language_code="ja_JP",
            )

            operation = client.long_running_recognize(config=config, audio=audio)

            response = operation.result(timeout=round(length))

            for result in response.results:
                speech_result += result.alternatives[0].transcript

            # Google Storage file deletion
            blob.delete()
    else:
        form = ResuméForm()
    return render(request, 'resumé/texte_resumé.html', {
        'form': form,
        'transcribe_result': speech_result
    })


