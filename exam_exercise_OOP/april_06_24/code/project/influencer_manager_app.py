from typing import List

from project.campaigns.base_campaign import BaseCampaign
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    VALID_INFLUENCER_TYPE = {"PremiumInfluencer": PremiumInfluencer, "StandardInfluencer": StandardInfluencer}
    VALID_CAMPAIGN_TYPE = {"HighBudgetCampaign": HighBudgetCampaign, "LowBudgetCampaign": LowBudgetCampaign}

    def __init__(self):
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):

        if influencer_type not in self.VALID_INFLUENCER_TYPE.keys():
            return f"{influencer_type} is not an allowed influencer type."

        try:
            next(filter(lambda x: x.username == username, self.influencers))
            return f"{username} is already registered."

        except StopIteration:
            self.influencers.append(self.VALID_INFLUENCER_TYPE[influencer_type](username, followers, engagement_rate))
            return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):

        if campaign_type not in self.VALID_CAMPAIGN_TYPE.keys():
            return f"{campaign_type} is not a valid campaign type."

        try:
            next(filter(lambda x: campaign_id == x.campaign_id, self.campaigns))
            return f"Campaign ID {campaign_id} has already been created."

        except StopIteration:
            self.campaigns.append(self.VALID_CAMPAIGN_TYPE[campaign_type](campaign_id, brand, required_engagement))
            return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):

        try:
            influencer = next(filter(lambda x: x.username == influencer_username, self.influencers))

        except StopIteration:
            return f"Influencer '{influencer_username}' not found."

        try:
            campaign = next(filter(lambda x: x.campaign_id == campaign_id, self.campaigns))

        except StopIteration:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign with ID {campaign_id}."

        payment = influencer.calculate_payment(campaign)

        if payment > 0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= payment
            influencer.campaigns_participated.append(campaign)
            return f"Influencer '{influencer_username}' has successfully participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):
        result = {}

        for c in self.campaigns:
            f = sum(i.reached_followers(c) for i in c.approved_influencers)
            if f > 0:
                result[c] = f

        return result

    def influencer_campaign_report(self, username: str):

        influencer = [i for i in self.influencers if i.username == username][0]

        return influencer.display_campaigns_participated()

    def campaign_statistics(self):

        result = ["$$ Campaign Statistics $$", ]
        for c in sorted(self.campaigns, key= lambda x: (len(x.approved_influencers), -x.budget)):
            result.append(
                f"  * Brand: {c.brand}, Total influencers: {len(c.approved_influencers)}, "
                f"Total budget: ${c.budget:.2f}, Total reached followers: {sum(i.reached_followers(c) for i in c.approved_influencers)}")

        return "\n".join(result)
