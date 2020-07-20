from django.shortcuts import render
from datetime import datetime
from django.forms.models import model_to_dict
# Create your views here.
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BaseAuthentication
from rest_framework.views import APIView
from .serializers import TaskCreateSerializer, TableFieldsSerializer, FilterFieldSerializer

from .extra_tool.DbTool import conn_mysql, conn_close

from .models import TaskMsg, SeleTable
from .tasks import op_task1


class TaskCreateViewSet(mixins.CreateModelMixin,mixins.ListModelMixin, viewsets.GenericViewSet):  #添加个人用户返回个人信息

    """
    连接数据库接口
    """
    # queryset = TaskMsg.objects.all()
    serializer_class = TaskCreateSerializer
    # authentication_classes = (SessionAuthentication, BaseAuthentication)
    def get_queryset(self):
        # print(type(self.request.user.username))
        return TaskMsg.objects.filter(username=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        if serializer.validated_data['host']:
            handler, cursor = conn_mysql(serializer.validated_data)

            SQL = 'show tables;'
            cursor.execute(SQL)
            list_table = []
            for table in cursor.fetchall():
                list_table.append(table[0])
            conn_close(handler, cursor)
        self.perform_create(serializer)
        data = serializer.data
        data['列表信息']= list_table
        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)



class TablefieldsViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    '''
    post选择归档目标表
    '''

    serializer_class = TableFieldsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        meg = TaskMsg.objects.filter(pk=serializer.validated_data['taskid'])
        handler, cursor = conn_mysql(model_to_dict(meg[0]))
        SQL = 'desc {TableName};'.format(TableName=serializer.validated_data['seletable'])
        cursor.execute(SQL)
        list_table = []
        for table in cursor.fetchall():
            list_table.append(table[0])
        conn_close(handler, cursor)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = serializer.data
        data['字段列表'] = list_table
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


def on_raw_message(body):
    print(body)

class SeleFieldFilterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    '''
    post归档字段及归档规则
    '''

    serializer_class = FilterFieldSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # 已经import date time
        # result = op_task1.apply_async(args=serializer)
        validated_data = {}
        for i in serializer.validated_data:
            if i == 'username':
                validated_data[i] = model_to_dict(serializer.validated_data['username'])['username']
            else:
                validated_data[i] = serializer.validated_data[i]
        # validated_data = serializer.validated_data
        # validated_data['username'] = model_to_dict(serializer.validated_data['username'])['username']
        meg = model_to_dict(TaskMsg.objects.filter(id=validated_data['taskid'])[0])
        result = op_task1.delay(validated_data, meg)
        self.perform_create(serializer)

        data = {'操作结果': '任务开启成功',
                '任务id': '{0}'.format(result.id),
                '任务结果': result.get(on_message=on_raw_message, propagate=False),
                '任务状态': result.ready(),
                }

        headers = self.get_success_headers(serializer.data)
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)

    # def get_serializer_class(self):
    #     if self.request.data['']:
    #         pass


