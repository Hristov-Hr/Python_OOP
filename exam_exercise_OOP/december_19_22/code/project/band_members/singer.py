from project.band_members.musician import Musician


class Singer(Musician):

    MUSICIAN_TYPE = "Singer"

    def is_valid_skill(self, skill):

        return skill in ["sing high pitch notes", "sing low pitch notes"]
