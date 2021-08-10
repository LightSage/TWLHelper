from jishaku.features.management import ManagementFeature


class CustomJishaku(ManagementFeature):
    ...


def setup(bot):
    bot.add_cog(CustomJishaku(bot=bot))

