# views.py
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import ChatMessage
from .serializers import ChatMessageSerializer

from groq import Groq
from django.conf import settings

class ChatCompletionView(APIView):
    @method_decorator(login_required)
    def post(self, request):
        serializer = ChatMessageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)

            client = Groq(api_key=settings.GROQ_API_KEY)
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": serializer.validated_data['content'],
                    }
                ],
                model="mixtral-8x7b-32768",
            )

            ai_message = chat_completion.choices[0].message.content
            ai_serializer = ChatMessageSerializer(data={'role': 'MedicalBot', 'content': ai_message})
            if ai_serializer.is_valid():
                ai_serializer.save(user=request.user)

            return Response(ai_serializer.data, status=201)

        return Response(serializer.errors, status=400)

@login_required
def chat_view(request):
    messages = ChatMessage.objects.filter(user=request.user)
    return render(request, 'groqchat.html', {'messages': messages})