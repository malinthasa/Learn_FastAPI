from typing import Optional, List
from pydantic import BaseModel

from models.User import Gender, Roles


class UpdateUser(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    middle_name: Optional[str]
    gender: Optional[Gender]
    roles: Optional[List[Roles]]
