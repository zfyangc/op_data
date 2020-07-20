from datetime import datetime
import time
from .extra_tool.DbTool import conn_mysql, conn_close
from django.forms.models import model_to_dict
from .models import TaskMsg, SeleTable
from op_data.celerys import app


@app.task(bind=True)
def op_task1(self, validated_data, meg):
    time.sleep(3)
    self.update_state(state="PROGRESS", meta={'progress': 10})
    time.sleep(3)
    self.update_state(state="PROGRESS", meta={'progress': 20})
    time.sleep(3)
    self.update_state(state="PROGRESS", meta={'progress': 40})
    handler, cursor = conn_mysql(meg)
    time.sleep(3)
    self.update_state(state="PROGRESS", meta={'progress': 40})
    # rangetop = datetime.strftime(validated_data['rangetop'], '%Y-%m-%d %H:%M')
    # rangelow = datetime.strftime(validated_data['rangelow'], '%Y-%m-%d %H:%M')
    SQL = 'select * from {0} where {1} >= {2} and {3} <= {4};'.format(
        model_to_dict(SeleTable.objects.filter(taskid = validated_data['taskid']).order_by("-id")[0])["seletable"],
        "add_time", '"{0}"'.format(validated_data['rangelow'].strftime("%Y-%m-%d %H:%M:%S"),),
        "add_time", '"{0}"'.format(validated_data['rangetop'].strftime("%Y-%m-%d %H:%M:%S"),))
    time.sleep(3)
    self.update_state(state="PROGRESS", meta={'progress': 50})
    cursor.execute(SQL)
    list_table = []
    for table in cursor._rows:
        list_table.append(table)
    time.sleep(3)
    self.update_state(state="PROGRESS", meta={'progress': 60})
    conn_close(handler, cursor)
    time.sleep(3)
    self.update_state(state="PROGRESS", meta={'progress': 70})
    print(list_table)
    time.sleep(3)
    self.update_state(state="PROGRESS", meta={'progress': 80})
    time.sleep(3)
    self.update_state(state="PROGRESS", meta={'progress': 90})
    return list_table

