from abstract_storage import AbstractStorage
from exceptions import UnknownStorageError, InvalidRequestError


class Request:
    def __init__(self, request, storages: dict[str, AbstractStorage]):
        split_req = request.lower().split()
        if len(split_req) != 7 or not split_req[1].isdigit():
            raise InvalidRequestError

        self.amount = int(split_req[1])
        self.product = split_req[2]
        self.destination = split_req[6]
        self.departure = split_req[4]

        if self.destination not in storages or self.departure not in storages:
            raise UnknownStorageError
