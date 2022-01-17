from rest_framework import viewsets
# from django.http import JsonResponse


from .models import ImgModel, FormModel, PostModel, CommentsModel
from .api.serializers import ImgSerializer, FormModelSerializer, PostSerializer, CommentsSerializer


class ImgView(viewsets.ModelViewSet):
    queryset = ImgModel.objects.all()
    serializer_class = ImgSerializer
    lookup_field = ('id')


class FormView(viewsets.ModelViewSet):
    queryset = FormModel.objects.all()
    serializer_class = FormModelSerializer
    lookup_field = ('id')


class PostView(viewsets.ModelViewSet):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer
    lookup_field = ('slug')


class CommentsView(viewsets.ModelViewSet):
    queryset = CommentsModel.objects.all()
    serializer_class = CommentsSerializer
    lookup_field = ('slug')


# def My_test(request):
#     if request.method == 'POST':
    #     print('request::', request)
    #     print('request content_type::', request.content_type)
    #     # print('body::')
    #     # print(request.body)
    #     print('POST::')
    #     print(request.POST)
    #     print('FILE::')
    #     print(request.FILES)
    #     print('FILE keys::')
    #     print(request.FILES.keys())
    #     print("FILE['file']::")
    #     print(request.FILES['file'])
    # else:
    #     print('hello')

    # return JsonResponse({'MSG': 'ok'})
