from dataclasses import asdict, dataclass
import uuid


@dataclass
class Room:
    code: uuid.UUID
    size: int
    price: int
    longitude: float
    latitude: float


    @classmethod
    def from_dict(cls, dictionary: dict):
        return cls(**dictionary)
    
    
    def to_dict(self):
        return asdict(self)
    
    def __repr__(self):
        return f"""
            Room(
                code: {self.code}, 
                size: {self.size}, 
                price: {self.price}, 
                longitude: {self.longitude}, 
                latitude: {self.latitude}
            )
        """