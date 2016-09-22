from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.parsers import MultiPartParser
from commentengine.serializers import MasterCommentSerializer
from commentengine.models import MasterComment
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import response, schemas, renderers
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404


@api_view()
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
@renderer_classes([renderers.CoreJSONRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='Comment Micro services')
    return response.Response(generator.get_schema(request=request))


class MasterCommentList(APIView):
    """
       A view that returns the count of active users in JSON.
    """
    parser_classes = (MultiPartParser,)

    def get(self, request, format=None):
        pageNum = int(request.GET.get('pn', 1))
        pageSize = int(request.GET.get('rpp', 10))
        begin = (int(pageNum) - 1) * pageSize
        end = begin + pageSize

        comments = MasterComment.objects.all().order_by('commentid')[begin:end]
        totalComments = MasterComment.objects.count()
        serializer = MasterCommentSerializer(comments, many=True)

        response = {'status': 'success',
                    'data': serializer.data,
                    'total': totalComments,
                    'cp': pageNum}
        return Response(response)

    def post(self, request, format=None):
        serializer = MasterCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MasterCommentDetail(APIView):
    """
    Retrieve, update or delete a comment instance.
    """
    parser_classes = (JSONParser,)

    def get_object(self, pk):
        try:
            return MasterComment.objects.get(pk=pk)
        except MasterComment.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        comment = self.get_object(pk)
        comment = MasterCommentSerializer(comment)
        response = {'status': 'success',
                    'data': comment.data}
        return Response(response)

    def put(self, request, pk, format=None):
        comment = self.get_object(pk)
        serializer = MasterCommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        comment = self.get_object(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
