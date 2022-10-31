from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        for category in self.categories:
            if category.id == category.id:
                return
        self.categories.append(category)

    def add_topic(self, topic: Topic):
        for topic in self.topics:
            if topic.id == topic.id:
                return
        self.topics.append(topic)

    def add_document(self, document: Document):
        for document in self.documents:
            if document.id == document.id:
                return
        self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = self.__get_category(category_id)
        category.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.__get_topic(topic_id)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        document = self.__get_document(document_id)
        document.edit(new_file_name)

    def delete_category(self, category_id):
        category = self.__get_category(category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.__get_topic(topic_id)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.__get_document(document_id)
        self.documents.remove(document)

    def get_document(self, document_id):
        return self.__get_document(document_id)

    def __repr__(self):
        return '\n'.join(repr(x) for x in self.documents)

    def __get_category(self, category_id):
        for category in self.categories:
            if category.id == category_id:
                return category

    def __get_topic(self, topic_id):
        for topic in self.topics:
            if topic.id == topic_id:
                return topic

    def __get_document(self, document_id):
        for document in self.documents:
            if document.id == document_id:
                return document


