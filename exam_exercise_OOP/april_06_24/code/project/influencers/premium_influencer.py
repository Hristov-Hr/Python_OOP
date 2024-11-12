from project.influencers.base_influencer import BaseInfluencer


class PremiumInfluencer(BaseInfluencer):

    PAYMENT_PERCENTAGE = 0.85

    def reached_followers(self, campaign_type: str):
        multiply = 1.5 if campaign_type == "HighBudgetCampaign" else 0.8

        return int(self.followers * self.engagement_rate * multiply)