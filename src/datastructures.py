
from random import randint


class FamilyStructure:
    def __init__(self, last_name): 
        self.last_name = last_name
        self._next_id = 1
        self._members = [ ]

        
    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id  


    def add_member(self, member):
        new_member = {
            "id": self._generate_id(),
            "last_name": self.last_name,
            "age": member["age"],
            "lucky_numbers": member["lucky_numbers"]
        }
        self._members.append(new_member)


    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return {"message": "Member deleated"}
        return {"message": "ID doesn't exist"}

    def get_member(self, id):
        for member in self._members:
            if member["id"] == int(id):
                return member            
        return {"message": "Member not found"}
        
    def get_all_members(self):
        return self._members
