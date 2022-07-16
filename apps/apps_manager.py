from django.core.paginator import Paginator


class BaseManager:
    
    def __init__(self, model, serial, list_serial, save_serial):
        self._object = model.objects
        self._serial = serial
        self._list_serial = list_serial
        self._save_serial = save_serial        

    def read(self, obj_id):
        obj = self._object.get(id=obj_id)
        return self._serial(obj).data

    def list(self, page, size):
        obj_list = self._object.all()
        paging = Paginator(obj_list, size)
        posts = paging.get_page(page).object_list
        total_pages = paging.num_pages
        total_count = paging.count
        return self._list_serial(posts, many=True).data, total_count, total_pages

    def create(self, obj_list):
        created_ids = []

        for obj_one in obj_list:
            created_id = self.create_one(obj_one)
            created_ids.append(created_id)

        return created_ids

    def create_one(self, obj_one):
        serializer = self._save_serial(data=obj_one)
        result = self._save(serializer)
        return result.id

    def update(self, obj_id, obj_one):
        obj = self._object.get(id=obj_id)
        serializer = self._save_serial(obj, data=obj_one, partial=True)
        updated = self._save(serializer)
        return self._serial(updated).data

    def _save(self, serializer):
        serializer.is_valid(raise_exception=True)
        return serializer.save()

    def delete(self, obj_id):
        obj = self._object.get(id=obj_id)
        obj.delete()
