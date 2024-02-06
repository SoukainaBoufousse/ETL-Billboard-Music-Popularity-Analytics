from airflow.plugins_manager import AirflowPlugin
from flask import Blueprint, request
from flask_appbuilder import expose, BaseView as AppBuilderBaseView
from my_task import MyTask
from wtforms import Form, StringField
from airflow.www.app import csrf
#from wtforms.fields.html5 import DateTimeField
import json
import os
bp = Blueprint(
               "test_plugin",
               __name__,
               template_folder="templates", 
               static_folder="static",
               static_url_path="/static/test_plugin",
               )
class FilterForm(Form):
    chromastft= StringField('chromastft')
    rms= StringField('rms')
    spectral_centroid= StringField('spectral_centroid')
    spectral_bandwidth= StringField('spectral_bandwidth')
    spectral_rolloff=StringField('spectral_rolloff')
    zero_crossing_rate=StringField('zero_crossing_rate')
    mfcc_1=StringField('mfcc_1')
    mfcc_2=StringField('mfcc_2')
    mfcc_3=StringField('mfcc_3')
    mfcc_4=StringField('mfcc_4')
    mfcc_5=StringField('mfcc_5')
    mfcc_6=StringField('mfcc_6')
    mfcc_7=StringField('mfcc_7')
    mfcc_8=StringField('mfcc_8')
    mfcc_9=StringField('mfcc_9')
    mfcc_10=StringField('mfcc_10')
    mfcc_11=StringField('mfcc_11')
    mfcc_12=StringField('mfcc_12')
    mfcc_13=StringField('mfcc_13')
    mfcc_14=StringField('mfcc_14')
    mfcc_15=StringField('mfcc_15')
    mfcc_16=StringField('mfcc_16')
    mfcc_17=StringField('mfcc_17')
    mfcc_18=StringField('mfcc_18')
    mfcc_19=StringField('mfcc_19')
    mfcc_20=StringField('mfcc_20')



class TestAppBuilderBaseView(AppBuilderBaseView):
    default_view = "test"
    @expose("/", methods=['GET', 'POST'])
    #this method gets the view as localhost:/testappbuilderbaseview/
    @csrf.exempt
    def test(self):
        form = FilterForm(request.form)
        if request.method == 'POST' and form.validate():
            #Here we are calling our usecase functions
            my_task_output = MyTask(
                   form.chromastft.data, 
                   form.rms.data,
                   form.spectral_centroid.data, 
                   form.spectral_bandwidth.data,
                   form.spectral_rolloff.data,
                   form.zero_crossing_rate.data,
                   form.mfcc_1.data,
                   form.mfcc_2.data,
                   form.mfcc_3.data,
                   form.mfcc_4.data,
                   form.mfcc_5.data,
                   form.mfcc_6.data,
                   form.mfcc_7.data,
                   form.mfcc_8.data,
                   form.mfcc_9.data,
                   form.mfcc_10.data,
                   form.mfcc_11.data,
                   form.mfcc_12.data,
                   form.mfcc_13.data,
                   form.mfcc_14.data,
                   form.mfcc_15.data,
                   form.mfcc_16.data,
                   form.mfcc_17.data,
                   form.mfcc_18.data,
                   form.mfcc_19.data,
                   form.mfcc_20.data,
            )
            df = my_task_output.my_function()
            return df
        return self.render_template("test.jinja", form = form)

v_appbuilder_view = TestAppBuilderBaseView()
v_appbuilder_package = {
    "name": "Test View",
    "category": "Test Plugin",
    "view": v_appbuilder_view
}
class AirflowTestPlugin(AirflowPlugin):
    name = "test_plugin"
    operators = []
    flask_blueprints = [bp]
    hooks = []
    executors = []
    admin_views = []
    appbuilder_views = [v_appbuilder_package]