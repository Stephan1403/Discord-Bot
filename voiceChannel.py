class voiceChannel:
    def __init__(self, name, member, channel, textChannel=None) -> None:
        self.name = name
        self.member = member
        self.channel = channel
        self.textChannel = textChannel
        self.category = channel.category