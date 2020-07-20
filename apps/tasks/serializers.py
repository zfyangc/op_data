from abc import ABC

from rest_framework import serializers
from .models import TaskMsg, SeleTable, SeleField


class TaskCreateSerializer(serializers.ModelSerializer):
    port = serializers.IntegerField(required=True, label="端口",error_messages={
                                     "required": "请输入端口" },)
    username = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )
    add_time = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        '''
        post过来参数创建任务连接数据库信息
        :param validated_data:
        :return:
        '''

        return TaskMsg.objects.create(**validated_data)

    class Meta:
        model = TaskMsg
        fields = "__all__"


#
class TableFieldsSerializer(serializers.ModelSerializer):
    username = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = SeleTable
        fields = "__all__"


class FilterFieldSerializer(serializers.ModelSerializer):
    rangetop = serializers.DateTimeField(label="终止时间范围")
    rangelow = serializers.DateTimeField(label="起始时间范围")
    username = serializers.HiddenField(
        default=serializers.CurrentUserDefault(), write_only=True,)
    selefield = serializers.CharField(required=True, label="归档目标字段", error_messages={
                                     "required": "请输入端口"})

    class Meta:
        model = SeleField
        fields = "__all__"


# class GoodsSerializer(serializers.Serializer):
#     name = serializers.CharField(required=True,max_length=100)
#     click_num = serializers.IntegerField(default=0)
#     goods_front_Image = serializers.ImageField()




