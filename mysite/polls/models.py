from neo4django.db import models

class Poll(models.NodeModel):
    question = models.StringProperty(max_length=200)
    pub_date = models.DateTimeProperty('date published')

class Choice(models.NodeModel):
    poll = models.Relationship('Poll',
                               rel_type='offers',
                               single=True,
                               related_name='choices')
    choice = models.StringProperty(max_length=200)
    votes = models.IntegerProperty()
