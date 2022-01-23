class BaseManager:
    
    def __init__(self, model, serial, list_serial, save_serial):
        self._object = model.objects
        self._serial = serial
        self._list_serial = list_serial
        self._save_serial = save_serial        

    def read_one(self, obj_id):
        obj = self._object.get(id=obj_id)
        return self._serial(obj).data

    def list(self):
        obj_list = self._object.all()
        return self._list_serial(obj_list, many=True).data

    def create(self, obj_list):
        created_ids = []

        for obj_one in obj_list:
            created_id = self.create_one(obj_one)
            created_ids.append(created_id)

        return created_ids

    def create_one(self, obj_one):
        serializer = self._save_serial(data=obj_one)
        serializer.is_valid(raise_exception=True)
        result = serializer.save()
        return result.id
        