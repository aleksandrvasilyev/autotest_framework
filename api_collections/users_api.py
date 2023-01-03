from my_framework.data_classes.user import User
from my_framework.utilities.api.base_api import BaseAPI


class UsersAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.__url = '/users'

    def get_user_by_id(self, user_id, headers=None):
        return self.get(f'{self.__url}/{user_id}', headers=headers)

    def create_user(self, body=None):
        user_data = User()
        if body is not None:
            user_data.update_dict(**body)
        response = self.post(self.__url, body=user_data.get_json())
        return response

    def delete_user_by_id(self, user_id, headers=None):
        return self.delete(f'{self.__url}/{user_id}', headers=headers)
