from project.influencers.base_influencer import BaseInfluencer


class StandardInfluencer(BaseInfluencer):

    PAYMENT_PERCENTAGE = 0.45

    def reached_followers(self, campaign_type: str):
        multiply = 1.2 if campaign_type == "HighBudgetCampaign" else 0.9

        return int(self.followers * self.engagement_rate * multiply)