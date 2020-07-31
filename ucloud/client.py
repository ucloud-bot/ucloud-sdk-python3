""" Code is generated by ucloud-model, DO NOT EDIT IT. """

from ucloud.core import client


class Client(client.Client):
    def __init__(
        self, config: dict, transport=None, middleware=None, logger=None
    ):
        self._config = config
        super(Client, self).__init__(config, transport, middleware, logger)

    def pathx(self):
        from ucloud.services.pathx.client import PathXClient

        return PathXClient(
            self._config, self.transport, self.middleware, self.logger
        )

    def stepflow(self):
        from ucloud.services.stepflow.client import StepFlowClient

        return StepFlowClient(
            self._config, self.transport, self.middleware, self.logger
        )

    def uaccount(self):
        from ucloud.services.uaccount.client import UAccountClient

        return UAccountClient(
            self._config, self.transport, self.middleware, self.logger
        )

    def ucdn(self):
        from ucloud.services.ucdn.client import UCDNClient

        return UCDNClient(
            self._config, self.transport, self.middleware, self.logger
        )

    def udb(self):
        from ucloud.services.udb.client import UDBClient

        return UDBClient(
            self._config, self.transport, self.middleware, self.logger
        )

    def udpn(self):
        from ucloud.services.udpn.client import UDPNClient

        return UDPNClient(
            self._config, self.transport, self.middleware, self.logger
        )

    def udisk(self):
        from ucloud.services.udisk.client import UDiskClient

        return UDiskClient(
            self._config, self.transport, self.middleware, self.logger
        )

    def uhost(self):
        from ucloud.services.uhost.client import UHostClient

        return UHostClient(
            self._config, self.transport, self.middleware, self.logger
        )

    def ulb(self):
        from ucloud.services.ulb.client import ULBClient

        return ULBClient(
            self._config, self.transport, self.middleware, self.logger
        )

    def umem(self):
        from ucloud.services.umem.client import UMemClient

        return UMemClient(
            self._config, self.transport, self.middleware, self.logger
        )

    def unet(self):
        from ucloud.services.unet.client import UNetClient

        return UNetClient(
            self._config, self.transport, self.middleware, self.logger
        )

    def uphost(self):
        from ucloud.services.uphost.client import UPHostClient

        return UPHostClient(
            self._config, self.transport, self.middleware, self.logger
        )

    def usms(self):
        from ucloud.services.usms.client import USMSClient

        return USMSClient(
            self._config, self.transport, self.middleware, self.logger
        )

    def ipsecvpn(self):
        from ucloud.services.ipsecvpn.client import IPSecVPNClient

        return IPSecVPNClient(
            self._config, self.transport, self.middleware, self.logger
        )

    def ucloudstack(self):
        from ucloud.services.ucloudstack.client import UCloudStackClient

        return UCloudStackClient(
            self._config, self.transport, self.middleware, self.logger
        )

    def ufs(self):
        from ucloud.services.ufs.client import UFSClient

        return UFSClient(
            self._config, self.transport, self.middleware, self.logger
        )

    def uhub(self):
        from ucloud.services.uhub.client import UHubClient

        return UHubClient(
            self._config, self.transport, self.middleware, self.logger
        )

    def vpc(self):
        from ucloud.services.vpc.client import VPCClient

        return VPCClient(
            self._config, self.transport, self.middleware, self.logger
        )
