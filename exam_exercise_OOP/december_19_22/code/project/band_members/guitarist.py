from project.band_members.musician import Musician


class Guitarist(Musician):

    MUSICIAN_TYPE = "Guitarist"

    def is_valid_skill(self, skill):
        return skill in ["play metal", "play rock", "play jazz"]
