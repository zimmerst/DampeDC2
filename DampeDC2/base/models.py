from mongoengine import CASCADE
from mongoengine import Document, StringField, BooleanField, DateTimeField, FloatField
from datetime import datetime

origins = ("UNIGE","CNAF","BARI","PMO","OTHER")


class DataFile(Document):
    created_at = DateTimeField(default=datetime.now, required=True)
    lfn = StringField(required=True,max_length=2048,verbose_name="logical file name of file")
    md5 = StringField(required=True,max_length=512, verbose_name="md5 checksum string")
    ftype = StringField(required=True,max_length=20,verbose_name="type of file to be stored")
    ext = StringField(required=False,max_length=8,verbose_name="extension of file")
    origin = StringField(required=False,max_length=8,default="OTHER",verbose_name="original source", choices=origins)
    comment = StringField(required=False, max_length=64, verbose_name="any comment")
    is_ok = BooleanField(required_true=False, default=False, verbose_name="status is good")
    new = BooleanField(required_true=False, default=True, verbose_name="file is new")
    tstart = FloatField(verbose_name="start time (MET)",required=False,default=0.)
    tstop = FloatField(verbose_name="stop  time (MET)",required=False,default=0.)
    meta = {
            'allow_inheritance': True,
            'indexes': ['-created_at','lfn','comment','tstart','tstop','origin']
    }
