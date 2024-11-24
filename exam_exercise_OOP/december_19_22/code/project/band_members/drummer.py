from project.band_members.musician import Musician


class Drummer(Musician):
    MUSICIAN_TYPE = "Drummer"

    def is_valid_skill(self, skill):
        return skill in ["play the drums with drumsticks", "play the drums with drum brushes", "read sheet music"]
