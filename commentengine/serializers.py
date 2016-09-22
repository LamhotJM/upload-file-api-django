from commentengine.models import MasterComment
from rest_framework import serializers


class MasterCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterComment
        fields = ("commentid", "userid", "loanid", "comment", "file_upload", "context_id", "context_scope", "status",
                  "createdby", "createdfrom", "createddate", "modifiedby", "modifiedfrom", "modifieddate",)


class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        file_upload = serializers.ImageField(max_length=None, use_url=True)