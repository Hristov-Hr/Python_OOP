from project.artifacts.contemporary_artifact import ContemporaryArtifact
from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.collectors.museum import Museum
from project.collectors.private_collector import PrivateCollector


class AuctionHouseManagerApp:

    VALID_ARTIFACTS = {"RenaissanceArtifact": RenaissanceArtifact, "ContemporaryArtifact": ContemporaryArtifact}
    VALID_COLLECTORS = {"Museum": Museum, "PrivateCollector": PrivateCollector}
    SOLD_ARTIFACTS = 0

    def __init__(self):
        self.artifacts = []
        self.collectors = []

    def register_artifact(self, artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int):

        if artifact_type not in self.VALID_ARTIFACTS.keys():
            raise ValueError("Unknown artifact type!")

        artifact = [a for a in self.artifacts if a.name == artifact_name]

        if artifact:
            raise ValueError(f"{artifact_name} has been already registered!")

        self.artifacts.append(self.VALID_ARTIFACTS[artifact_type](artifact_name, artifact_price, artifact_space))
        return f"{artifact_name} is successfully added to the auction as {artifact_type}."

    def register_collector(self, collector_type: str, collector_name: str):

        if collector_type not in self.VALID_COLLECTORS.keys():
            raise ValueError("Unknown collector type!")

        collector = [c for c in self.collectors if c.name == collector_name]
        if collector:
            raise ValueError(f"{collector_name} has been already registered!")

        self.collectors.append(self.VALID_COLLECTORS[collector_type](collector_name))
        return f"{collector_name} is successfully registered as a {collector_type}."

    def perform_purchase(self, collector_name: str, artifact_name: str):
        try:
            collector = next(filter(lambda x: x.name == collector_name, self.collectors))

        except StopIteration:
            raise ValueError(f"Collector {collector_name} is not registered to the auction!")

        try:
            artifact = next(filter(lambda x: x.name == artifact_name, self.artifacts))

        except StopIteration:
            raise ValueError(f"Artifact {artifact_name} is not registered to the auction!")

        if collector.can_purchase(artifact.price, artifact.space_required):
            self.artifacts.remove(artifact)
            collector.purchased_artifacts.append(artifact)
            collector.available_money -= artifact.price
            collector.available_space -= artifact.space_required
            self.SOLD_ARTIFACTS += 1

            return f"{collector.name} purchased {artifact.name} for a price of {artifact.price:.2f}."

        else:
            return "Purchase is impossible."

    def remove_artifact(self, artifact_name: str):

        artifact = [a for a in self.artifacts if a.name == artifact_name]
        if not artifact:
            return "No such artifact."

        self.artifacts.remove(artifact[0])
        return f"Removed {artifact[0].artifact_information()}"

    def fundraising_campaigns(self, max_money: float):

        count = 0

        for c in self.collectors:
            if c.available_money <= max_money:
                c.increase_money()
                count += 1

        return f"{count} collector/s increased their available money."

    def get_auction_report(self):

        result = [f"**Auction statistics**\nTotal number of sold artifacts: {self.SOLD_ARTIFACTS}\nAvailable artifacts for sale: {len(self.artifacts)}\n***"]

        collectors = sorted(self.collectors, key=lambda x: (-len(x.purchased_artifacts), x.name))

        for c in collectors:
            result.append(str(c))

        return "\n".join(result)
