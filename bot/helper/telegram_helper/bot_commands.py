from bot import CMD_INDEX


class _BotCommands:
    def __init__(self):
        self.StartCommand = f'start{CMD_INDEX}'
        self.MirrorCommand = f'dmirror{CMD_INDEX}'
        self.UnzipMirrorCommand = f'dunzipmirror{CMD_INDEX}'
        self.ZipMirrorCommand = f'dzipmirror{CMD_INDEX}'
        self.CancelMirror = f'cancel{CMD_INDEX}'
        self.CancelAllCommand = f'cancelall{CMD_INDEX}'
        self.ListCommand = f'list{CMD_INDEX}'
        self.SearchCommand = f'search{CMD_INDEX}'
        self.StatusCommand = f'status{CMD_INDEX}'
        self.AuthorizedUsersCommand = f'users{CMD_INDEX}'
        self.AuthorizeCommand = f'authorize{CMD_INDEX}'
        self.UnAuthorizeCommand = f'unauthorize{CMD_INDEX}'
        self.AddSudoCommand = f'addsudo{CMD_INDEX}'
        self.RmSudoCommand = f'rmsudo{CMD_INDEX}'
        self.PingCommand = f'ping{CMD_INDEX}'
        self.RestartCommand = f'restart{CMD_INDEX}'
        self.StatsCommand = f'stats{CMD_INDEX}'
        self.HelpCommand = f'dhelp{CMD_INDEX}'
        self.LogCommand = f'log{CMD_INDEX}'
        self.SpeedCommand = f'speedtest{CMD_INDEX}'
        self.CloneCommand = f'dclone{CMD_INDEX}'
        self.CountCommand = f'dcount{CMD_INDEX}'
        self.WatchCommand = f'dwatch{CMD_INDEX}'
        self.ZipWatchCommand = f'dzipwatch{CMD_INDEX}'
        self.QbMirrorCommand = f'dqbmirror{CMD_INDEX}'
        self.QbUnzipMirrorCommand = f'dqbunzipmirror{CMD_INDEX}'
        self.QbZipMirrorCommand = f'dqbzipmirror{CMD_INDEX}'
        self.DeleteCommand = f'del{CMD_INDEX}'
        self.ShellCommand = f'shell{CMD_INDEX}'
        self.ExecHelpCommand = f'exechelp{CMD_INDEX}'
        self.LeechSetCommand = f'leechset{CMD_INDEX}'
        self.SetThumbCommand = f'setthumb{CMD_INDEX}'
        self.LeechCommand = f'leech{CMD_INDEX}'
        self.UnzipLeechCommand = f'leechunzip{CMD_INDEX}'
        self.ZipLeechCommand = f'leechzip{CMD_INDEX}'
        self.QbLeechCommand = f'qbleech{CMD_INDEX}'
        self.QbUnzipLeechCommand = f'qbleechunzip{CMD_INDEX}'
        self.QbZipLeechCommand = f'qbleechzip{CMD_INDEX}'
        self.LeechWatchCommand = f'leechwatch{CMD_INDEX}'
        self.LeechZipWatchCommand = f'leechzipwatch{CMD_INDEX}'
        self.RssListCommand = f'rsslist{CMD_INDEX}'
        self.RssGetCommand = f'rssget{CMD_INDEX}'
        self.RssSubCommand = f'rsssub{CMD_INDEX}'
        self.RssUnSubCommand = f'rssunsub{CMD_INDEX}'
        self.RssUnSubAllCommand = f'rssunsuball{CMD_INDEX}'

BotCommands = _BotCommands()
