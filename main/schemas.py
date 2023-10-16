from ninja import Schema, ModelSchema
from datetime import date
from main.models import Note


class CategoryIn(Schema):
    title: str
    description: str
    authors: str


class CategoryOut(Schema):
    id: int
    title: str
    description: str
    authors: str
    created: date


class NoteIn(ModelSchema):
    class Config:
        model = Note
        model_fields = ['title', 'category_id']


class NoteUpd(ModelSchema):
    class Config:
        model = Note
        model_fields = ['id', 'completed']


class NoteOut(ModelSchema):
    class Config:
        model = Note
        model_fields = ['id', 'title', 'category_id', 'created', 'completed']