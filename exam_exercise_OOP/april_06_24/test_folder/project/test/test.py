from unittest import TestCase, main
from project.social_media import SocialMedia


class TestSocialMedia(TestCase):

    def setUp(self) -> None:
        self.media = SocialMedia("Peter", "YouTube", 3500, "podcast")

    def test_username(self):
        self.assertEqual("Peter", self.media._username)

    def test_validate_and_set_platform(self):
        self.assertEqual("YouTube", self.media.platform)
        with self.assertRaises(ValueError) as m:
            self.media.platform = "Facebook"
        self.assertEqual("Platform should be one of ['Instagram', 'YouTube', 'Twitter']", str(m.exception))

    def test_followers(self):
        self.assertEqual(3500, self.media.followers)
        with self.assertRaises(ValueError) as m:
            self.media.followers = -1
        self.assertEqual("Followers cannot be negative.", str(m.exception))

    def test_content_type(self):
        self.assertEqual("podcast", self.media._content_type)

    def test_posts(self):
        self.assertEqual([], self.media._posts)

    def test_create_comment_and_like_post(self):
        self.assertEqual(f"New podcast post created by Peter on YouTube.", self.media.create_post("say_hi"))
        self.assertEqual([{'content': 'say_hi', 'likes': 0, 'comments': []}], self.media._posts)

        self.assertEqual("Invalid post index.", self.media.like_post(1))
        self.assertEqual("Post liked by Peter.", self.media.like_post(0))
        for _ in range(9):
            self.media.like_post(0)
        self.assertEqual([{'content': 'say_hi', 'likes': 10, 'comments': []}], self.media._posts)
        self.assertEqual("Post has reached the maximum number of likes.", self.media.like_post(0))
        self.assertEqual([{'content': 'say_hi', 'likes': 10, 'comments': []}], self.media._posts)

        self.assertEqual("Comment should be more than 10 characters.", self.media.comment_on_post(0, "Not valid"))
        self.assertEqual("Comment added by Peter on the post.", self.media.comment_on_post(0, "This is comment"))
        self.assertEqual([{'content': 'say_hi', 'likes': 10, 'comments': [{'user': 'Peter', 'comment': 'This is comment'}]}], self.media._posts)


if __name__ == "__main__":
    main()