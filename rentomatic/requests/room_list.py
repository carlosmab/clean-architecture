from abc import ABC, abstractmethod
from collections.abc import Mapping

class RoomListRequest(ABC):
    filters: dict | None = None
    errors: list[dict] = []
    
    @abstractmethod
    def has_errors(self) -> bool:
        pass
 
    
class RoomListValidRequest(RoomListRequest):
    
    def __init__(self, filters: dict | None = None) -> None:
        self.filters = filters
    
    def has_errors(self) -> bool:
        return False

    def __bool__(self) -> bool:
        return True

class RoomListInvalidRequest(RoomListRequest):
    
    def __init__(self, filters: dict | None = None) -> None:
        self.filters = filters
        self.errors = []
        self.errors.append({"parameter": "filters"})
        
    def add_error(self, parameter, message):
        """
        Adds an error message to the list of errors.
        Parameters:
            parameter (str): The parameter that caused the error.
            message (str): The error message.
        Returns:
            None
        """
        self.errors.append({"parameter": parameter, "message": message})
    
    def __bool__(self) -> bool:
        return False

    def has_errors(self) -> bool:
        return True


        
def build_room_list_request(filters: dict | None = None) -> RoomListRequest:
    accepted_filters = ["code__eq", "price__eq", "price__lt", "price__gt"]
    
    if filters is not None:
        invalid_request = RoomListInvalidRequest()
        
        if not isinstance(filters, Mapping):
            invalid_request.add_error("filters", "Is not an iterable")
            return invalid_request
        
        for key, value in filters.items():
            if key not in accepted_filters:
                invalid_request.add_error("filters", f"Invalid filter key: {key}")
        
        if invalid_request.has_errors():
            return invalid_request
    
    return RoomListValidRequest(filters)



    

    