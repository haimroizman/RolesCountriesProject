import json
from typing import Dict, Set
from data_models import ApalulaDataSet, Citizen, Role

class VisitCheck:
    def __init__(self):
        self.apalula_data_set: ApalulaDataSet = None
        self.role_dic: Dict[str, Role] = {}
        self.citizen_dic: Dict[str, Citizen] = {}

    def load_dataset(self, dataset_file: str) -> None:
        with open(dataset_file, 'r') as f:
            data = json.load(f)

        citizens = [Citizen(**c) for c in data['citizens']]
        roles = [Role(**r) for r in data['roles']]
        self.apalula_data_set = ApalulaDataSet(citizens, roles)

        self.role_dic = {role.title: role for role in self.apalula_data_set.roles}
        self.citizen_dic = {citizen.name: citizen for citizen in self.apalula_data_set.citizens}

    def can_visit(self, citizen_name: str, place: str) -> bool:
        if not self.apalula_data_set:
            raise ValueError("Dataset not loaded. Call load_dataset() first.")

        citizen = self.citizen_dic.get(citizen_name)
        if not citizen:
            return False

        allowed_places = set(citizen.allowed_places)
        for role in citizen.roles:
            allowed_places.update(self._get_allowed_places_for_sub_roles(role))

        return place in allowed_places

    def _get_allowed_places_for_sub_roles(self, role_title: str) -> Set[str]:
        allowed_places = set()
        visited_roles = set()

        def dfs(current_role: str):
            if current_role in visited_roles:
                return
            visited_roles.add(current_role)

            role = self.role_dic.get(current_role)
            if role:
                allowed_places.update(role.allowed_places)
                for sub_role in role.sub_roles:
                    dfs(sub_role)

        dfs(role_title)
        return allowed_places